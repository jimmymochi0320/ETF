def build_obstacles(page,blocks,current_block_id=None):
    hard=[]
    for b in blocks:
        if b.block_id!=current_block_id: hard.append(b.bbox)
    for img in page.get_images(full=True):
        pass
    for dr in page.get_drawings():
        r=dr.get('rect')
        if r: hard.append((r.x0,r.y0,r.x1,r.y1))
    h=page.rect.height
    hard.append((0,0,page.rect.width,0.05*h))
    hard.append((0,0.95*h,page.rect.width,h))
    return {"hard":hard,"soft":[]}
