from translators.base_translator import BaseTranslator
class DummyTranslator(BaseTranslator):
    def translate(self,text:str)->str: return "【中譯】"+text
