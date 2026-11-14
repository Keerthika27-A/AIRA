ROUTES=["DEL-BOM","DEL-BLR","DEL-CCU","DEL-HYD","DEL-MAA","BOM-BLR","BOM-HYD","BOM-MAA","BOM-CCU","BOM-PNQ","BLR-HYD","BLR-MAA","BLR-CCU","BLR-PNQ","MAA-HYD","MAA-CCU","HYD-CCU","TRZ-MAA","CJB-MAA","IXM-MAA","CJB-BLR","TRZ-BLR","IXM-BLR","CJB-HYD"]
BOOKING_WINDOWS={1:"T+1",7:"T+7",15:"T+15",30:"T+30",45:"T+45"}
BOOKING_HELP={1:"Tomorrow / 1 day before travel",7:"7 days before travel",15:"15 days before travel",30:"30 days before travel",45:"45 days before travel"}
AIRPORTS={
"DEL":{"city":"Delhi","airport":"Indira Gandhi International Airport"},
"BOM":{"city":"Mumbai (Bombay)","airport":"Chhatrapati Shivaji Maharaj International Airport"},
"BLR":{"city":"Bengaluru (Bangalore)","airport":"Kempegowda International Airport"},
"CCU":{"city":"Kolkata (Calcutta)","airport":"Netaji Subhas Chandra Bose International Airport"},
"HYD":{"city":"Hyderabad","airport":"Rajiv Gandhi International Airport"},
"MAA":{"city":"Chennai (Madras)","airport":"Chennai International Airport"},
"PNQ":{"city":"Pune","airport":"Pune International Airport"},
"TRZ":{"city":"Tiruchirappalli (Trichy)","airport":"Tiruchirappalli International Airport"},
"CJB":{"city":"Coimbatore","airport":"Coimbatore International Airport"},
"IXM":{"city":"Madurai","airport":"Madurai Airport"}
}
BASE={r:3000+((i*473)%3600) for i,r in enumerate(ROUTES)}
WEIGHTS={r:1/len(ROUTES) for r in ROUTES}
