# Layout-Aware PDF Translator

將英文論文 PDF 翻譯為繁體中文 PDF，並盡量保留雙欄排版、圖片、表格與公式。

## 功能特色
- 以 PyMuPDF 在原頁面上覆寫文字，而非重排整頁。
- Layout-Aware Text Fitter：先調行高，再安全擴張 bbox，再降字級，最後 overflow。
- Obstacle map + collision detection，避免撞到圖片/表格/其他段落。
- Overflow Appendix：主文標記 `[+...]`，完整內容附錄保存。
- tkinter GUI，支援 Dummy/OpenAI/DeepL 翻譯器。

## 安裝
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 字型
將 Noto Sans/Serif TC 字型放進 `fonts/`。

## 使用
```bash
python main.py
```

## 打包
```bash
build/build_exe.bat
```

## 限制
- 複雜 PDF 無法保證 100% 完美還原。
- 掃描 PDF 需 OCR（目前保留介面）。
- API 翻譯可能產生費用。

## License
MIT
