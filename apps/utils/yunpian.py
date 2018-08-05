# coding:utf-8
# Author:Nan ji dong

import requests


class YunPian(object):

    def __init__(self):
        self.api_key = api_key
        self.single_send_url = ""

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": ""
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        print(re_dict)


if __name__ == "__main__":
    yun_pian = YunPian("")
    yun_pian.send_sms("2018", "13201917726")
