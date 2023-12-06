import time
import json
from pathlib import Path
import logging
from openai import OpenAI
import base64

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# https://platform.openai.com/docs/guides/vision
class VisionAssistant:

    def __init__(self):
        self.client = OpenAI()

    def describe_image(self, image_path: Path):
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        image_url = f"data:image/jpeg;base64,{base64_image}"
        return self.describe_image_url(image_url)

    def describe_image_url(self, image_url):
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What’s in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        logger.info(response)
        return response.choices[0].message.content