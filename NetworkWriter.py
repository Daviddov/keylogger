from IWrite import IWrite
import requests
class NetworkWrite(IWrite):
    def Write(self,data):
        print("write to network")
        url = "https://httpbin.org/post"

        respones = requests.post(url,data)
        if respones.status_code == 200:
            print(respones.json())


if __name__ == '__main__':
    import json
    data = [["key","value"]]
    databyte = json.dumps(data).encode('utf-8')
    buffer = databyte.decode("utf-8")  # המרה למחרוזת
    nw = NetworkWrite()
    nw.Write(buffer)
