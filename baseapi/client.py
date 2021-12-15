from common import utils


class HttpClient():

    def __init__(self):
        self.env=utils.get_dafalut_environment()

        self.headers = { 'Content-Type': 'application/json'}

