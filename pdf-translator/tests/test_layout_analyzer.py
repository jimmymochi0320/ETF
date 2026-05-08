from core.layout_analyzer import detect_columns
from types import SimpleNamespace
def test_two_column():
 b=[SimpleNamespace(bbox=(10,10,100,20)),SimpleNamespace(bbox=(15,30,100,40)),SimpleNamespace(bbox=(300,10,390,20)),SimpleNamespace(bbox=(310,30,395,40))]
 r=detect_columns(b,400)
 assert r["is_two_column"]
