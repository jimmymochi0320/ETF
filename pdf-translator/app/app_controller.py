from pathlib import Path
from core.pdf_processor import PDFProcessor
from translators.dummy_translator import DummyTranslator
from translators.openai_translator import OpenAITranslator
from translators.deepl_translator import DeepLTranslator

class AppController:
    def __init__(self, logger_callback=None, progress_callback=None):
        self.logger_callback = logger_callback
        self.progress_callback = progress_callback

    def _log(self, msg: str):
        if self.logger_callback:
            self.logger_callback(msg)

    def create_translator(self, service: str, api_key: str):
        s = service.lower()
        if s == "openai":
            return OpenAITranslator(api_key=api_key)
        if s == "deepl":
            return DeepLTranslator(api_key=api_key)
        return DummyTranslator()

    def run(self, input_pdf: str, output_dir: str, service: str, api_key: str, enable_ocr: bool=False):
        translator = self.create_translator(service, api_key)
        out = Path(output_dir) / (Path(input_pdf).stem + "_zh_tw.pdf")
        p = PDFProcessor(translator=translator, logger=self._log, progress_callback=self.progress_callback, enable_ocr=enable_ocr)
        result = p.process(input_pdf, str(out))
        return result
