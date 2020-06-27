import requests
import xmltodict

key = "r%2FZ30kTHVMm69k4TivRV63Rx55N5yNxYbYzeBeiPfAakUWiAlaxzgrMMaZSBQ3TikIBPw0bwxuhFwUsBXDtlTw%3D%3D"
url = "http://apis.data.go.kr/B551182/msupCmpnMeftInfoService/getMajorCmpnNmCdList?ServiceKey={}".format(key)

content = requests.get(url).content
dict_api = xmltodict.parse(content)
