import textwrap

def wrap_text_to_width(text, font, font_size, max_width):
    cpl = max(1, int(max_width / (font_size * 0.9)))
    out = []
    for p in text.split("\n"):
        out += textwrap.wrap(p, width=cpl) or [""]
    return out

def estimate_text_height(lines, font_size, line_height):
    return len(lines) * font_size * line_height

def can_fit(text, bbox, font, font_size, line_height):
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    lines = wrap_text_to_width(text, font, font_size, w)
    return estimate_text_height(lines, font_size, line_height) <= h, lines

def fit_text(text, original_bbox, expanded_bbox, font, original_font_size, min_font_size=8):
    for box in [original_bbox, expanded_bbox]:
        for lh in [1.2, 1.15, 1.1, 1.05]:
            size = original_font_size
            while size >= min_font_size:
                ok, lines = can_fit(text, box, font, size, lh)
                if ok:
                    return {"bbox": box, "font_size": size, "line_height": lh, "lines": lines, "overflow": False}
                size -= 0.5
    return {"bbox": expanded_bbox, "font_size": min_font_size, "line_height": 1.05, "lines": [], "overflow": True}

def truncate_to_fit_with_marker(text, bbox, marker="[+...]"):
    max_chars = max(1, int(((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) / 120))
    if len(text) <= max_chars:
        return text, ""
    keep = max(1, max_chars - len(marker))
    return text[:keep] + marker, text[keep:]
