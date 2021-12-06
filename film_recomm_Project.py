## pip install request
from datetime import datetime, date, time
import requests

current_time = datetime.now()
print(f"\nStart time: {current_time}")
#print(current_time.time())
#print(current_time.date())

apiKey = 'k_r64d9its'

print("\n**************************************************************\n"
      "                   WELCOME TO MOVIE WARRIORS\n"
      "**************************************************************")

def urls(api_ending, expre=None):
    if expre is None:
        url = f'https://imdb-api.com/en/API/{api_ending}/{apiKey}'
    else:
        url = f'https://imdb-api.com/en/API/{api_ending}/{apiKey}/{expression}'
    return url

show_menu = "y"

while show_menu == "y":

    print("\nPlease enter the number of the desired option:\n")
    option = input("\n1. Search film by keywords\n2. Search current films in theaters\n3. Find films comming soon\n4. Exit\n")

    if option == "1":
        """Option 1 - API: search for expresions (keywords) and find movies
                    https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}

                    lang	Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
                    apiKey	Required	API Key required for all API calls. Register on site to get free API Key.
        """

        expression = input('\nPlease, type the keyword for searching a movie: ') #'inception 2010'
        #url_params = dict(apiKey = v_apiKey, expression= v_expression)

        api_ = "SearchMovie"
        expr_ = expression

        current_time = datetime.now()

        # url = f'https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}'
        # response = requests.get(url)
        response = requests.get(urls(api_, expr_))

        try:
            if response:
                if response.status_code == 200:
                    # print(response.text)
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

            else:
                print('Events Response Failed')
                print(response.content)

        except Exception as e:
            print(e)

        time_opt = datetime.now()
        print(f"Response time: {time_opt - current_time} sec.")

        show_menu = input("\nDo you want to continue (y/n)?: ")

    elif option == "2":
        """Option 2 - API: find current movios in theaters:
                https://imdb-api.com/en/API/InTheaters/k_r64d9its

                lang	Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
                apiKey	Required	API Key required for all API calls. Register on site to get free API Key
        """

        print('\nMovies in theaters:')

        api_ = "InTheaters"

        current_time = datetime.now()

        response = requests.get(urls(api_))

        try:
            if response:
                if response.status_code == 200:
                    #print(response.text)
                    json_response = response.json()
                    print(json_response)

                    print(f"\nThere were {len(json_response['items'])} results found:\n")

                    for tag in range(len(json_response['items'])):
                        print(f"{tag + 1}- Title:       {json_response['items'][tag]['fullTitle']}")
                        print(f"           Genre:       {json_response['items'][tag]['genres']}")
                        print(f"           Stars:       {json_response['items'][tag]['stars']}")
                        print(f"           Directors:   {json_response['items'][tag]['directors']}")
                        print(f"           Release:     {json_response['items'][tag]['releaseState']}")
                        print(f"           Duration:    {json_response['items'][tag]['runtimeStr']}")
                        print(f"           Plot:        {json_response['items'][tag]['plot']}")
                        print(f"           Image:       {json_response['items'][tag]['image']}\n")
                    print(json_response['errorMessage'])
                else:
                    response.reason
            else:
                print('Events Response Failed')
                print(response.content)

        except Exception as e:
            print(e)

        time_opt = datetime.now()
        print(f"Response time: {time_opt - current_time} sec.")

        show_menu = input("\nDo you want to continue (y/n)?: ")

    # option 3 needs to be adapted to the api:
    elif option == "3":
        """"Option 3 - API: films comming soon
                 https://imdb-api.com/en/API/ComingSoon/k_r64d9its   

                 lang	Optional	Language of results. Default value is "en" (English). Language ch  ange is not important in this action.
                 apiKey	Required	API Key required for all API calls. Register on site to get free API Key.
        """

        print('\nMovies in theaters:')

        api_ = "InTheaters"

        current_time = datetime.now()

        response = requests.get(urls(api_))

        try:
            if response:
                if response.status_code == 200:
                    #print(response.text)
                    json_response = response.json()
                    print(json_response)

                    print(f"\nThere were {len(json_response['items'])} results found:\n")

                    for tag in range(len(json_response['items'])):
                        print(f"{tag + 1}- Title:       {json_response['items'][tag]['fullTitle']}")
                        print(f"           Genre:       {json_response['items'][tag]['genres']}")
                        print(f"           Stars:       {json_response['items'][tag]['stars']}")
                        print(f"           Directors:   {json_response['items'][tag]['directors']}")
                        print(f"           Release:     {json_response['items'][tag]['releaseState']}")
                        print(f"           Duration:    {json_response['items'][tag]['runtimeStr']}")
                        print(f"           Plot:        {json_response['items'][tag]['plot']}")
                        print(f"           Image:       {json_response['items'][tag]['image']}\n")
                    print(json_response['errorMessage'])
                else:
                    response.reason

            show_menu = input("Do you want to continue (y/n)?: ")

        except Exception as e:
            print(e)

        time_opt = datetime.now()
        print(f"Response time: {time_opt - current_time} sec.")

        show_menu = input("\nDo you want to continue (y/n)?: ")

    elif option == "4":
        """Option 4 - Exit from the app"""

        show_menu = "n"

current_time = datetime.now()
print(f"\nEnd time: {current_time}")
print("\nThanks for visiting us!")