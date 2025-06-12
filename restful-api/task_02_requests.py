import requests
import csv

API_URL = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print
      status code and titles of each post.
    """
    try:
        response = requests.get(API_URL)
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return

    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    try:
        posts = response.json()
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return

    for post in posts:
        print(post.get('title'))


def fetch_and_save_posts(filename='posts.csv'):
    """
    Fetch posts from JSONPlaceholder and save
      id, title, and body to a CSV file.
    """
    try:
        response = requests.get(API_URL)
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return

    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    try:
        posts = response.json()
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return

    rows = [
        {
            'id': post.get('id'),
            'title': post.get('title'),
            'body': post.get('body')
        }
        for post in posts
    ]

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

        print(f"Saved {len(rows)} posts to '{filename}'")
    except (IOError, OSError) as e:
        print(f"Error writing to CSV file: {e}")
