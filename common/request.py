import requests

class Request():
    def __init__(self,host,token):
        self.host=host
        self.token=token
    def get_token(self):
        print(self.token)



class Package(Request):
    def __init__(self,host,token):
        self.host=host
        self.token=token
    def get_token(self):
        print(self.token)


if __name__=="__main__":
    Package("hhj","jjj").get_token()

