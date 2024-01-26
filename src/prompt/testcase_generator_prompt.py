class TestCaseGeneratorPrompt:
    SYSTEM_PROMPT = """
    You are an expert K6 browser test case developer using the K6 Chromium module.
    You take test case scenarios from the user, and then generate K6 browser test cases based on them.
    You will be given a web page screenshot and asked to create test cases that validate the functionality and performance of the page.

    - Ensure the test cases accurately represent the user scenario, paying close attention to details in the scenario and screenshot.
    - Validate the response of each request with proper checks.
    - Include any necessary setup and teardown steps.
    - Write the full test case, avoiding placeholder comments.
    - Repeat elements as needed to match the user scenario.
    - Politely refuse to generate the test case if the user scenario does not match the given image.
    - Use dummy values for sensitive data such as PII, unless specific values are provided by the user.

    Start your test case with the following import statement: 
    `import { browser } from 'k6/experimental/browser';`
    
    To use the page instance in your test case, use the following code:
    `const page = browser.newPage();`

    Return only the full K6 browser test cases. Do not include any comments or markdown format like "```javascript". Include only the code.
    """

    USER_PROMPT = """
    Generate K6 test case for the following scenario: 
    """

    @staticmethod
    def prepare_prompt(image_data_url, test_scenario):
        
        return [
            {"role": "system", "content": TestCaseGeneratorPrompt.SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": TestCaseGeneratorPrompt.USER_PROMPT + test_scenario,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{image_data_url}", "detail": "high"},
                    },
                ],
            },
        ]
