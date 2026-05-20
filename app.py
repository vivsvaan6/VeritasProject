from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow requests from external origins (frontend)
CORS(app)

@app.route('/verify', methods=['POST'])
def verify():
    """
    API Endpoint to verify the authenticity of a news URL based on trusted domains.
    Expects a JSON payload containing the 'url' key.
    """
    data = request.get_json()
    
    # Extract the URL and convert it to lowercase for case-insensitive verification
    news_url = data.get('url', '').lower()
    
    # White-listed authoritative news domains for verification simulation
    trusted_channels = [
        "aajtak.in", 
        "ndtv.com", 
        "bbc.com", 
        "indiatoday.in", 
        "timesofindia.indiatimes.com"
    ]
    
    # Perform standard substring matching against the trusted domains list
    if any(channel in news_url for channel in trusted_channels):
        return jsonify({
            "status": "real", 
            "color": "green", 
            "message": "Verified Source: This news originates from a trusted channel."
        })
    else:
        # Fallback response for unverified or potentially malicious links
        return jsonify({
            "status": "fake", 
            "color": "red", 
            "message": "Unverified Source: Use caution, this domain is not present in our trusted directory!"
        })

if __name__ == '__main__':
    import os
    # Dynamic port binding logic required for cloud deployment environments like Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
