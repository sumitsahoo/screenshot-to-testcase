import gradio as gr

from src.llm.custom_llm import CustomLLM
from src.util.log_util import LogUtil


class GradioUI:
    def __init__(self):
        self.log = LogUtil()
        self.llm = CustomLLM()
        self.primary_color = "#226FD4"

        self.theme = gr.themes.Base(
            primary_hue="purple",
            secondary_hue="purple",
        ).set(
            # button_primary_background_fill="*secondary_500",
            button_primary_background_fill=self.primary_color,
            button_primary_background_fill_dark="*primary_500",
            button_primary_text_color="white",
            loader_color=self.primary_color,
        )

    def launch_ui(self):
        # Check if index is built

        with gr.Blocks(
            title="Screenshot to Test Case",
            theme=self.theme,
            # css=custom_css,
        ) as generate_testcase:
            gr.Image(
                "./images/logo.png",
                height=50,
                width=210,
                interactive=False,
                container=False,
                show_download_button=False,
            )

            with gr.Tab("Generate K6 Test Case"):
                gr.Textbox(
                    value="Upload a screenshot of a webpage and enter a test scenario to generate a K6 test case. Generated code may not be perfect or accurate, but it should be a good starting point for further development.",
                    show_label=False,
                    interactive=False,
                    container=False,
                )

                gr.Interface(
                    fn=self.llm.generate_testcase_using_vision,
                    inputs=[
                        gr.Image(
                            label="Select webpage screenshot",
                            sources=["upload"],
                            type="filepath",
                            height=400,
                        ),
                        gr.Textbox(
                            label="Test scenario",
                            show_copy_button=True,
                        ),
                    ],
                    outputs=[
                        gr.Code(
                            label="Generated K6 Test Case",
                        ),
                    ],
                    examples=[[
                        "./images/example/example1.png","Create an employee by filling all the fields and clicking on the save button. You can use dummy data for the fields."
                    ]],
                    allow_flagging="never",
                )
           

        generate_testcase.queue().launch(
            favicon_path="./images/favicon.ico",
            debug=False,
            show_api=False,
            server_name="0.0.0.0",
            server_port=8080,
            share=False,
            allowed_paths=["./images/", "./outputs/"],
        )
