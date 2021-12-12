#TEIL 2: GUI

from tkinter import *
from tkinter import messagebox
import requests

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Movie Warriors!")
        self.switch(Menu)
        self.geometry('700x600')
        self.config(bg = "white")

    def switch(self, frame_class):
        """Destroys current frame and replaces it with a chosen by the user"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Menu(Frame):
    """Main menu"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "#95D1CC")

        """Frame widgets"""

        frame_label = Label(self, text = "\n\nSearch Movies!"
                      , bg = "#95D1CC", fg = "black", font=("Arial", 16))
        #frame_label.grid(column=0, row=0, padx=100)
        frame_label.pack()

        instruction_label = Label(self, text = "\nPlease, choose an option:"
                      , bg = "#95D1CC", fg = "black", font=("Arial", 13)).pack()

        button_keywords = Button(self, text = "Find movies by keywords", width = 40, font=("Arial", 11), command = lambda: master.switch(Movies_byKeywords))
        button_keywords.pack(padx = 30, pady = 8)

        button_inTheaters = Button(self, text = "Discover movies in theaters", width = 40, font=("Arial", 11), command = lambda: master.switch(Movies_inTheaters))
        button_inTheaters.pack(padx = 10, pady = 8)

        button_comingSoon = Button(self, text = "Be aware of movies coming soon", width = 40, font=("Arial", 11), command = lambda: master.switch(Movies_comingSoon))
        button_comingSoon.pack(padx = 10, pady = 8)

        button_exit = Button(self, text = "Exit", width = 20, font=("Arial", 11), command = self.close)
        button_exit.pack(padx = 10, pady = 30)

    def close(self):
        """Close the app"""
        self.destroy()
        exit()

class Movies_byKeywords(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "#95D1CC")

        def on_click():
            """API: search for expresions (keywords) and find movies
               https://imdb-api.com/en/API/SearchMovie/{apiKey}/{expression}
        
               lang	    Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
               apiKey	Required	API Key required for all API calls. Register on site to get free API Key.
            """

            # API connection
            apiKey = 'k_r64d9its'
            api = "SearchMovie"
            #expression = input('\nPlease, type the keyword for searching a movie: ')  # E.g. 'inception 2010'
            expression = entry_expression.get()
            url = f'https://imdb-api.com/en/API/{api}/{apiKey}/{expression}'
            response = requests.get(url)

            try:
                if response:
                    if response.status_code == 200:
                        # print(response.text)
                        json_response = response.json()

                        result = f"Search type: {json_response['searchType']}\n"
                        #result += f"Expression searched: {json_response['expression']}\n"
                        result += f"\nThere were {len(json_response['results'])} results found (scroll down to see more results):\n\n"

                        for tag in range(len(json_response['results'])):
                            result += f"{tag + 1}- Title: {json_response['results'][tag]['title']}\n"
                            result += f"   Description: {json_response['results'][tag]['description']}\n"
                            result += f"   Poster: {json_response['results'][tag]['image']}\n\n"

                        box_output.delete(0.0, END)
                        box_output.insert(END, result)
                        print(json_response['errorMessage'])
                    else:
                        response.reason
                else:
                    print('Events Response Failed')
                    print(response.content)
            except Exception as e:
                print(e)
                error_label = Label(self, text=f"There was an error by trying to connect the API:\n{json_response['errorMessage']}"
                                    , bg="#95D1CC", fg="black")
                error_label.pack()

        """Frame widgets"""
        frame_label = Label(self, text="\n\nFind movies by keywords", bg="#95D1CC", fg="black", font=("Arial", 13))
        frame_label.pack()

        # user input
        label_expression = Label(self, text="\nPlease enter an expression or keyword: ", bg="#95D1CC", fg="black", font=("Arial", 11))
        label_expression.pack()
        entry_expression = Entry(self, width=30, bg="white", font=("Arial", 11))
        entry_expression.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 11), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 11))
        label_output.pack()
        box_output = Text(self, width=80, height=20, wrap=WORD, bg="white", font=("Arial", 11))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)


