from dataclasses import dataclass
from typing import List, Tuple
BBox = Tuple[float,float,float,float]

@dataclass
class TextBlock:
    block_id:int
    text:str
    bbox:BBox
    font_size:float


def extract_text_blocks(page_dict: dict) -> List[TextBlock]:
    out=[]
    bid=0
    for b in page_dict.get('blocks',[]):
        if b.get('type',0)!=0: continue
        lines=[]; size=10.0
        for ln in b.get('lines',[]):
            for sp in ln.get('spans',[]):
                t=sp.get('text','').strip()
                if t: lines.append(t); size=sp.get('size',size)
        txt=' '.join(lines).strip()
        if txt:
            out.append(TextBlock(bid,txt,tuple(b['bbox']),size)); bid+=1
    return out
