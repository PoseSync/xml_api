from flask import Flask, Response

app = Flask(__name__)

@app.route("/voice.xml")
def voice():
    xml_response = """
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="alice" language="ko-KR">낙상이 감지되었습니다. 즉시 확인 바랍니다.</Say>
    </Response>
    """
    return Response(xml_response, mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
