from dotenv import load_dotenv
from src.ui.gradio_ui import GradioUI

# Launch the Gradio UI

if __name__ == "__main__":
    # Take environment variables from .env.
    load_dotenv()
    ui = GradioUI()
    ui.launch_ui()