class Movies_inTheaters(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#95D1CC")

        def on_click():
            """API: find current movios in theaters:
               https://imdb-api.com/en/API/InTheaters/k_r64d9its

               lang     Optional	Language of results. Default value is "en" (English). Language change is not important in this action.
               apiKey	Required	API Key required for all API calls. Register on site to get free API Key
            """

            # API connection
            apiKey = 'k_r64d9its'
            api = "InTheaters"
            url = f'https://imdb-api.com/en/API/{api}/{apiKey}'
            response = requests.get(url)

            try:

                if response:
                    if response.status_code == 200:
                        json_response = response.json()

                        result = f"\nThere were {len(json_response['items'])} results found (scroll down to see more results):\n\n"

                        for tag in range(len(json_response['items'])):
                            result += f"{tag + 1}- Title: {json_response['items'][tag]['fullTitle']}\n"
                            result += f"   Genre: {json_response['items'][tag]['genres']}\n"
                            result += f"   Stars: {json_response['items'][tag]['stars']}\n"
                            result += f"   Directors: {json_response['items'][tag]['directors']}\n"
                            result += f"   Release: {json_response['items'][tag]['releaseState']}\n"
                            result += f"   Duration: {json_response['items'][tag]['runtimeStr']}\n"
                            result += f"   Plot: {json_response['items'][tag]['plot']}\n"
                            result += f"   Image: {json_response['items'][tag]['image']}\n\n"

                        box_output.delete(0.0, END)
                        box_output.insert(END, result)
                        print(json_response['errorMessage'])
                    else:
                        response.reason
                else:
                    print('Events Response Failed')
                    print(response.content)
            except Exception as e:
                print(e)
                error_label = Label(self,
                                text=f"There was an error by trying to connect the API:\n{json_response['errorMessage']}"
                                , bg="#95D1CC", fg="black")
                error_label.pack()

        """Frame widgets"""
        frame_label = Label(self, text="\n\nDiscover movies in theaters", bg="#95D1CC", fg="black", font=("Arial", 13))
        frame_label.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 11), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 11))
        label_output.pack()
        box_output = Text(self, width=80, height=20, wrap=WORD, bg="white", font=("Arial", 11))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, font=("Arial", 11), command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)

class Movies_comingSoon(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#95D1CC")

        def on_click():
            """"API: films coming soon
                https://imdb-api.com/en/API/ComingSoon/k_r64d9its

                lang	Optional	Language of results. Default value is "en" (English). Language ch  ange is not important in this action.
                apiKey	Required	API Key required for all API calls. Register on site to get free API Key.
            """

            # API connection
            apiKey = 'k_r64d9its'
            api = "ComingSoon"
            url = f'https://imdb-api.com/en/API/{api}/{apiKey}'
            response = requests.get(url)

            try:
                if response:
                    if response.status_code == 200:
                        # print(response.text)
                        json_response = response.json()
                        # print(json_response)

                        result = f"\nThere were {len(json_response['items'])} results found (scroll down to see more results):\n\n"

                        for tag in range(len(json_response['items'])):
                            result += f"{tag + 1}- Title: {json_response['items'][tag]['fullTitle']}\n"
                            result += f"   Genre: {json_response['items'][tag]['genres']}\n"
                            result += f"   Stars: {json_response['items'][tag]['stars']}\n"
                            result += f"   Directors: {json_response['items'][tag]['directors']}\n"
                            result += f"   Release: {json_response['items'][tag]['releaseState']}\n"
                            result += f"   Duration: {json_response['items'][tag]['runtimeStr']}\n"
                            result += f"   Plot: {json_response['items'][tag]['plot']}\n"
                            result += f"   Image: {json_response['items'][tag]['image']}\n\n"

                        box_output.delete(0.0, END)
                        box_output.insert(END, result)
                        print(json_response['errorMessage'])
                    else:
                        response.reason
                else:
                    print('Events Response Failed')
                    print(response.content)

            except Exception as e:
                print(e)

        """Frame widgets"""
        frame_label = Label(self, text="\n\nBe aware of movies coming soon", bg="#95D1CC", fg="black", font=("Arial", 13))
        frame_label.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 11), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 11))
        label_output.pack()
        box_output = Text(self, width=80, height=20, wrap=WORD, bg="white", font=("Arial", 11))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, font=("Arial", 11), command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
