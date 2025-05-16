from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

token = "akash_8110231942"

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Akash API</title></head>
        <body style="text-align:center; font-family:sans-serif; padding-top:50px;">
            <h1>Welcome to My API</h1>
            <p>By <strong>@Akash_Servers</strong></p>
        </body>
    </html>
    '''

@app.route('/api')
def my_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    api_url = f"https://terabox.web.id/url?url={url}&token={token}"
    
    try:
        r = requests.get(api_url)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": "Failed to fetch from source API", "details": str(e)}), 500

# For Vercel, we expose the 'app' variable
app = app
