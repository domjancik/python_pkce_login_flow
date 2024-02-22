import uuid

from flask import Flask, request, redirect
from utils.code_verifier import generate_code_verifier, generate_code_challenge
from utils.get_tokens import get_tokens
from utils.constants import DOMAIN, REGION, CLIENT_ID, REDIRECT_URI

app = Flask(__name__)

verifiers = {} 

@app.route('/login')
def login():
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)
    state = str(uuid.uuid4())
    verifiers[state] = code_verifier
    return redirect(f"https://{DOMAIN}.auth.{REGION}.amazoncognito.com/login?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state={state}&scope=openid%20email%20profile&code_challenge={code_challenge}&code_challenge_method=S256")

@app.route('/')
def callback():
    # Extract query parameters (e.g., code, state) from the callback URL
    auth_code = request.args.get('code')
    state = request.args.get('state')
    
    # Dump the important information received in the callback
    print(f"Authorization Code: {auth_code}")
    print(f"State: {state}")
    
    code_verifier = verifiers.pop(state, None)
    if code_verifier is None:
        raise ValueError("Invalid or reused state")
     
    tokens = get_tokens(
        domain=DOMAIN,
        client_id=CLIENT_ID,
        code=auth_code,
        redirect_uri=REDIRECT_URI,
        code_verifier=code_verifier
    )

    print (tokens)
    return tokens


if __name__ == '__main__':
    app.run(debug=True, port=3000)
