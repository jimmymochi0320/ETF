from core.collision_detector import *

def expand_bbox(bbox, obstacles, page_rect, col_left, col_right, max_scale=1.5, margin=2):
    x0,y0,x1,y1=bbox
    h=y1-y0
    max_h=h*max_scale
    d=distance_to_nearest_obstacle_down((x0,y0,x1,y1),obstacles,page_rect.height)-margin
    y1=min(y1+max(0,min(d,max_h-h)),page_rect.height)
    r=distance_to_nearest_obstacle_right((x0,y0,x1,y1),obstacles,col_right)-margin
    l=distance_to_nearest_obstacle_left((x0,y0,x1,y1),obstacles,col_left)-margin
    x1=min(col_right,x1+max(0,min(r,20)))
    x0=max(col_left,x0-max(0,min(l,20)))
    return (x0,y0,x1,y1)
