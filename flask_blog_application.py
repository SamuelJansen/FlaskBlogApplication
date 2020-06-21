from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return f'''<h1>{__name__} api running</h1>'''

class Posts(Resource):
    def get(self):
        return {'posts': []}

    def post(self):
        pass

api.add_resource(Posts, '/posts')

if __name__ == '__main__':
    app.run(debug=True)
