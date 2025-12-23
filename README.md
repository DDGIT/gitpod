# Hugging Face Gitpod 环境

这是一个预配置的 Gitpod 环境，用于在 Hugging Face 上进行机器学习开发。

## 快速开始

点击下面的按钮在 Gitpod 中打开此项目：

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#你的仓库URL)

## 已安装的工具

- Python 3
- transformers - Hugging Face 的 Transformers 库
- datasets - 数据集处理
- torch - PyTorch 深度学习框架
- gradio - 快速创建 ML 演示界面
- huggingface_hub - Hugging Face Hub API

## 使用示例

创建一个简单的 Gradio 应用：

```python
import gradio as gr
from transformers import pipeline

# 加载预训练模型
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    return f"{result['label']}: {result['score']:.4f}"

# 创建 Gradio 界面
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="输入文本..."),
    outputs="text",
    title="情感分析演示"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
```

## 端口配置

- 端口 7860：Gradio 应用默认端口（自动打开预览）
