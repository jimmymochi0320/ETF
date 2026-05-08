from translators.dummy_translator import DummyTranslator
def test_dummy():
 assert "中譯" in DummyTranslator().translate("abc")
