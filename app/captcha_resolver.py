from loguru import logger
from app.settings import CAPTCHA_RESOLVER_API_KEY, CAPTCHA_RESOLVER_API_URL
import requests


class CaptchaResolver(object):

    def __init__(self, api_url=CAPTCHA_RESOLVER_API_URL, api_key=CAPTCHA_RESOLVER_API_KEY):
        self.api_url = api_url
        self.api_key = api_key

    def create_task(self, image_base64_string, question_id):
        logger.debug(f'start to recognize image for question {question_id}')
        data = {
            "clientKey": self.api_key,
            "task": {
                "type": "ReCaptchaV2Classification",
                "image": image_base64_string,
                "question": question_id,
                "softID": 78
            }
        }
        try:
            response = requests.post(self.api_url, json=data)
            result = response.json()
            logger.debug(f'captcha recogize result {result}')
            return result
        except requests.RequestException:
            logger.exception(
                'error occurred while recognizing captcha', exc_info=True)

    def create_ocr_task(self, image_base64_string):
        logger.debug('start to recognize image for ocr')
        data = {
            "clientKey": self.api_key,
            "task": {
                "type": "ImageToTextTaskTest",
                "body": image_base64_string,
            }
        }
        try:
            response = requests.post(self.api_url, json=data)
            result = response.json()
            logger.debug(f'captcha recogize result {result}')
            return result
        except requests.RequestException:
            logger.exception(
                'error occurred while recognizing captcha ocr ', exc_info=True)
