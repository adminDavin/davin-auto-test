import requests
import json
class Runmethod():
    def post_main(self,url,data,header=None):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,headers=header).json()
        else:
            res=requests.post(url=url,data=data).json()
            print(res.status_code)
        return res.json

    def get_main(self,url,data=None,header=None):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,headers=header).json()
        else:
            res=requests.post(url=url,data=data).json()
        return res.text
    def run_main(self,method,url,data=None,header=None):
        res=None
        if method=="post_main":
            res=self.post_main(url,data,header)
        else:
            res=self.get_main(url,data,header)

        return json.dumps(res,ensure_ascill=False,sort_key=True,indent=2)




