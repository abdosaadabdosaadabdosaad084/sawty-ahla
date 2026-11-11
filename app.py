import gradio as gr

def make_video(image, audio):
    if image is None:
        return None, "ارفع صورتك الأول"
    if audio is None:
        return None, "ارفع صوتك الأول"
    return None, "تمام! صورتك وصوتك اترفعوا، جاري توليد الفيديو..."

with gr.Blocks(title="صوتي أحلى", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎤 صوتي أحلى")
    gr.Markdown("حط صورتك وصوتك، واعمل فيديو كأنه حقيقي - ببلاش وبدون تعقيد")
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="1 - حط صورتك هنا", type="filepath")
            audio_input = gr.Audio(label="2 - حط صوتك المسجل من موبايلك", type="filepath")
            btn = gr.Button("اعمل الفيديو ✨", variant="primary")
        with gr.Column():
            video_output = gr.Video(label="الفيديو بتاعك هيظهر هنا")
            status = gr.Textbox(label="الحالة")
    btn.click(make_video, inputs=[image_input, audio_input], outputs=[video_output, status])
    gr.Markdown("---")
    gr.Markdown("### 🎙️ أو استنسخ صوتك")
    with gr.Row():
        clone_audio = gr.Audio(label="سجل 30 ثانية من صوتك", type="filepath")
        clone_text = gr.Textbox(label="اكتب الكلام اللي عايز يتقال بصوتك", placeholder="مثلا: ازيكم يا جماعة عاملين ايه؟")
    clone_btn = gr.Button("استنسخ صوتي")
    clone_output = gr.Audio(label="صوتك المستنسخ")

demo.launch()
