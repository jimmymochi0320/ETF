from pathlib import Path

def get_cjk_font():
    p=Path(__file__).resolve().parents[1]/'fonts'
    for n in ['NotoSansTC-Regular.ttf','NotoSansTC-Medium.ttf','NotoSerifTC-Regular.ttf']:
        f=p/n
        if f.exists(): return str(f)
    return None
