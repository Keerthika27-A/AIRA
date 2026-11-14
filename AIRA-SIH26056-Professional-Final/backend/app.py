from flask import Flask,jsonify,request
from flask_cors import CORS
from backend.sample_data import generate
from backend.services.core import clean,index,series,booking,heatmap,insights,quality
from backend.services.trustchain import Chain
app=Flask(__name__); CORS(app); chain=Chain(); DF=clean(generate(30))
@app.get("/")
def home(): return jsonify({"project":"AIRA - Airfare Index for Regulatory Analytics","status":"running","mode":"synthetic demonstration data"})
@app.get("/api/v1/dashboard/overview")
def overview():
 z=index(DF); p={"current_airfare_price_index":z["apix"],"routes_monitored":len(set(DF.sector)),"fare_observations":len(DF),"booking_periods":["T+1","T+7","T+15","T+30","T+45"],"data_quality":quality(DF),"insights":insights(DF),"methodology":z["methodology"]}; b=chain.add(p); p["data_integrity"]={"status":"VERIFIED","message":"The analytical snapshot is protected by a SHA-256 hash chain. Changing a protected snapshot changes its verification hash.","block_number":b["block_number"],"hash":b["hash"]}; return jsonify(p)
@app.get("/api/v1/index/daily")
def daily(): return jsonify(series(DF,"D"))
@app.get("/api/v1/index/weekly")
def weekly(): return jsonify(series(DF,"W"))
@app.get("/api/v1/index/monthly")
def monthly(): return jsonify(series(DF,"M"))
@app.get("/api/v1/routes")
def routes(): return jsonify(index(DF)["route_details"])
@app.get("/api/v1/analytics/booking-time")
def book():
 r=request.args.get("route"); x=booking(DF); return jsonify([a for a in x if not r or a["sector"]==r.upper()])
@app.get("/api/v1/analytics/heatmap")
def hm(): return jsonify(heatmap(DF))
@app.get("/api/v1/analytics/explanations")
def ex(): return jsonify(insights(DF))
@app.get("/api/v1/data-quality")
def dq():
 q=quality(DF); q["plain_explanation"]={"total_records":"Every fare observation received by the prototype.","available_quotes":"Quotes that were available for analysis.","outliers_flagged":"Statistically unusual fare values flagged using IQR checks.","missing_base_fares":"Records without a usable base-fare value.","sold_out":"Flights marked unavailable because seats were sold out.","cancelled":"Flights marked cancelled and excluded from fare analysis."}; return jsonify(q)
@app.get("/api/v1/backtesting")
def bt():
 x=series(DF,"D")
 for a in x:a["reference_value"]=round(a["apix"]*.97+3.2,2);a["absolute_difference"]=round(abs(a["apix"]-a["reference_value"]),2);a["percentage_difference"]=round(a["absolute_difference"]/a["reference_value"]*100,2)
 import math; dif=[a["apix"]-a["reference_value"] for a in x]; m={"mae":round(sum(abs(v) for v in dif)/len(dif),3),"rmse":round(math.sqrt(sum(v*v for v in dif)/len(dif)),3),"mean_percentage_difference":round(sum(a["percentage_difference"] for a in x)/len(x),3)}
 return jsonify({"days_compared":len(x),"comparison":x,"metrics":m,"note":"Demo reference values demonstrate the validation workflow only. Replace them with publicly available or otherwise permitted DGCA reference data before claiming final validation."})
@app.get("/api/v1/trustchain/verify")
def ver(): return jsonify({"verified":chain.verify(),"blocks":len(chain.blocks),"method":"SHA-256 tamper-evident hash chain"})
if __name__=="__main__": app.run(port=5000,debug=True)
