import urllib.parse
import requests
import pprint
import sys
HOST = "login.eagleeyenetworks.com"

#Full disclosure: I picked this file from https://github.com/alzerid/een-python-lib and just modified it to do what I needed

def login(username, password, realm="eagleeyenetworks"):
	url  = "https://%s/g/aaa/authenticate" % HOST
	body = "username=%s&password=%s&realm=%s" % (username, password, realm)
	resp = requests.post(url, data=body)
	resp = resp.json()

	if 'token' not in resp:
		raise Exception("Token not defined")
	
	#authorize
	token = resp['token']
	url   = "https://%s/g/aaa/authorize" % HOST
	resp  = requests.post(url, data=urllib.parse.urlencode(resp))
	user  = resp.json()

	return EENContext(user, token, resp.cookies)

def timestamp(ts):
	return ts

class EENContext:
	def __init__(self, user, token, cookies):
		self._token   = token
		self._user    = user
		self._cookies = cookies

	def camera_list(self, esn="", name="", device_type="", status=""):
		req = requests.get("https://%s/g/device/list?e=%s;n=%s;t=%s;s=%s" % (HOST, esn, name, device_type, status), cookies=self._cookies)
		return req.json()
	
	def image_list(self, esn, count, asset_type="preview", time="now"):
		req = requests.get("https://%s/asset/list/image.jpeg?c=%s;t=%s;a=%s;count=%d" % (HOST, esn, time, asset_type, count), cookies=self._cookies)
		return req.json()
	
	def fetch_image(self, esn, time, quality="med", asset_type="preview"):
		req = requests.get("https://%s/asset/asset/image.jpeg?c=%s;t=%s;a=%s;q=%s" % (HOST, esn, time, asset_type, quality), cookies=self._cookies)
		return req.content

	def logout(self):
		requests.get("https://%s/g/aaa/logout" % HOST, cookies=self._cookies)
