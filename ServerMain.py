from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3

#Создание Flask приложения
app = Flask(__name__)
api = Api(app)

# Подключение к бд
dbRoute = sqlite3.connect("db.sqlite3", check_same_thread=False)


# Должности


class Post(Resource):
    def get(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("SELECT * FROM post")
            getPost = dbCursor.fetchall()
            listPost = []
            for i in getPost:
                listPost.append({"id": i[0], "post_name": i[1]})
            return {"Response": listPost}

    def post(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("post_name", type=str, location="form")
            dbCursor.execute("INSERT INTO post (post_name) VALUES (?)",
                             (dbParser.parse_args()["post_name"],))
            dbRoute.commit()


class PostById(Resource):
    def get(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("SELECT * FROM post WHERE id = ?",
                             (id,))
            getPost = dbCursor.fetchall()
            return {"id": getPost[0][0], "post_name": getPost[0][1]}

    def put(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("post_name", type=str, location="form")
            dbCursor.execute("UPDATE post SET post_name = ? WHERE id = ?",
                             (dbParser.parse_args()["post_name"], id,))
            dbRoute.commit()

    def delete(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("DELETE FROM post WHERE id = ?",
                             (id,))
            dbRoute.commit()


# Факультеты


class Faculty(Resource):
    def get(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("SELECT * FROM faculty")
            getFaculty = dbCursor.fetchall()
            listFaculty = []
            for i in getFaculty:
                listFaculty.append({"id": i[0], "faculty_name": i[1],
                                    "faculty_short_name": i[2]})
            return {"Response": listFaculty}

    def post(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("faculty_name", type=str, location="form")
            dbParser.add_argument("faculty_short_name", type=str, location="form")
            dbCursor.execute("INSERT INTO faculty (faculty_name, faculty_short_name) VALUES (?, ?)",
                             (dbParser.parse_args()["faculty_name"],
                              dbParser.parse_args()["faculty_short_name"],))
            dbRoute.commit()


class FacultyById(Resource):
    def get(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("SELECT * FROM faculty WHERE id = ?", (id,))
            getFaculty = dbCursor.fetchall()
            return {"id": getFaculty[0][0], "faculty_name": getFaculty[0][1],
                    "faculty_short_name": getFaculty[0][2]}

    def put(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("faculty_name", type=str, location="form")
            dbParser.add_argument("faculty_short_name", type=str, location="form")
            dbCursor.execute("UPDATE faculty SET faculty_name = ?, faculty_short_name = ? WHERE id = ? ",
                             (dbParser.parse_args()["faculty_name"],
                              dbParser.parse_args()["faculty_short_name"], id,))
            dbRoute.commit()

    def delete(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("DELETE FROM faculty WHERE id = ?",
                             (id,))
            dbRoute.commit()


# Кафедры


class Chair(Resource):
    def get(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("SELECT chair.id, chair.faculty_id, chair.code, chair.chair_name, chair.chair_short_name, faculty.faculty_short_name FROM chair, faculty WHERE chair.faculty_id = faculty.id")
            getChair = dbCursor.fetchall()
            listChair = []
            for i in getChair:
                print(i)
                listChair.append({"id": i[0], "faculty_id": i[1], "code": i[2],
                                  "chair_name": i[3], "chair_short_name": i[4],
                                  "faculty_short_name": i[5]})
            print(listChair)
            return {"Response": listChair}

    def post(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("faculty_id", type=int, location="form")
            dbParser.add_argument("code", type=str, location="form")
            dbParser.add_argument("chair_name", type=str, location="form")
            dbParser.add_argument("chair_short_name", type=str, location="form")
            dbCursor.execute("INSERT INTO chair (faculty_id, code, chair_name, chair_short_name) VALUES (?, ?, ?, ?)",
                             (dbParser.parse_args()["faculty_id"], dbParser.parse_args()["code"],
                              dbParser.parse_args()["chair_name"], dbParser.parse_args()["chair_short_name"],))
            dbRoute.commit()


class ChairById(Resource):
    def get(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute(  "SELECT chair.id, chair.faculty_id, chair.code, chair.chair_name, chair.chair_short_name, faculty.faculty_short_name FROM chair, faculty WHERE chair.faculty_id = faculty.id AND chair.id = ?",
                (id,))
            getChair = dbCursor.fetchall()
            return {"id": getChair[0][0], "faculty_id": getChair[0][1], "code": getChair[0][2],
                    "chair_name": getChair[0][3], "chair_short_name": getChair[0][4],
                    "faculty_short_name": getChair[0][5]}

    def put(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("faculty_id", type=int, location="form")
            dbParser.add_argument("code", type=str, location="form")
            dbParser.add_argument("chair_name", type=str, location="form")
            dbParser.add_argument("chair_short_name", type=str, location="form")
            dbCursor.execute( "UPDATE chair SET faculty_id = ?, code = ?, chair_name = ?, chair_short_name = ? WHERE id = ? ",
                (dbParser.parse_args()["faculty_id"], dbParser.parse_args()["code"],
                 dbParser.parse_args()["chair_name"], dbParser.parse_args()["chair_short_name"], id,))
            dbRoute.commit()

    def delete(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("DELETE FROM chair WHERE id = ?",
                             (id,))
            dbRoute.commit()


# Преподаватели


class Teacher(Resource):
    def get(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute( "SELECT teacher.id, teacher.chair_id, teacher.post_id, teacher.second_name, teacher.first_name, teacher.last_name, teacher.phone, teacher.email, chair.chair_short_name, post.post_name FROM teacher, chair, post WHERE teacher.chair_id = chair.id AND teacher.post_id = post.id")
            getTeacher = dbCursor.fetchall()
            listTeacher = []
            for i in getTeacher:
                listTeacher.append({"id": i[0], "chair_id": i[1], "post_id": i[2], "second_name": i[3],
                                    "first_name": i[4], "last_name": i[5], "phone": i[6], "email": i[7],
                                    "chair_short_name": i[8], "post_name": i[9]})
            return {"Response": listTeacher}

    def post(self):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("chair_id", type=int, location="form")
            dbParser.add_argument("post_id", type=int, location="form")
            dbParser.add_argument("second_name", type=str, location="form")
            dbParser.add_argument("first_name", type=str, location="form")
            dbParser.add_argument("last_name", type=str, location="form")
            dbParser.add_argument("phone", type=str, location="form")
            dbParser.add_argument("email", type=str, location="form")
            dbCursor.execute("INSERT INTO teacher (chair_id, post_id, second_name, first_name, last_name, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)",
                             (dbParser.parse_args()["chair_id"], dbParser.parse_args()["post_id"],
                              dbParser.parse_args()["second_name"], dbParser.parse_args()["first_name"],
                              dbParser.parse_args()["last_name"], dbParser.parse_args()["phone"],
                              dbParser.parse_args()["email"], ))
            dbRoute.commit()

class TeacherById(Resource):
    def get(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute(
                "SELECT teacher.id, teacher.chair_id, teacher.post_id, teacher.second_name, teacher.first_name, teacher.last_name, teacher.phone, teacher.email, chair.chair_short_name, post.post_name FROM teacher, chair, post WHERE teacher.chair_id = chair.id AND teacher.post_id = post.id AND teacher.id = ?",
                (id,))
            getTeacher = dbCursor.fetchall()
            return {"id": getTeacher[0][0], "chair_id": getTeacher[0][1], "post_id": getTeacher[0][2],
                    "second_name": getTeacher[0][3], "first_name": getTeacher[0][4], "last_name": getTeacher[0][5],
                    "phone": getTeacher[0][6], "email": getTeacher[0][7], "chair_short_name": getTeacher[0][8],
                    "post_name": getTeacher[0][9]}

    def put(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbParser = reqparse.RequestParser()
            dbParser.add_argument("chair_id", type=int, location="form")
            dbParser.add_argument("post_id", type=int, location="form")
            dbParser.add_argument("second_name", type=str, location="form")
            dbParser.add_argument("first_name", type=str, location="form")
            dbParser.add_argument("last_name", type=str, location="form")
            dbParser.add_argument("phone", type=str, location="form")
            dbParser.add_argument("email", type=str, location="form")
            dbCursor.execute("UPDATE teacher SET chair_id = ?, post_id = ?, second_name = ?, first_name = ?, last_name = ?, phone = ?, email = ? WHERE id = ? ",
                (dbParser.parse_args()["chair_id"], dbParser.parse_args()["post_id"],
                 dbParser.parse_args()["second_name"], dbParser.parse_args()["first_name"],
                 dbParser.parse_args()["last_name"], dbParser.parse_args()["phone"],
                 dbParser.parse_args()["email"], id,))
            dbRoute.commit()

    def delete(self, id):
        with dbRoute:
            dbCursor = dbRoute.cursor()
            dbCursor.execute("DELETE FROM teacher WHERE id = ?",
                             (id,))
            dbRoute.commit()


# Ссылки (Должности)
api.add_resource(Post, "/Post")
api.add_resource(PostById, "/Post/<int:id>")

# Ссылки (Факультеты)
api.add_resource(Faculty, "/Faculty")
api.add_resource(FacultyById, "/Faculty/<int:id>")

# Ссылки (Кафедры)
api.add_resource(Chair, "/Chair")
api.add_resource(ChairById, "/Chair/<int:id>")

# Ссылки (Преподаватели)
api.add_resource(Teacher, "/Teacher")
api.add_resource(TeacherById, "/Teacher/<int:id>")

# Запуск сервера
api.init_app(app)
app.run(debug=True, host="192.168.3.57")

