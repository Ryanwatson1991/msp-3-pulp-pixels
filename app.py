import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_index")
def get_index():
    """
    This route gets the index.
    """
    reviews = mongo.db.reviews.find().sort("_id", -1)
    return render_template("index.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = mongo.db.reviews.find({"$text": {"$search": query}}).sort("_id", -1)
    return render_template("index.html", reviews=reviews)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    This route is for user sign up.
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Username or email already in use")
            return redirect(url_for("sign_up"))

        elif existing_email:
            flash("Username or email already in use")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user: 
            # Check hashed password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # invalid password
                flash("Incorrect Username/Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username/Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username): 
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Get session user's reviews
    current_user = session["user"]
    reviews = mongo.db.reviews.find({"user_name": current_user})
    
    user_details = mongo.db.users.find_one(current_user)

    if session["user"]:
        return render_template(
            "profile.html", username=username, user_details=user_details, reviews=reviews)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    # remove user from session cookies
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/review/<review_id>")
def review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("review.html", review=review)

    # found solution for this^^^^ here https://github.com/PrettyPrinted/flask_blog/blob/master/app.py


@app.route("/write_review", methods=["GET", "POST"])
def write_review():
    if request.method == "POST":
        review = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre_name": request.form.get("genre_name"),
            "review_body": request.form.get("review_body"),
            "purchase_link": "www.ryansgoodbookshop.com",
            "user_name": session["user"],
            "book_cover": request.form.get("book_cover")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Uploaded")
        return redirect(url_for("get_index"))

    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("write_review.html", genre=genre)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        edit = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre_name": request.form.get("genre_name"),
            "review_body": request.form.get("review_body"),
            "purchase_link": "www.ryansgoodbookshop.com",
            "user_name": session["user"],
            "book_cover": request.form.get("book_cover")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edit)
        flash("Review Edited")
        return redirect(url_for("get_index"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genre=genre)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Deleted")
    return redirect(url_for("get_index"))


@app.route("/comment", methods=["GET", "POST"])
def comment():
    if request.method == "POST":
        comment = {
            "comment_body": request.form.get("comment_body"),
            "user_name": session["user"],
        }
        mongo.db.comments.insert_one(comment)
        flash("Comment Uploaded")
    return redirect(url_for("get_index"))    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")), 
        debug=True)
