## pip install request
import requests

apiKey = 'k_r64d9its'

print("\nWELCOME TO MOVIE WARRIORS\nPlease select one of the following options\n")
option = input("\n1. Search film by keywords\n2. Search current films in theaters\n3. Find films comming soon\n")


def urls(api_ending, expre):
    if expre == null:
        url = f'https://imdb-api.com/en/API/{api_ending}/{apiKey}'
    else:
        url = f'https://imdb-api.com/en/API/{api_ending}/{apiKey}/{expression}'
    return url


""" Option 1 - API: search for expresions (keywords) and find movies
        https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}

        lang	Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
        apiKey	Required	API Key required for all API calls. Register on site to get free API Key.

"""

if option == "1":

    expression = input('Please, type the keyword for searching a movie: ') #'inception 2010'
    #url_params = dict(apiKey = v_apiKey, expression= v_expression)

    #####url = f'https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}'

    api_ = "SearchMovie"
    expr_ = expression


    #response = requests.get(url)
    response = requests.get(urls(api_, expr_))


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

"""API: find current movios in theaters:
        https://imdb-api.com/en/API/InTheaters/k_r64d9its
        
        lang	Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
        apiKey	Required	API Key required for all API calls. Register on site to get free API Key
"""

if option == "2":

    expression = input('Please, type the keyword for searching a movie: ') #'inception 2010'
    #url_params = dict(apiKey = v_apiKey, expression= v_expression)

    url = f'https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}'
    response = requests.get(url)

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

""""API: films comming soon
         https://imdb-api.com/en/API/ComingSoon/k_r64d9its   
         
         lang	Optional	Language of results. Default value is "en" (English). Language ch  ange is not important in this action.
         apiKey	Required	API Key required for all API calls. Register on site to get free API Key.
"""


