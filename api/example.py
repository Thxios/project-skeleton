
from api.base import HaiAPI
from PIL import Image, ImageDraw, ImageFont



class ExampleAPI(HaiAPI):
    def __init__(self, font='malgun.ttf'):
        self.font = ImageFont.truetype(font, size=20)

    def query_image2text(self, image: Image.Image, **kwargs):
        image_info = f'Resolution: {image.size}, InfoDict: {image.info}'
        return image_info

    def query_image2image(self, image: Image.Image, **kwargs):
        image_grayscale = image.convert('L')
        return image_grayscale

    def query_text2text(self, text: str, **kwargs):
        return text + '\nHAI is the best!!'

    def query_text2image(
            self,
            text: str,
            size=(800, 600),
            position=(50, 50),
            bg_color=(0, 0, 0)
    ):
        image = Image.new(mode='RGB', size=size, color=bg_color)
        img_draw = ImageDraw.Draw(image)

        img_draw.text(xy=position, text=text, font=self.font)
        return image


