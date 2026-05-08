from core.bbox_expander import expand_bbox
from types import SimpleNamespace
def test_expand_no_cross():
 b=(10,10,50,30); ex=expand_bbox(b,[(10,35,80,60)],SimpleNamespace(height=200),0,100)
 assert ex[2]<=100
