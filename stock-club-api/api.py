from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://stock-club:stock-club-1>@ds155213.mlab.com:55213/heroku_n7zk6r5p"
mongo = PyMongo(app)
api = Api(app)

FUNDS = {
     "total": 2000,
    "available": 300,
    "used": 1600,
    "pending": 100
}

MEMBERS = [{
        "id": "asdf1",
        "firstName": "John",
        "lastName": "Lundeen",
        "username": "john.lundeen",
        "email": "john.lundeen@email.com"
    }, {
        "id": "asdf12",
        "firstName": "Braxton",
        "lastName": "Kinner",
        "username": "braxton.fart",
        "email": "braxton.fart@email.com"
    }, {
        "id": "asdf3",
        "firstName": "Alex",
        "lastName": "Peterson",
        "username": "alex.peterson",
        "email": "alex.peterson@email.com"
    }, {
        "id": "asdf4",
        "firstName": "Troy",
        "lastName": "Sawtell",
        "username": "troy.sawtell",
        "email": "troy.sawtell@email.com"
}]

LOGIN = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFzZGYiLCJ1c2VybmFtZSI6ImJ1dHQuc25pZmZlciIsImxhc3ROYW1lIjoic25pZmZlciIsImZpcnN0TmFtZSI6ImJ1dHQiLCJlbWFpbCI6ImJ1dHQuc25pZmZlckBlbWFpbC5jb20iLCJ0b2tlbiI6ImFzZGZhc2RmYXNkZiIsInN1YiI6IjEyMzQ1Njc4OTAiLCJpYXQiOjE1MTYyMzkwMjJ9.lLZ4Eg9RaIL6EkwU4Ct9JQTp9efLFfl7NMo_vD_Wg3c"
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'GET':
        return "got here'
        #dumps(mongo.db.members.find()) or 'no members'
    elif request.method == 'POST':
         mongo.db.members.insert(request.json)
         return 'member added'
    else:
        return 'error'

# Funds
# handles the funds of a stock club
class Funds(Resource):
    def get(self):
        return FUNDS


# # Members
# # shows a list of all todos, and lets you POST to add new tasks
# class Members(Resource):
#     def get(self):
#         return mongo.db.members.find()

#     def post(self, newMember):
#         mongo.db.members.insert(newMember)
#         return 'member added'

# Login
# shows a list of all todos, and lets you POST to add new tasks
class Login(Resource):
    def post(self):
        return LOGIN

##
## Actually setup the Api resource routing here
##
# api.add_resource(Members, '/members')
api.add_resource(Funds, '/funds')
api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True)