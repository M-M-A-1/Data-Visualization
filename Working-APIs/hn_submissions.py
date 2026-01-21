from operator import itemgetter
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict.get("title"),
        "author": response_dict.get("by"),
        "score": response_dict.get("score"),
        "url": response_dict.get("url"),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("score"), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict["title"])
    print("Author:", submission_dict["author"])
    print("Score:", submission_dict["score"])
    print("URL:", submission_dict["url"])