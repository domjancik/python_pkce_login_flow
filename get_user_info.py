import requests
import argparse

from utils.constants import DOMAIN

parser = argparse.ArgumentParser()
parser.add_argument('--access_token', required=True, help='Access token value')
args = parser.parse_args()
access_token = args.access_token

url = f"https://{DOMAIN}.auth.us-east-1.amazoncognito.com/oauth2/userInfo"
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
user_info = response.json()

print(user_info)
