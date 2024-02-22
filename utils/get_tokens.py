import requests

def get_tokens(
        domain: str,
        client_id: str,
        code: str,
        redirect_uri: str,
        code_verifier: str
):
    token_url = f'https://{domain}.auth.us-east-1.amazoncognito.com/oauth2/token'

    # Prepare the data payload
    payload = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'code': code,
        'redirect_uri': redirect_uri,
        'code_verifier': code_verifier
    }

    # Headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # POST request to exchange the authorization code for tokens
    response = requests.post(token_url, data=payload, headers=headers)

    # Parse the JSON response
    tokens = response.json()

    return tokens
