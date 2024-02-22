from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def callback():
    # Extract query parameters (e.g., code, state) from the callback URL
    auth_code = request.args.get('code')
    state = request.args.get('state')
    
    # Dump the important information received in the callback
    print(f"Authorization Code: {auth_code}")
    print(f"State: {state}")
    
    # You can add additional logic here to exchange the code for a token, etc.

    return 'Callback received! Check console for details.'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
