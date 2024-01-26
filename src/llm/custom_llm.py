import os

from openai import OpenAI

from src.prompt.testcase_generator_prompt import TestCaseGeneratorPrompt
from src.util.image_util import ImageUtil
from src.util.log_util import LogUtil


class CustomLLM:
    def __init__(self):
        self.log = LogUtil()
        self.image_util = ImageUtil()
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def generate_testcase_using_vision(self, image_path, test_scenario):
        data_url = self.image_util.generate_data_url(image_path)

        # data_url = f"data:image/jpeg;base64,{base64_image}"

        prompt = TestCaseGeneratorPrompt.prepare_prompt(data_url, test_scenario)

        completion = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=prompt,
            max_tokens=4096,
            stream=True,
        )

        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            # yield full_response

        # print(completion)

        return full_response

