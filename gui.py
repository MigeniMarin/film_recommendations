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
        self.config(bg='#FFFCDC')

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
        self.config(bg="#95D1CC")

        """Frame widgets"""

        frame_label = Label(self, text="\n\nSearch Movies!",
                            bg="#95D1CC", fg="black", font=("Arial", 18))
        frame_label.pack()

        instruction_label = Label(self, text="\nPlease, choose an option:",
                                  bg="#95D1CC", fg="black", font=("Arial", 15))
        instruction_label.pack()

        button_keywords = Button(self, text="Find movies by keywords", width=40, font=("Arial", 13),
                                 command=lambda: master.switch(MoviesByKeywords))
        button_keywords.pack(padx=30, pady=8)

        button_in_theaters = Button(self, text="Discover movies in theaters", width=40, font=("Arial", 13),
                                    command=lambda: master.switch(MoviesInTheaters))
        button_in_theaters.pack(padx=10, pady=8)

        button_coming_soon = Button(self, text="Get excited of coming movies", width=40, font=("Arial", 13),
                                    command=lambda: master.switch(MoviesComingSoon))
        button_coming_soon.pack(padx=10, pady=8)

        button_exit = Button(self, text="Exit", width=20, font=("Arial", 13), command=self.close)
        button_exit.pack(padx=10, pady=30)

    def close(self):
        """Close the app"""
        self.destroy()
        exit()


class MoviesByKeywords(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#95D1CC")

        def on_click():
            """API: search for expressions (keywords) and find movies
               https://imdb-api.com/en/API/SearchMovie/{api_key}/{expression}
        
               lang	    Optional	Language of results. Default value is "en" (English). Language is here not necessary.
               api_key	Required	API Key required for all API calls. Register on site to get free API Key.
            """

            # API connection
            api_key = 'k_r64d9its'
            api = "SearchMovie"
            expression = entry_expression.get()
            url = f'https://imdb-api.com/en/API/{api}/{api_key}/{expression}'
            response = requests.get(url)

            try:
                if response:
                    if response.status_code == 200:
                        # print(response.text)
                        json_response = response.json()

                        result = f"Search type: {json_response['searchType']}\n"
                        result += f"\nThere were {len(json_response['results'])} results found " \
                                  f"(scroll down to see more results):\n\n"

                        for tag in range(len(json_response['results'])):
                            result += f"{tag + 1}- Title: {json_response['results'][tag]['title']}\n"
                            result += f"   Description: {json_response['results'][tag]['description']}\n"
                            result += f"   Poster: {json_response['results'][tag]['image']}\n\n"

                        box_output.delete(0.0, END)
                        box_output.insert(END, result)
                        print(json_response['errorMessage'])
                else:
                    print('Events Response Failed')
                    print(response.content)
            except Exception as e:
                print(e)
                error_label = Label(self, text=f"There was an error by trying to connect the API:\n"
                                    f"{json_response['errorMessage']}", bg="#95D1CC", fg="black")
                error_label.pack()

        """Frame widgets"""
        frame_label = Label(self, text="\n\nFind movies by keywords", bg="#95D1CC", fg="black", font=("Arial", 15))
        frame_label.pack()

        # user input
        label_expression = Label(self, text="\nPlease enter an expression or keyword: ", bg="#95D1CC", fg="black",
                                 font=("Arial", 13))
        label_expression.pack()
        entry_expression = Entry(self, width=30, bg="white", font=("Arial", 13))
        entry_expression.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 13), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 13))
        label_output.pack()
        box_output = Text(self, width=70, height=16, wrap=WORD, bg="white", font=("Arial", 13))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, font=("Arial", 13), command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)


class MoviesInTheaters(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#95D1CC")

        def on_click():
            """API: find current movies in theaters:
               https://imdb-api.com/en/API/InTheaters/k_r64d9its

               lang     Optional	Language of results. Default value is "en" (English).
               api_key	Required	API Key required for all API calls. Register on site to get free API Key
            """

            # API connection
            api_key = 'k_r64d9its'
            api = "InTheaters"
            url = f'https://imdb-api.com/en/API/{api}/{api_key}'
            response = requests.get(url)

            try:

                if response:
                    if response.status_code == 200:
                        json_response = response.json()

                        result = f"\nThere were {len(json_response['items'])} results found " \
                                 f"(scroll down to see more results):\n\n"

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
                    print('Events Response Failed')
                    print(response.content)
            except Exception as e:
                print(e)
                error_label = Label(self,
                                    text=f"There was an error by trying to connect the API:\n"
                                    f"{json_response['errorMessage']}", bg="#95D1CC", fg="black")
                error_label.pack()

        """Frame widgets"""
        frame_label = Label(self, text="\n\nDiscover movies in theaters", bg="#95D1CC", fg="black", font=("Arial", 15))
        frame_label.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 13), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 13))
        label_output.pack()
        box_output = Text(self, width=70, height=16, wrap=WORD, bg="white", font=("Arial", 13))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, font=("Arial", 13), command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)


class MoviesComingSoon(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#95D1CC")

        def on_click():
            """"API: films coming soon
                https://imdb-api.com/en/API/ComingSoon/k_r64d9its

                lang	Optional	Language of results. Default value is "en" (English).
                api_key	Required	API Key required for all API calls. Register on site to get free API Key.
            """

            # API connection
            api_key = 'k_r64d9its'
            api = "ComingSoon"
            url = f'https://imdb-api.com/en/API/{api}/{api_key}'
            response = requests.get(url)

            try:
                if response:
                    if response.status_code == 200:
                        # print(response.text)
                        json_response = response.json()
                        # print(json_response)

                        result = f"\nThere were {len(json_response['items'])} results found " \
                                 f"(scroll down to see more results):\n\n"

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
                    print('Events Response Failed')
                    print(response.content)

            except Exception as e:
                print(e)

        """Frame widgets"""
        frame_label = Label(self, text="\n\nGet excited of coming movies", bg="#95D1CC", fg="black",
                            font=("Arial", 15))
        frame_label.pack()

        # search
        submit_search = Button(self, text="Search", width=8, font=("Arial", 13), command=on_click)
        submit_search.pack(padx=10, pady=10)

        # output
        label_output = Label(self, text="These are the results:", bg="#95D1CC", fg="black", font=("Arial", 13))
        label_output.pack()
        box_output = Text(self, width=70, height=16, wrap=WORD, bg="white", font=("Arial", 13))
        box_output.pack()

        # going back to menu
        self.button_back = Button(self, text="Back", width=8, font=("Arial", 13), command=lambda: master.switch(Menu))
        self.button_back.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
