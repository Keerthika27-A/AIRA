from datetime import date,timedelta
import random
from backend.config import ROUTES,BOOKING_WINDOWS,BASE

def generate(days=30,seed=26056):
 rng=random.Random(seed); out=[]; today=date.today()
 airlines=["IndiGo","Air India","Air India Express","Akasa Air","SpiceJet"]
 sources=["Sample Airline Portal","Sample OTA Feed"]
 for d in range(days):
  c=today-timedelta(days=days-1-d)
  for route in ROUTES:
   o,des=route.split('-')
   for win in BOOKING_WINDOWS:
    for airline in airlines:
     status="AVAILABLE" if rng.random()>.01 else rng.choice(["SOLD_OUT","CANCELLED"])
     if status=="AVAILABLE":
      base=round(BASE[route]*(1+d/days*.10)*(1+(45-win)/45*.55)*(1+rng.uniform(-.09,.10)),2)
      tax=round(base*.12+rng.uniform(220,600),2); udf=rng.choice([0,0,50,100]); conv=rng.choice([0,0,99,149]); total=round(base+tax+udf+conv,2)
     else: base=tax=udf=conv=total=None
     out.append({"origin":o,"destination":des,"sector":route,"carrier":airline,"source":rng.choice(sources),"collection_date":c.isoformat(),"travel_date":(c+timedelta(days=win)).isoformat(),"advance_purchase_days":win,"fare_class":"Economy","base_fare":base,"taxes":tax,"user_development_fee":udf,"convenience_charge":conv,"total_fare":total,"availability_status":status})
 return out
