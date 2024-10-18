import requests
import json

# Replace with your TryHackMe public ID
tryhackme_public_id = '1855659'

# Fetch TryHackMe profile data
url = f'https://tryhackme.com/api/v2/badges/public-profile?userPublicId={tryhackme_public_id}'
response = requests.get(url)

if response.status_code == 200:
    badge_data = response.json()

    # You can extract specific details like badges or stats from the API response
    total_badges = len(badge_data['badges'])
    profile_url = f'https://tryhackme.com/p/{tryhackme_public_id}'

    # Update README.md file
    with open("README.md", "w") as file:
        file.write("# Gaurav Sharma's GitHub Profile\n\n")
        file.write("## TryHackMe Profile Stats\n")
        file.write(f"- [View My TryHackMe Profile]({profile_url})\n")
        file.write(f"- Total Badges: {total_badges}\n")
        for badge in badge_data['badges']:
            file.write(f"  - {badge['name']}: {badge['description']}\n")
else:
    print(f"Failed to fetch TryHackMe data: {response.status_code}")
