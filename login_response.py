import argparse

from utils.get_tokens import get_tokens
from utils.constants import DOMAIN, CLIENT_ID, REDIRECT_URI

parser = argparse.ArgumentParser()
parser.add_argument('--code_verifier', required=True, help='Code verifier value')
parser.add_argument('--auth_code', required=True, help='Auth code value')
args = parser.parse_args()
code_verifier = args.access_token
code = args.auth_code

tokens = get_tokens(
    domain=DOMAIN,
    client_id=CLIENT_ID,
    code=code,
    redirect_uri=REDIRECT_URI,
    code_verifier=code_verifier
)

print(tokens)
