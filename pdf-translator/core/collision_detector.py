def intersects(a,b,margin=0):
    return not (a[2]<=b[0]+margin or a[0]>=b[2]-margin or a[3]<=b[1]+margin or a[1]>=b[3]-margin)

def has_collision(target,obstacles):
    return any(intersects(target,o) for o in obstacles)

def distance_to_nearest_obstacle_down(t,obs,page_bottom):
    c=[o[1]-t[3] for o in obs if o[1]>=t[3] and not (o[2]<=t[0] or o[0]>=t[2])]
    c.append(page_bottom-t[3]); return max(0,min(c))

def distance_to_nearest_obstacle_right(t,obs,col_right):
    c=[o[0]-t[2] for o in obs if o[0]>=t[2] and not (o[3]<=t[1] or o[1]>=t[3])]
    c.append(col_right-t[2]); return max(0,min(c))

def distance_to_nearest_obstacle_left(t,obs,col_left):
    c=[t[0]-o[2] for o in obs if o[2]<=t[0] and not (o[3]<=t[1] or o[1]>=t[3])]
    c.append(t[0]-col_left); return max(0,min(c))
