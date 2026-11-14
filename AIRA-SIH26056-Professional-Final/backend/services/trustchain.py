import hashlib,json
class Chain:
 def __init__(self):self.blocks=[]
 def add(self,payload):
  prev=self.blocks[-1]["hash"] if self.blocks else "GENESIS"; h=hashlib.sha256((prev+json.dumps(payload,sort_keys=True,separators=(",",":"))).encode()).hexdigest(); b={"block_number":len(self.blocks)+1,"previous_hash":prev,"hash":h,"payload":payload}; self.blocks.append(b); return b
 def verify(self):
  prev="GENESIS"
  for b in self.blocks:
   if hashlib.sha256((prev+json.dumps(b["payload"],sort_keys=True,separators=(",",":"))).encode()).hexdigest()!=b["hash"]:return False
   prev=b["hash"]
  return True
