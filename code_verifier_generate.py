from utils.code_verifier import generate_code_verifier, generate_code_challenge

# Generate the code_verifier and code_challenge
code_verifier = generate_code_verifier()
code_challenge = generate_code_challenge(code_verifier)

print(f"Code Verifier: {code_verifier}")
print(f"Code Challenge: {code_challenge}")
