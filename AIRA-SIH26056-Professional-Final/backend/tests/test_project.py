from backend.sample_data import generate
from backend.services.core import clean,index
from backend.services.trustchain import Chain
def test_index():
 r=index(clean(generate(2)));assert r["apix"]>0 and r["routes_used"]==24
def test_chain():
 c=Chain();c.add({"a":1});c.add({"a":2});assert c.verify()
