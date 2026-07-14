"""缓存模块 — 避免重复调用 API 花冤枉钱"""
import os
import json
import hashlib


def _fingerprint(text: str) -> str:
    """取文章前 500 字的 MD5 作为缓存键"""
    return hashlib.md5(text.strip()[:500].encode("utf-8")).hexdigest()


def load_cache(cache_file: str) -> dict:
    """读本地缓存"""
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache_file: str, key: str, result: dict):
    """写缓存到本地 JSON"""
    cache = load_cache(cache_file)
    cache[key] = result
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def get_cached_or_none(cache_file: str, text: str) -> dict | None:
    """查缓存，命中返回结果，未命中返回 None"""
    key = _fingerprint(text)
    cached = load_cache(cache_file).get(key)
    if cached:
        print("  ↩  命中缓存，跳过 API 调用")
    return cached
