import pandas as pd
import requests
import json

def get_prediction(data):
  url = 'https://4srz4f0vc4.execute-api.us-east-1.amazonaws.com/Predict/cc496ecb-0fca-4e5d-9240-7c344ea4f1f9'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response

prediction = json.loads(json.loads(get_prediction())['body'])['predicted_label']
print('The AI predicted: ', prediction)
print('new change')
