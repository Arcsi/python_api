from flask import *
import json
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/index')
def frontend():
    return frontend('index.html')

@app.route("/")
def view():
    con = sqlite3.connect("cars.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Cars")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        name = data["name"]
        email = data["email"]
        address = data["address"]
        number = data["number"]
        country = data["country"]

        with sqlite3.connect("cars.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Cars (name, email, address,number,country) values (?,?,?,?,?)", (name, email, address, number, country))
            con.commit()
            msg = "Cars successfully Added"
    except:
        con.rollback()
        msg = "We can not add the employee to the list"
    finally:
        return name
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("cars.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Cars where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return msg
            con.close()

@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["id"]
        name = data["name"]
        email = data["email"]
        address = data["address"]
        number = data["number"]
        country = data["country"]

        with sqlite3.connect("cars.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE Cars SET name=?, email=?, address=? number=?, country=?, WHERE id=?", (name, email, address, number ,country +id))
            con.commit()
            msg = "Cars successfully Updated"
    except:
        con.rollback()
        msg = "We can not update the employee to the list"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
