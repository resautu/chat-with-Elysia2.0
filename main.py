sys.path.append('./')
import gradio as gr
import webbrowser
import argparse
import sys
from parse import Parse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--api', action="store_true", default=False)
    parser.add_argument("--share", action="store_true", default=False, help="share gradio app")
    parser.add_argument("--colab", action="store_true", default=False, help="share gradio app")
    args = parser.parse_args()
    ps = Parse()

    with gr.Blocks() as app:
        gr.Markdown(
            "# <center> chat with Elysia2.0\n"
            "### <center> base on chatglm and vits\n"
        )
        with gr.Row():
            with gr.Column():
                textbox = gr.TextArea(label="对话内容",
                                        placeholder="Type your sentence here",
                                        value="你好！", elem_id=f"tts-input")
                with gr.Row():
                    with gr.Column():
                        max_length = gr.Slider(label="max length", minimum=0, maximum=4096, value=2048, step=1.0, interactive=True)
                        top_p = gr.Slider(label="top p", minimum=0, maximum=1, value=0.7, step=0.01, interactive=True)
                        temperature = gr.Slider(label="temperature", minimum=0, maximum=1, value=0.95, step=0.01, interactive=True)
                    with gr.Column():
                        ns = gr.Slider(label="emotion change", minimum=0.1, maximum=1.0, step=0.1, value=0.6, interactive=True)
                        nsw = gr.Slider(label="noise_scale", minimum=0.1, maximum=1.0, step=0.1, value=0.668, interactive=True)
                        ls = gr.Slider(label="language speed", minimum=0.1, maximum=2.0, step=0.1, value=1.2, interactive=True)
            with gr.Column():
                text_output = gr.Textbox(label="回复信息")
                audio_output = gr.Audio(label="音频信息", elem_id="tts-audio")
                generate = gr.Button("生成对话")
                upload = gr.UploadButton('读取聊天记录', file_types=['file'])
                logdown = gr.Button("记录当前聊天记录")
                upload.upload(ps.loadHistory, inputs=[upload])
                logdown.click(ps.logContent)
                generate.click(ps.PipeChat,
                            inputs=[textbox, max_length, top_p, temperature, ns, nsw, ls],
                            outputs=[text_output, audio_output])
                
    webbrowser.open("http://127.0.0.1:7860")
    app.launch(share=args.share)