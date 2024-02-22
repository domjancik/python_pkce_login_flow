import os
import base64
import hashlib

def base64url_encode(input):
    """Encode input in a base64url format"""
    return base64.urlsafe_b64encode(input).rstrip(b'=')

def generate_code_verifier(length=128):
    """Generate a cryptographically secure code_verifier"""
    token = os.urandom(length)
    return base64url_encode(token).decode('utf-8')

def generate_code_challenge(code_verifier):
    """Generate a code_challenge based on the code_verifier"""
    sha256_digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    return base64url_encode(sha256_digest).decode('utf-8')
