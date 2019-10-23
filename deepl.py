from requests_html import HTMLSession


class Config:
    url_endpoint = "https://www.deepl.com/en/translator"
    delay = 3


class DeepL:
    def __init__(self):
        self.session = HTMLSession()

    def translate(self, text, dest="en", src="en"):
        request = self.session.get(f"{Config.url_endpoint}#{src}/{dest}/{text}")
        request.html.render(sleep=Config.delay)
        elements = request.html.find("button.lmt__translations_as_text__text_btn")
        return [element.text for element in elements]
