from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://@localhost/SC_Group14'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'created_at': self.created_at,
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'task_id': self.task_id,
            'created_at': self.created_at,


            db.create_all()



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.serialize() for user in users]})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully.'})

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify({'categories': [category.serialize() for category in categories]})

@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'], description=data['description'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully.'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [task.serialize() for task in tasks]})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], content=data['content'], user_id=data['user_id'], category_id=data['category_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully.'})

@app.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify({'comments': [comment.serialize() for comment in comments]})

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    new_comment = Comment(content=data['content'], user_id=data['user_id'], category_id=data['category_id'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': "comment created."})

 

