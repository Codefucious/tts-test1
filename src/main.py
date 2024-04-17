import os
import json
import requests

headers = {
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY', ''),
    'Content-Type': 'application/json',
}

# API endpoint
url = 'https://api.openai.com/v1/audio/speech'

input = """ 

Call Center Costs are increasing drastically. Vodacom is loosing a billion dollars every day on customer care calls and now , 
because of the mini apps we're getting even more calls for third party related services.
We need to do something! Fast!

Now I know what your thinking , "don't we already have TOBi?". 
Yes , in fact TOBI's already contributing to a 10percent call reduction.
But TOBI desperatly needs a revamp . 
It has no idea how to sort out mini app related issues , and it isn't the most easy to talk to , its too... ROBOTIC.


"""


# Request body
data = {
    'model': 'tts-1-hd',
    'input': input,
    'voice': 'alloy'
}

# Sending the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Checking if the request was successful
if response.status_code == 200:
    # Saving the speech as an mp3 file
    with open('speech.mp3', 'wb') as f:
        f.write(response.content)
    print("Speech generated successfully and saved as 'speech.mp3'")
else:
    print(f"Error: {response.status_code} - {response.text}")