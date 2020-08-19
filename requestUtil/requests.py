import requests

class RequestUtil(object):
    def DoGet(self, url, params, header=None):
        result = None
        if header == None:
            result = requests.get(url, params=params).json()
        else:
            result = requests.get(url, headers=header, params=params).json()
        return result

    def DoPost(self, url, data, header=None):
        result = None
        if header == None:
            result = requests.post(url, data=data).json()
        else:
            result = requests.post(url, data=data, header=header).json()
        return result

    def DoRequest(self, method, url, data, header):
        if method == "GET":
           return  self.DoGet(url, data, header)
        elif method == "POST":
           return  self.DoPost(url, params=data, header=header)
        else:
            raise Exception("No Method")
