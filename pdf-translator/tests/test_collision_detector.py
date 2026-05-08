from core.collision_detector import intersects
def test_intersects():
 assert intersects((0,0,10,10),(5,5,15,15))
 assert not intersects((0,0,10,10),(11,11,15,15))
