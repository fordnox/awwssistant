import base64
import logging
from pathlib import Path

from openai import OpenAI

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# https://platform.openai.com/docs/guides/vision
class VisionAssistant:
    def __init__(self):
        self.client = OpenAI()

    @staticmethod
    def encode_image(image_path: Path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def get_article_from_image(self, image_path: Path):
        base64_image = self.encode_image(image_path)
        image_url = f"data:image/jpeg;base64,{base64_image}"
        prompt = """
            I will provide you an image that is a scan of the single magazine page. 
            Image contains multiple articles and images. 
            Extract text for each article.
            Return result as json string, do not add any additional comments and do 
            not add markdown formatting.
            """
        return self.describe_image_url(image_url, prompt)

    def describe_image(self, image_path: Path):
        base64_image = self.encode_image(image_path)
        image_url = f"data:image/jpeg;base64,{base64_image}"
        return self.describe_image_url(image_url)

    def describe_image_url(self, image_url, prompt="What’s in this image?"):
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
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
