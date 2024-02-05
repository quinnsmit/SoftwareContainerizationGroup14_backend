# import os
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
#
#
#
# app = Flask(__name__)
#
# db_root_password = os.getenv("db_root_password", "default_password")
# print(db_root_password)
# MYSQL_SERVICE_HOST = os.getenv("MYSQL_SERVICE_HOST", "default_host")
# MYSQL_SERVICE_PORT = os.getenv("MYSQL_SERVICE_PORT", "default_port")
# db_name = os.getenv("db_name", "default_db_name")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:YWRtaW4=@' + MYSQL_SERVICE_HOST + ':' + str(MYSQL_SERVICE_PORT) + '/' + db_name
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(255), nullable=False, unique=True)
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     password_hash = db.Column(db.String(255), nullable=False)
#
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'username': self.username,
#             'email': self.email,
#         }
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False, unique=True)
#     description = db.Column(db.Text)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#         }
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     created_at = db.Column(db.TIMESTAMP, default=datetime.now)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'content': self.content,
#             'user_id': self.user_id,
#             'category_id': self.category_id,
#             'created_at': self.created_at,
#         }
#
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
#     created_at = db.Column(db.TIMESTAMP, default=datetime.now)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'content': self.content,
#             'user_id': self.user_id,
#             'task_id': self.task_id,
#             'created_at': self.created_at,
#         }
#
# with app.app_context():
#     db.create_all()
#
# @app.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify({'users': [user.serialize() for user in users]})
#
# @app.route('/categories', methods=['GET'])
# def get_categories():
#     categories = Category.query.all()
#     return jsonify({'categories': [category.serialize() for category in categories]})
#
# @app.route('/categories', methods=['POST'])
# def create_category():
#     data = request.get_json()
#     new_category = Category(name=data['name'], description=data['description'])
#     db.session.add(new_category)
#     db.session.commit()
#     return jsonify({'message': 'Category created successfully.'})
#
# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     tasks = Task.query.all()
#     return jsonify({'tasks': [task.serialize() for task in tasks]})
#
# @app.route('/tasks', methods=['POST'])
# def create_task():
#     data = request.get_json()
#     new_task = Task(title=data['title'], content=data['content'], user_id=data['user_id'], category_id=data['category_id'])
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify({'message': 'Task created successfully.'})
#
# @app.route('/comments', methods=['GET'])
# def get_comments():
#     comments = Comment.query.all()
#     return jsonify({'comments': [comment.serialize() for comment in comments]})
#
# @app.route('/comments', methods=['POST'])
# def create_comment():
#     data = request.get_json()
#     new_comment = Comment(content=data['content'], user_id=data['user_id'], category_id=data['category_id'])
#     db.session.add(new_comment)
#     db.session.commit()
#     return jsonify({'message': "comment created."})
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User created successfully.'}), 201
#
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(username=data['username']).first()
#
#     if user and check_password_hash(user.password_hash, data['password']):
#
#         return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
#     else:
#         return jsonify({'message': 'Invalid username or password'}), 401
#
#
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)

"""Code for a flask API to Create, Read, Update, Delete users"""
import os
from flask import jsonify, request, Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)


@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"


@app.route("/create", methods=["POST"])
def add_user():
    """Function to create a user to the MySQL database"""
    json = request.json
    name = json["name"]
    email = json["email"]
    pwd = json["pwd"]
    if name and email and pwd and request.method == "POST":
        sql = "INSERT INTO users(user_name, user_email, user_password) " \
              "VALUES(%s, %s, %s)"
        data = (name, email, pwd)
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
            resp = jsonify("User created successfully!")
            resp.status_code = 200
            return resp
        except Exception as exception:
            return jsonify(str(exception))
    else:
        return jsonify("Please provide name, email and pwd")


@app.route("/users", methods=["GET"])
def users():
    """Function to retrieve all users from the MySQL database"""
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


@app.route("/user/<int:user_id>", methods=["GET"])
def user(user_id):
    """Function to get information of a specific user in the MSQL database"""
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=%s", user_id)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


@app.route("/update", methods=["POST"])
def update_user():
    """Function to update a user in the MYSQL database"""
    json = request.json
    name = json["name"]
    email = json["email"]
    pwd = json["pwd"]
    user_id = json["user_id"]
    if name and email and pwd and user_id and request.method == "POST":
        # save edits
        sql = "UPDATE users SET user_name=%s, user_email=%s, " \
              "user_password=%s WHERE user_id=%s"
        data = (name, email, pwd, user_id)
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("User updated successfully!")
            resp.status_code = 200
            cursor.close()
            conn.close()
            return resp
        except Exception as exception:
            return jsonify(str(exception))
    else:
        return jsonify("Please provide id, name, email and pwd")


@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    """Function to delete a user from the MySQL database"""
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE user_id=%s", user_id)
        conn.commit()
        cursor.close()
        conn.close()
        resp = jsonify("User deleted successfully!")
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
