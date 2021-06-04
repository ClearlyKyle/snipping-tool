import json
import urllib3


class AnkiConnect:
    def request(self, action, **params):
        return {'action': action, 'params': params, 'version': 6}

    def invoke(self, action, **params):
        http = urllib3.PoolManager()
        requestJson = json.dumps(self.request(action, **params)).encode('utf-8')
        try:
            response = http.request('POST', 'http://127.0.0.1:8765', body=requestJson)
            resp_dict = json.loads(response.data.decode('utf-8'))
            return resp_dict['result']

        except urllib3.exceptions.HTTPError as e:
            print('Request failed:', e)
            print("Make sure the Anki application is running and the \"Ankiconect\" pluging is installed")
            return

        if len(resp_dict) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in resp_dict:
            raise Exception('response is missing required error field')
        if 'result' not in resp_dict:
            raise Exception('response is missing required result field')
        if resp_dict['error'] is not None:
            raise Exception(resp_dict['error'])
        return resp_dict


#anki = AnkiConnect()
#modelNames = anki.invoke("modelNames")['result'][0]
#fieldNames = anki.invoke("modelFieldNames", modelName=modelNames)
#print(modelNames)
#print(fieldNames)
