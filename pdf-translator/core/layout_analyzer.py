from statistics import median

def detect_columns(blocks,page_width:float):
    centers=[(b.bbox[0]+b.bbox[2])/2 for b in blocks]
    if len(centers)<4:
        return {"is_two_column":False,"split_x":page_width/2}
    m=median(centers)
    left=sum(1 for c in centers if c<m*0.95)
    right=sum(1 for c in centers if c>m*1.05)
    is_two=left>1 and right>1
    return {"is_two_column":is_two,"split_x":m if is_two else page_width/2}

def sort_blocks(blocks,layout):
    if not layout['is_two_column']:
        return sorted(blocks,key=lambda b:(b.bbox[1],b.bbox[0]))
    sx=layout['split_x']
    wide=[b for b in blocks if (b.bbox[2]-b.bbox[0])>0.6*(sx*2)]
    left=[b for b in blocks if b not in wide and b.bbox[2]<=sx]
    right=[b for b in blocks if b not in wide and b.bbox[0]>=sx]
    mid=[b for b in blocks if b not in wide and b not in left and b not in right]
    return sorted(wide,key=lambda b:b.bbox[1])+sorted(left,key=lambda b:b.bbox[1])+sorted(right,key=lambda b:b.bbox[1])+sorted(mid,key=lambda b:b.bbox[1])
