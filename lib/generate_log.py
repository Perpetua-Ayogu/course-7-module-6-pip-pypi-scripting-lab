from datetime import datetime
import requests

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as error:
        print(f"Could not fetch post: {error}")
        return {}


def main():
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)
    generate_log([f"Fetched Post Title: {title}"])


if __name__ == "__main__":
    main()
