from flask import Flask
from flask_restful import Api, Resource, reqparse
import datetime

app = Flask(__name__)

api = Api(app)

new_user_post_args = reqparse.RequestParser()
new_user_post_args.add_argument("name",
                                type=str,
                                help="You must input a name.",
                                required=True)

new_user_post_args.add_argument("age",
                                type=int,
                                help="You must specify the age for a given name.",
                                required=False)


class New_User(Resource):
    def post(self):
        args = new_user_post_args.parse_args()
        age = args['age']
        name = args['name']
        now = datetime.datetime.now()
        response = {
            'name': name,
            'age': age,
            'created_on': now.strftime("%m/%d/%Y, %H:%M:%S")
        }
        return response


api.add_resource(New_User, "/api/new_user")

# http://localhost/api/new_user
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

