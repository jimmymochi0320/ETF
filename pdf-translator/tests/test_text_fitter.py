from core.text_fitter import fit_text
def test_fit_or_overflow():
 r=fit_text("hello "*100,(0,0,50,20),(0,0,70,40),"f",10)
 assert "overflow" in r
