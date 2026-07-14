"""PDF 解析模块 — 支持多种解析引擎"""
import os

# ── 方案 A: pdfplumber（文本型 PDF，速度快）──
def _try_pdfplumber(filepath: str) -> str | None:
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages[:50]:  # 最多读 50 页
                t = page.extract_text()
                if t:
                    text_parts.append(t)
        full = "\n\n".join(text_parts)
        return full if len(full.strip()) > 100 else None
    except Exception:
        return None


# ── 方案 B: markitdown（复杂 PDF，OCR 友好）──
def _try_markitdown(filepath: str) -> str | None:
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(filepath)
        return result.text_content if len(result.text_content.strip()) > 100 else None
    except Exception:
        return None


# ── 方案 C: 纯文本（.txt / .md 直接读）──
def _try_text(filepath: str) -> str | None:
    ext = os.path.splitext(filepath)[1].lower()
    if ext in (".txt", ".md", ".markdown"):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        return text if len(text.strip()) > 50 else None
    return None


def read_file(filepath: str) -> dict:
    """
    统一入口：读取任意文件，返回 {"text": ..., "method": ..., "pages": ...}

    支持格式：
    - PDF（文本型 → pdfplumber；扫描型 → markitdown）
    - TXT / Markdown（直接读取）
    """
    if not os.path.exists(filepath):
        return {"text": "", "method": "error", "error": f"文件不存在: {filepath}"}

    ext = os.path.splitext(filepath)[1].lower()

    # 纯文本直接读
    text = _try_text(filepath)
    if text:
        return {"text": text, "method": "text", "pages": 1}

    # PDF 走两套引擎
    if ext == ".pdf":
        # 先试 pdfplumber（快，文本型 PDF）
        text = _try_pdfplumber(filepath)
        if text:
            return {"text": text, "method": "pdfplumber", "pages": text.count("\f") + 1}

        # 再试 markitdown（慢，但能处理扫描版）
        print("  ⏳ pdfplumber 提取失败，尝试 markitdown...")
        text = _try_markitdown(filepath)
        if text:
            return {"text": text, "method": "markitdown", "pages": len(text.split("\n\n"))}

        return {"text": "", "method": "error", "error": "无法解析此 PDF（可能是纯扫描图片，需 OCR）"}

    return {"text": "", "method": "error", "error": f"不支持的文件格式: {ext}"}
