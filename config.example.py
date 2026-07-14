"""
城市设计案例研究助手 — 配置文件
=================================
填写 API 密钥后，与 case_extractor.py 放同一目录即可运行。
支持多家国内 AI API，选一家填入，其余留空。
"""

# ──────────────────────────────────────────────────────────────
# 多选一：填入对应密钥，其余留空
# ──────────────────────────────────────────────────────────────

# DeepSeek — 几乎免费，100 篇文章约 ¥0.15
# 申请：https://platform.deepseek.com → API Keys
DEEPSEEK_API_KEY = ""

# 智谱 GLM-4-Flash — 完全免费
# 申请：https://open.bigmodel.cn → 控制台 → API 密钥
ZHIPU_API_KEY = ""

# 通义千问 — 新用户赠 ¥300
# 申请：https://dashscope.aliyuncs.com
QWEN_API_KEY = ""

# Moonshot (Kimi) — 长文本能力强，适合论文
# 申请：https://platform.moonshot.cn
MOONSHOT_API_KEY = ""

# 百度文心一言 (ERNIE) — 中文理解好
# 申请：https://console.bce.baidu.com/ai
ERNIE_API_KEY = ""

# ──────────────────────────────────────────────────────────────
# 改这一行来切换供应商
# ──────────────────────────────────────────────────────────────
ACTIVE_API = "deepseek"

# ──────────────────────────────────────────────────────────────
# 接口参数（通常不需要修改）
# ──────────────────────────────────────────────────────────────
API_REGISTRY = {
    "deepseek": {
        "key":      DEEPSEEK_API_KEY,
        "base_url": "https://api.deepseek.com",
        "model":    "deepseek-chat",
        "label":    "DeepSeek V3",
    },
    "zhipu": {
        "key":      ZHIPU_API_KEY,
        "base_url": "https://open.bigmodel.cn/api/paas/v4/",
        "model":    "glm-4-flash",
        "label":    "智谱 GLM-4-Flash【免费】",
    },
    "qwen": {
        "key":      QWEN_API_KEY,
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model":    "qwen-turbo",
        "label":    "通义千问 Turbo",
    },
    "moonshot": {
        "key":      MOONSHOT_API_KEY,
        "base_url": "https://api.moonshot.cn/v1",
        "model":    "moonshot-v1-8k",
        "label":    "Moonshot (Kimi)",
    },
    "ernie": {
        "key":      ERNIE_API_KEY,
        "base_url": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro",
        "model":    "ernie-speed-128k",
        "label":    "百度文心 ERNIE",
    },
}

# 输出目录
OUTPUT_DIR = "./research_output"
