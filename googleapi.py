import requests

def google_search(query, api_key, cse_id, **kwargs):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return response.json()

# Replace 'your_api_key_here' and 'your_cse_id_here' with your actual API key and Custom Search Engine ID
API_KEY = 'AIzaSyDBzd_IZnMZmG4HzzQbxTwPGB1bMMXWw9M' #google project test, if it is not needed, turn off the api in project "test"
CSE_ID = '91cf046415f154454'

if __name__ == '__main__':
    query = 'google sport result'
    results = google_search(query, API_KEY, CSE_ID, num=10)
    for item in results.get('items', []):
        print(f"Title: {item['title']}\nLink: {item['link']}\n")
