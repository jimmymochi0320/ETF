class OCREngine:
    def suggest_ocr(self, page_text:str)->bool:
        return not bool(page_text.strip())
