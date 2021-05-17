import json
import urllib.request

class AnkiConnect:
	def request(self, action, **params):
		return {'action': action, 'params': params, 'version': 6}


	def invoke(self, action, **params):
		requestJson = json.dumps(self.request(action, **params)).encode('utf-8')
		try:
			response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
		except urllib.error.URLError:
			print("Error! Make sure the Anki application is running and the \"Ankiconect\" pluging is installed")

			if len(response) != 2:
				raise Exception('response has an unexpected number of fields')
			if 'error' not in response:
				raise Exception('response is missing required error field')
			if 'result' not in response:
				raise Exception('response is missing required result field')
			if response['error'] is not None:
				raise Exception(response['error'])
			return response['result']

anki = AnkiConnect()
result = anki.invoke('deckNames')
print(result)
