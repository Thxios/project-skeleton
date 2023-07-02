
import abc
from PIL import Image


class HaiAPI(abc.ABC):

    @abc.abstractmethod
    def query_image2text(self, image: Image.Image, **kwargs):
        pass

    @abc.abstractmethod
    def query_image2image(self, image: Image.Image, **kwargs):
        pass

    @abc.abstractmethod
    def query_text2text(self, text: str, **kwargs):
        pass

    @abc.abstractmethod
    def query_text2image(self, text: str, **kwargs):
        pass




