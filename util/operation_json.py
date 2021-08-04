import json
class OperetionJson:
    def __init__(self):
        self.data=self.read_data()

    def read_data(self):
        with open("../util/new1.json") as fp:
            data=json.load(fp)
            return data
    def get_data(self,id):
        print(self.data)
        return self.data['login']


if __name__ == '__main__':
    opjson=OperetionJson()
    # print(opjson.get_data("login"))
