import requests
import json
import smtplib
import ssl
import os

def fetch_api_data(url):
    """Fetches data from a given API URL and returns it as JSON."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return None

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """Sends an email."""
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def format_size(size_bytes):
    """Formats file size in bytes to a human-readable format."""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    return f"{size_bytes:.2f} {units[i]}"

# Configuration
api_url_template = "https://apibay.org/q.php?q=(test_title)&cat="
test_title = "Test Show"
target_episode = "S01E01"
sender_email = "your_email@example.com"
receiver_email = "Test@gmail.com"
email_subject = f"New torrents for {test_title} found!"
last_notified_file = "last_notified.txt" # File to store the last notified episode

# Replace placeholder in URL
api_url = api_url_template.replace("(test_title)", test_title.replace(" ", "%20"))

data = fetch_api_data(api_url)

if data:
    matching_torrents = []

    for torrent in data:
        title = torrent.get("name")
        if title and target_episode in title:
            magnet_link = f"magnet:?xt=urn:btih:{torrent.get('info_hash')}&dn={title}"
            seeders = int(torrent.get('seeders', 0))
            size = int(torrent.get('size', 0))
            matching_torrents.append({
                'title': title,
                'magnet_link': magnet_link,
                'seeders': seeders,
                'size': size
            })

    if matching_torrents:
        # Sort by seeders (descending)
        matching_torrents.sort(key=lambda x: x['seeders'], reverse=True)

        email_body = f"The following torrents for '{test_title}' were found (sorted by seeders):\n\n"
        for torrent in matching_torrents:
            email_body += f"Title: {torrent['title']}\n"
            email_body += f"Size: {format_size(torrent['size'])}\n"
            email_body += f"Seeders: {torrent['seeders']}\n"
            email_body += f"Link: {torrent['magnet_link']}\n\n"

        sender_password = "your_app_password" # Use your App password here for automation
        send_email(sender_email, sender_password, receiver_email, email_subject, email_body)

        # Update the last notified file with the title of the top result, or handle this line however you'd like
        if matching_torrents:
            with open(last_notified_file, "w") as f:
                f.write(matching_torrents[0]['title'])
    else:
        print(f"No torrents for '{target_episode}' found for '{test_title}'.")
else:
    print(f"Failed to fetch or decode API data for '{test_title}'.")