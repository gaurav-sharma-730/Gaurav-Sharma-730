import requests

# Fetch data from TryHackMe API
THM_PROFILE_URL = "https://tryhackme.com/api/v2/badges/public-profile?userPublicId=1855659"
response = requests.get(THM_PROFILE_URL)
data = response.json()

# Extract relevant data (e.g., badges)
badge_count = len(data['badges'])
badges = data['badges']

# Create content to be inserted in README
thm_stats = f"- [View My TryHackMe Profile](https://tryhackme.com/p/1855659)\n"
thm_stats += f"- Total Badges: {badge_count}\n\n"

for badge in badges:
    thm_stats += f"  - {badge['name']}: {badge['description']}\n"

# Read the existing README.md file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Replace the placeholder with the new content
start_marker = "<!-- TRYHACKME-STATS -->"
end_marker = "<!-- TRYHACKME-STATS-END -->"
updated_content = f"{start_marker}\n{thm_stats}\n{end_marker}"

# Replace the placeholder section in README.md
new_readme_content = readme_content.split(start_marker)[0] + updated_content + readme_content.split(end_marker)[1]

# Write the updated content back to README.md
with open('README.md', 'w') as file:
    file.write(new_readme_content)
