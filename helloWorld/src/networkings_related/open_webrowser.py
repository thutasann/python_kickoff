import webbrowser


def open_webrowser(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


query = input("Search Google...")
open_webrowser(query)
