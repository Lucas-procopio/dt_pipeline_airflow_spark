import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
def get_auth():
    return os.environ.get("BEARER_TOKEN")

def create_url():
    # Optional params: start_time, end_time, since_id, until_id, max_results, next_token,
    # expansions, tweet.fields, media.fields, poll.fields, place.fields, user.fields
    query_params = {'query': 'Flamengo', 'tweet.fields': 'author_id, conversation_id, created_at, id, in_reply_to_user_is, public_metrics, text'}
    user_fields = "expansions=author_id&user.fields=id,name,username,created_at"
    filters = "start_time=2023-11-09T00:00:00.00Z&end_time=2023-13-09T00:00:00.00Z"
    search_url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query_params["query"], query_params["tweet.fields"])

    return search_url

def bearer_oauth(r):
    "Method required by bearer token authentication."

    r.headers["Authorization"] = f"Bearer {get_auth()}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()