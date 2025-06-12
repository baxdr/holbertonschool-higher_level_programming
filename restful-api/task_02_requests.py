import requests
import csv

API_URL = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints
      status code and titles of each post.
    """
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return

    posts = response.json()
    for post in posts:
        print(post.get('title'))


def fetch_and_save_posts(filename='posts.csv'):
    """
    Fetches posts from JSONPlaceholder and saves
      id, title, and body into a CSV file.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return

    posts = response.json()
    # Prepare data for CSV
    rows = [{'id': post['id'],
             'title': post['title'],
             'body': post['body']}
            for post in posts]

    # Write to CSV
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)
        print(f"Saved {len(rows)} posts to '{filename}'")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
