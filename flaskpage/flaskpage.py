import uvicorn
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, request, render_template, make_response, Response

app = Flask(__name__)

@app.after_request
def after_request(response = Response()):
    if response.status_code != 200:
        return Response(render_template('index.html'), status=response.status_code, mimetype='text/html')
    return response

@app.route('/')
def show_index():
    return render_template('index.html')


asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    uvicorn.run(app= asgi_app , host="127.0.0.1", port=7000)
