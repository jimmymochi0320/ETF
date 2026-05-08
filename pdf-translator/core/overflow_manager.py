class OverflowManager:
    def __init__(self): self.items=[]
    def add(self,**kwargs): self.items.append(kwargs)
    def count(self): return len(self.items)
    def render_appendix(self,doc,fontname='helv'):
        if not self.items: return
        page=doc.new_page()
        y=40
        page.insert_text((40,y),'翻譯溢位附錄',fontsize=16,fontname=fontname); y+=30
        for it in sorted(self.items,key=lambda x:(x['page_number'],x['block_id'])):
            lines=[f"第 {it['page_number']} 頁，段落 {it['block_id']}",f"原文：{it['original_text']}",f"完整譯文：{it['translated_text']}",""]
            for l in lines:
                page.insert_textbox((40,y,page.rect.width-40,y+60),l,fontsize=10,fontname=fontname)
                y+=24
                if y>page.rect.height-60: page=doc.new_page(); y=40
