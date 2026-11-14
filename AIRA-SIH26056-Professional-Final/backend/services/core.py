import pandas as pd
from backend.config import BASE,WEIGHTS,BOOKING_WINDOWS,BOOKING_HELP,AIRPORTS

def clean(rows):
 df=pd.DataFrame(rows)
 for c in ["base_fare","taxes","user_development_fee","convenience_charge","total_fare","advance_purchase_days"]: df[c]=pd.to_numeric(df[c],errors="coerce")
 df=df.drop_duplicates(subset=["sector","carrier","source","collection_date","travel_date","advance_purchase_days"],keep="last").copy()
 df["availability_status"]=df["availability_status"].fillna("UNKNOWN").str.upper(); df["quality_flag"]="OK"; df.loc[df.availability_status!="AVAILABLE","quality_flag"]="UNAVAILABLE"; df.loc[(df.availability_status=="AVAILABLE")&df.base_fare.isna(),"quality_flag"]="MISSING_BASE_FARE"; df["is_outlier"]=False
 avail=df[(df.availability_status=="AVAILABLE")&df.base_fare.notna()]
 for _,g in avail.groupby(["sector","advance_purchase_days"]):
  if len(g)>=4:
   q1,q3=g.base_fare.quantile(.25),g.base_fare.quantile(.75); i=q3-q1; m=(g.base_fare<q1-1.5*i)|(g.base_fare>q3+1.5*i); df.loc[g.index[m],"is_outlier"]=True
 return df

def eligible(df): return df[(df.availability_status=="AVAILABLE")&(~df.is_outlier)&df.base_fare.notna()]
def index(df):
 data=eligible(df); rows=[]
 for r,g in data.groupby("sector"):
  fare=float(g.base_fare.median()); rel=fare/BASE[r]*100; o,d=r.split("-"); rows.append({"route":r,"origin":o,"destination":d,"origin_details":AIRPORTS[o],"destination_details":AIRPORTS[d],"representative_base_fare":round(fare,2),"price_index":round(rel,2),"weight":WEIGHTS[r]})
 if not rows:return {"apix":0,"routes_used":0,"route_details":[]}
 x=pd.DataFrame(rows); return {"apix":round(float((x.price_index*x.weight).sum()/x.weight.sum()),2),"routes_used":len(rows),"route_details":rows,"methodology":"Weighted route price relatives; prototype base period = 100."}
def series(df,freq):
 d=df.copy(); d.collection_date=pd.to_datetime(d.collection_date); out=[]
 for p,g in d.groupby(pd.Grouper(key="collection_date",freq=freq)):
  if len(g):
   z=index(g); out.append({"period":p.strftime("%Y-%m-%d" if freq=="D" else "%Y-%m"),"apix":z["apix"],"routes_used":z["routes_used"]})
 return out
def booking(df):
 g=eligible(df).groupby(["sector","advance_purchase_days"]).base_fare.median().reset_index(); g["booking_label"]=g.advance_purchase_days.map(BOOKING_WINDOWS); g["booking_help"]=g.advance_purchase_days.map(BOOKING_HELP); g["median_base_fare"]=g.base_fare.round(2); return g[["sector","advance_purchase_days","booking_label","booking_help","median_base_fare"]].to_dict("records")
def heatmap(df):
 rows=booking(df); vals=[x["median_base_fare"] for x in rows]; lo,hi=min(vals),max(vals)
 return [{**x,"relative_price_score":round(50 if hi==lo else (x["median_base_fare"]-lo)/(hi-lo)*100)} for x in rows]
def insights(df):
 rows=booking(df); by={}
 for x in rows: by.setdefault(x["sector"],[]).append(x)
 out=[]
 for r,a in by.items():
  a=sorted(a,key=lambda x:x["advance_purchase_days"])
  early=max(a,key=lambda x:x["advance_purchase_days"]); late=min(a,key=lambda x:x["advance_purchase_days"])
  pct=(late["median_base_fare"]-early["median_base_fare"])/early["median_base_fare"]*100
  # Prototype explainability model: booking-window effect is measured directly; fuel/USD are contextual indicators.
  out.append({"route":r,"fare_change_percent":round(pct,1),"primary_reason":"Short booking window / demand pressure","reasons":[{"factor":"Booking window","impact":"High","explanation":f"T+1 is {pct:.1f}% higher than T+45 in this prototype dataset."},{"factor":"ATF fuel indicator","impact":"Contextual","explanation":"Fuel costs are shown as an explanatory signal and are not claimed as a proven causal value in the synthetic prototype."},{"factor":"USD/INR indicator","impact":"Contextual","explanation":"Currency movement is shown as an explanatory signal because some aviation costs can be currency-sensitive."}],"message":f"The strongest measured signal for {r} is the shorter booking window; T+1 is about {pct:.1f}% above T+45."})
 return out
def quality(df):
 return {"total_records":len(df),"available_quotes":int((df.availability_status=="AVAILABLE").sum()),"sold_out":int((df.availability_status=="SOLD_OUT").sum()),"cancelled":int((df.availability_status=="CANCELLED").sum()),"outliers_flagged":int(df.is_outlier.sum()),"missing_base_fares":int((df.quality_flag=="MISSING_BASE_FARE").sum()),"data_quality_rate":round(float(((df.availability_status=="AVAILABLE").sum()-df.is_outlier.sum())/len(df)*100),2)}
