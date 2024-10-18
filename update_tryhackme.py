import requests
import json

# Define the URL for the image regeneration
url = "https://tryhackme.com/api/v2/badges/public-profile/image"

# Set the headers required for the request
headers = {
    "Host": "tryhackme.com",
    "Cookie": "AWSALB=BYST0GYTcflCLdiXy7qMa3RPM0PMvlL55ps6Py7mLsBFKF7RzbGD9y1hCV3AZgSsjKjY1dbUiWQNKSyxfRVzKr6KfrgvmxAAVOE03M+0WzQ0iVBlHyJ3mUtwpb0a; _csrf=R7s_yF-VAPs5cHFxEYWZNI6g; AMP_d09a34bd2d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIxNGYzMTUzZi1lYWZlLTQ4ZGItYmRjOS00MDFkOGEwNDU1MTklMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDMxNWUyMzQ4NzNjYTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG7uSWQlMjIlM0ExNzI5MjI3OTE2Mjk0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG7hc3RFdmVudElkJTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG7yJTNBMCU3RA==; _hjSessionUser_1950941=eyJpZCI6Ijk3OTUxZTA0LTY5MmUtNWZhYy05NTFmLTJjN2JjNzA2MGVjZiIsImNyZWF0ZWQiOjE3MjkyMjc5MTY1NjcsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1950941=eyJpZCI6ImViZDM3MzQ0LTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG7hMSIsImMiOjE3MjkyMjc5MTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG7zciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _cioanonid=2471bf51-6427-c220-02de-d0056ae4643f; _ga_Z8D4WL3D4P=GS1.1.1729227918.1.1.1729228779.41.0.0; _ga=GA1.1.868122149.1729227919; __hstc=256179476.592b28bbf4608e8adff13a17d293d0c9.1729227920095.1729227920095.1729227920095.1; hubspotutk=592b28bbf4608e8adff13a17d293d0c9; __hssrc=1; __hssc=256179476.6.1729227920096; intercom-device-id-pgpbhph6=44341883-b0d9-45a1-bd83-793034753916; connect.sid=s%3AiYejjRw--6Z0q__3cEGN9l9T6A9-cJoZ.8QD0hlnmHQvHsB6t6nJynbYh90zscYiZvnfoiWNIlNA; logged-in-hint=64315e234873ca004b868bc4; _cioid=gauravjangid7300@gmail.com; _hjHasCachedUserAttributes=true; cookieconsent_status=dismiss; cf_clearance=bcHybu0NU0_Y1fKiXSLWT_n51X53pRwmRcwolicPgmc-1729228765-1.2.1.1-jqqAHz7sgcSPmzCb.RvJ.qPhLah7v348D.VJu3YwakGXMQvDYXVnXyHMr4vOnIxH0aKcEZOqVpiQslDTDquzXjUmH4iRh5CdEhOgw50kQLpuxpJoLEYqp32t7Azd90.B5FZbClJ3h3nZPpe4sF788iMIE0VLhPsfuGpwTJe4AfYpYh8ziNJ5jkfdWuP_RdBJ8RJbgS43cvL8yQTkzUR2zoUYrZfRcmLMNAgFzCTU_sdxCvDjxeSYTd1Vft61m0GBIc7ZYuskxHgqVCg52B8cdnhsIk0k96rxQ_5sKMWdDfYci7HdFCVDlj0YehNKpTdJNXoIB1eIMSfRJQD9TNafsg; intercom-session-pgpbhph6=a0M1a2x4cU5sck9DS3NoU1cwZ2tTUh9d3mZzWEozPksMvNiM4FQ7HeYKCFdG73hSYkQxZklrQ0JTckxHWWxZSC0tNkV2ZE5ud283b2duQmlOTGl6Y1kvUT09--bc1qpn3xw9nfz0jml9c2262gmc6f86sfxqlyfhq8wy",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://tryhackme.com/r/p/Gauravjangid",
    "Content-Type": "application/json",
    "Csrf-Token": "OfisDrba-h2_9bENM4YgBsNIXZA4_9cQAd54",
    "Origin": "https://tryhackme.com",
}

# Define the payload for the request
payload = {
    "userPublicId": 1855659,
    "username": "Gauravjangid"
}

# Function to update the profile image
def update_profile_image():
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Profile image updated successfully!")
    else:
        print(f"Failed to update image: {response.status_code}, {response.text}")

# Call the function to update the profile image immediately
update_profile_image()

