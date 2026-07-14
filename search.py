"""学术搜索模块 — Semantic Scholar + 网页抓取"""
import re
from typing import Optional

try:
    import requests
    import urllib3
    urllib3.disable_warnings()
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


def search_semantic_scholar(query: str, max_results: int = 8) -> list:
    """
    通过 Semantic Scholar API 搜索英文学术文献。
    免费、无需 API Key，建议用英文搜索词。
    """
    if not HAS_REQUESTS:
        print("⚠  缺少 requests 包：pip install requests")
        return []

    params = {
        "query":  query,
        "limit":  min(max_results, 20),
        "fields": "title,abstract,year,authors,url,openAccessPdf",
    }
    headers = {"User-Agent": "Mozilla/5.0 (academic research tool)"}

    try:
        resp = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params=params, headers=headers, timeout=15
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"⚠  Semantic Scholar 搜索失败: {e}")
        return []

    results = []
    for p in data.get("data", []):
        results.append({
            "title":    p.get("title", "Unknown"),
            "abstract": p.get("abstract") or "No abstract.",
            "year":     p.get("year", "N/A"),
            "authors":  ", ".join(a["name"] for a in p.get("authors", [])[:3]),
            "url":      p.get("url", ""),
            "pdf_url":  (p.get("openAccessPdf") or {}).get("url"),
            "source":   "Semantic Scholar",
        })
    return results


def fetch_url_content(url: str) -> Optional[str]:
    """
    从 URL 抓取文章正文。
    CNKI / 万方等需登录的页面请手动复制，不要用此函数。
    """
    if not (HAS_REQUESTS and HAS_BS4):
        print("⚠  缺少 requests 或 beautifulsoup4")
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        resp.encoding = resp.apparent_encoding

        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style","nav","header","footer","aside","iframe"]):
            tag.decompose()

        body = (
            soup.find("article") or
            soup.find(class_=re.compile(r"article|content|main|body", re.I)) or
            soup.find("main") or
            soup.body
        )
        if not body:
            return None

        text = body.get_text(separator="\n")
        text = re.sub(r'\n{3,}', '\n\n', text).strip()
        return text if len(text) > 200 else None

    except Exception as e:
        print(f"⚠  抓取失败 ({url[:60]}): {e}")
        return None
