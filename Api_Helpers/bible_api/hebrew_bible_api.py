import requests
import qrng

base_url = "http://www.sefaria.org/api"
payload = {}
headers = {}


def get_all_books():
    url = base_url + "/index/"
    # url = base_url + "/index/:title"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).json()
    return response


def get_book_meta(book):
    url = f"{base_url}/v2/raw/index/{book}"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).json()

    book_meta_data = {
        "book_name": book,
        "chapeters": response["schema"]["lengths"][0],
        "verses": response["schema"]["lengths"][1],
    }
    return book_meta_data


def open_book():
    url = "https://www.sefaria.org/api/texts/Genesis.2"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).json()
    # take verse and convert to list
    random_verse = qrng(len(response["he"]))
    verse_list = response["he"][random_verse].split()
    return response


def get_all_tanakh_books():
    Tanakh_books = []
    Tanakh_books_list = get_all_books()[0]["contents"]  # return the Tanakh
    for i in range(len(Tanakh_books_list)):
        book_dict = {
            "heb_name": Tanakh_books_list[i]["heCategory"],
            "eng_name": Tanakh_books_list[i]["category"],
        }
        # book_name = Tanakh_books_list[i]['category']
        Tanakh_books.append(book_dict)
    return Tanakh_books


def get_specific_verse(book, chapter=None, start_verse=None, end_verse=None):
    # build the correct url based on the optional args
    default_url = f"{base_url}/texts/{book}"

    if chapter is not None:
        default_url += f".{chapter}"
    if start_verse is not None:
        default_url += f".{start_verse}"
    if end_verse is not None:
        default_url += f"-{end_verse}"
    url = default_url

    payload = {"context": 0}
    print(url)
    response = requests.get(url, params=payload).json()
    if "error" in response:
        raise ValueError(f'\n{url} invalid. \n{response["error"]}\nExit..')
    else:
        # create a dictionary of Lists
        verses_dict = {}
        heb_verses = response["he"]
        current_verse = int(start_verse)
        for verse in heb_verses:
            verses_dict[f"verse_{current_verse}"] = verse.split()
            current_verse += 1
        print(verses_dict)
        # NOTE 26.11.2022 - create sacred_object with each word and its fibonacci/369 num
        # TODO 26.11.2022 - apply to both each word and verse (pasuk)
        # TODO 26.11.2022 - apply gematria on each word/verse and add to the sacred_object

    # Example for fetch a specific Verse: https://www.sefaria.org/api/texts/Jeremiah.23.24?context=0
    # Example for fetch range of Verses: https://www.sefaria.org/api/texts/Jeremiah.23.24-25?context=0


if __name__ == "__main__":

    # books_list = get_all_tanakh_books()
    # book = "bereshit"
    # get_book_data = get_book_meta(book)
    # open_book()
    book = "Sefer_Yetzirah"  # "Jeremiah"
    # book_number = "1"  # None
    chapter = "1"
    start_verse = "1"
    end_verse = "2"
    get_specific_verse(book, chapter, start_verse, end_verse)
