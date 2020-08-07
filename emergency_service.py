import pandas as pd
import requests
import json

# This REST API was created in AIClub Navigator
# You can interact with it here as well: https://aiclub.world/projects/32e764d4-0b61-4c36-bce9-2cb85903cc33?tab=service
def get_prediction(data):
  url = 'https://4srz4f0vc4.execute-api.us-east-1.amazonaws.com/Predict/cc496ecb-0fca-4e5d-9240-7c344ea4f1f9'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response

prediction = json.loads(json.loads(get_prediction())['body'])['predicted_label']
print('The AI predicted: ', prediction)
print('new change')
