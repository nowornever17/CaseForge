"""格式化与保存模块"""
import os
import json
from datetime import datetime


def format_result(result: dict, title: str = "") -> str:
    """在终端美观地打印提取结果"""
    sep = "─" * 52
    return "\n".join([
        "",
        "=" * 52,
        f"  {title or '案例分析'}",
        f"  来源：{result.get('model', '未知')}",
        "=" * 52,
        "",
        "【背景与冲突】",
        result.get("background") or "（未提取到）",
        "",
        "【关键决策或方案】",
        result.get("decisions") or "（未提取到）",
        "",
        "【经验与教训】",
        result.get("lessons") or "（未提取到）",
        "",
        sep,
    ])


def save_results(results: list, output_dir: str, prefix: str = "analysis"):
    """
    保存为 Markdown + JSON 双格式
    """
    os.makedirs(output_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    md_path   = os.path.join(output_dir, f"{prefix}_{ts}.md")
    json_path = os.path.join(output_dir, f"{prefix}_{ts}.json")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# 城市设计案例精华摘录\n\n")
        f.write(f"_生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}，")
        f.write(f"共 {len(results)} 篇，模型：{results[0].get('model','') if results else ''}_ \n\n")
        for r in results:
            t = r.get("title", "未知案例")
            f.write(f"## {t}\n\n")
            f.write(f"**背景与冲突**\n\n{r.get('background','未提取到')}\n\n")
            f.write(f"**关键决策或方案**\n\n{r.get('decisions','未提取到')}\n\n")
            f.write(f"**经验与教训**\n\n{r.get('lessons','未提取到')}\n\n")
            f.write("---\n\n")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n  💾  结果已保存：")
    print(f"      Markdown → {md_path}")
    print(f"      JSON     → {json_path}")
    return md_path, json_path
