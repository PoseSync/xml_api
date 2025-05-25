from flask import Flask, Response

app = Flask(__name__)

# 루트 URL 접속 시 "Hello, World!" 출력
@app.route("/")
def home():
    return "Hello, World!"

# Twilio가 참조할 음성 안내 XML
@app.route("/voice.xml")
def voice():
    xml_response = """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="Polly.Joanna" language="en-US">This is Hansung Fitness Center. Thank you for calling.</Say>
    </Response>
    """
    return Response(xml_response, mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)