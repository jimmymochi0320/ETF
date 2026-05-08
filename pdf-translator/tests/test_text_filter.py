from core.text_filter import should_translate

def test_filters():
    assert not should_translate('https://example.com')
    assert not should_translate('10.1000/xyz123')
    assert not should_translate('a@b.com')
    assert not should_translate('12345')
    assert should_translate('This is a paper.')
