## pip install request
import requests

apiKey = 'k_r64d9its'
expression = input('Please, type the key word for searching a movie: ') #'inception 2010'

#url_params = dict(apiKey = v_apiKey, expression= v_expression)

url = f'https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}'
response = requests.get(url) #, params=url_params)

if response:
    if response.status_code == 200:
        #print(response.text)
        json_response = response.json()
        print(f"Search type:                   {json_response['searchType']}")
        print(f"Expression searched:           {json_response['expression']}")

        print(f"\nThere were {len(json_response['results'])} results found:\n")

        for tag in range(len(json_response['results'])):
            print(f"{tag + 1}- Title:       {json_response['results'][tag]['title']}")
            print(f"           Description: {json_response['results'][tag]['description']}")
            print(f"           Poster:      {json_response['results'][tag]['image']}")

        print(json_response['errorMessage'])
    else:
        response.reason