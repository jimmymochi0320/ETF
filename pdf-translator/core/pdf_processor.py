import fitz
from core.text_extractor import extract_text_blocks
from core.text_filter import should_translate
from core.layout_analyzer import detect_columns, sort_blocks
from core.obstacle_detector import build_obstacles
from core.bbox_expander import expand_bbox
from core.text_fitter import fit_text, truncate_to_fit_with_marker
from core.overflow_manager import OverflowManager
from core.font_manager import get_cjk_font

class PDFProcessor:
    def __init__(self, translator, logger=print, progress_callback=None, enable_ocr=False):
        self.translator=translator; self.logger=logger; self.progress=progress_callback; self.enable_ocr=enable_ocr
    def process(self,input_pdf,output_pdf):
        doc=fitz.open(input_pdf); ov=OverflowManager(); fontfile=get_cjk_font()
        for i,page in enumerate(doc):
            pd=page.get_text('dict'); blocks=extract_text_blocks(pd); layout=detect_columns(blocks,page.rect.width); ordered=sort_blocks(blocks,layout)
            for b in ordered:
                if not should_translate(b.text): continue
                tr=self.translator.translate(b.text)
                obs=build_obstacles(page,blocks,b.block_id)['hard']
                col_left=0; col_right=page.rect.width
                if layout['is_two_column']:
                    sx=layout['split_x'];
                    if b.bbox[2]<=sx: col_right=sx
                    elif b.bbox[0]>=sx: col_left=sx
                ex=expand_bbox(b.bbox,obs,page.rect,col_left,col_right)
                plan=fit_text(tr,b.bbox,ex,'NotoSansTC',b.font_size)
                draw_box=fitz.Rect(*plan['bbox'])
                page.draw_rect(fitz.Rect(*b.bbox), color=(1,1,1), fill=(1,1,1), overlay=True)
                if plan['overflow']:
                    vis,rest=truncate_to_fit_with_marker(tr,draw_box)
                    page.insert_textbox(draw_box,vis,fontsize=plan['font_size'],fontfile=fontfile,color=(0,0,0))
                    ov.add(page_number=i+1,block_id=b.block_id,original_text=b.text,translated_text=tr,visible_text=vis,overflow_text=rest)
                else:
                    page.insert_textbox(draw_box, "\n".join(plan['lines']), fontsize=plan['font_size'], fontfile=fontfile, color=(0,0,0), lineheight=plan['line_height'])
            if self.progress: self.progress(i+1,len(doc))
        ov.render_appendix(doc)
        doc.save(output_pdf)
        return {"output_pdf":output_pdf,"overflow_count":ov.count()}
