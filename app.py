import gradio as gr
from transformers import pipeline

# 加载预训练模型
print("正在加载模型...")
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """分析文本情感"""
    if not text:
        return "请输入文本"
    
    result = classifier(text)[0]
    label = "积极" if result['label'] == "POSITIVE" else "消极"
    score = result['score']
    
    return f"情感: {label}\n置信度: {score:.2%}"

# 创建 Gradio 界面
with gr.Blocks(title="Hugging Face 演示") as demo:
    gr.Markdown("# 🤗 Hugging Face 情感分析演示")
    gr.Markdown("输入任意英文文本，AI 将分析其情感倾向")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                lines=5,
                placeholder="输入英文文本...",
                label="输入文本"
            )
            submit_btn = gr.Button("分析", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                lines=5,
                label="分析结果"
            )
    
    submit_btn.click(
        fn=analyze_sentiment,
        inputs=input_text,
        outputs=output_text
    )
    
    gr.Examples(
        examples=[
            ["I love this product! It's amazing!"],
            ["This is terrible and disappointing."],
            ["The weather is nice today."]
        ],
        inputs=input_text
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
