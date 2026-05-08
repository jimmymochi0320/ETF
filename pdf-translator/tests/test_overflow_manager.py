from core.overflow_manager import OverflowManager
def test_overflow_record():
 o=OverflowManager(); o.add(page_number=1,block_id=1,original_text="a",translated_text="b",visible_text="b",overflow_text="")
 assert o.count()==1
