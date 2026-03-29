from flask import Flask, request, jsonify
from flask_cors import CORS # Agar error aaye toh 'pip install flask-cors' karna

app = Flask(__name__)
CORS(app) # Ye mobile se connection allow karne ke liye zaruri hai

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    news_url = data.get('url', '').lower()
    
    # Trusted News Sources (API simulation)
    trusted_channels = ["aajtak.in", "ndtv.com", "bbc.com", "indiatoday.in", "timesofindia.indiatimes.com"]
    
    # Agar link inme se kisi ka hai toh Green (Safe/Real)
    if any(channel in news_url for channel in trusted_channels):
        return jsonify({"status": "real", "color": "green", "message": "Verified Source: This news is from a trusted channel."})
    else:
        # Agar unknown hai toh Red (Fake/Unverified)
        return jsonify({"status": "fake", "color": "red", "message": "Unverified Source: Use caution, this might be fake news!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
