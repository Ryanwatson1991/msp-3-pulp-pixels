import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from datetime import datetime
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
    """
    This route allows user to search reviews
    """
    query = request.form.get("query")
    reviews = mongo.db.reviews.find(
        {"$text": {"$search": query}}).sort("_id", -1)
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

        # check if email already exists in db
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
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    This route allows user to log in to website
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check hashed password matches up to username in db
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
    """
    This route takes user to profile page
    that shows their name and the reviews they have written
    """
    # get session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Get session user's reviews
    current_user = session["user"]
    reviews = mongo.db.reviews.find({"user_name": current_user})
    review_count = reviews.count()

    user_details = mongo.db.users.find_one(current_user)

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            user_details=user_details, reviews=reviews, review_count=review_count)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    """
    This route logs user out of website by removing
    their info from 'session' cookie
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/review/<review_id>")
def review(review_id):
    """
    This route takes user to a review page based
    on the _id saved to mongodb for the selected review.
    Reviews are selected from either index or profile page.
    It also allows comments to display on the reviews page
    by matching comments saved in comments db to the _id
    for the review page they were posted on.
    """
    # Gets review based on which review was selected on index or profile page
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    # Gets comments based on which review_id was saved
    # into db for comment when it was posted (see /comment for further details)
    comments = mongo.db.comments.find({"book_id": ObjectId(review_id)})
    return render_template("review.html", review=review, comments=comments)


@app.route("/write_review", methods=["GET", "POST"])
def write_review():
    """
    This route allows user to add a review to database to then be
    displayed on index, profile & review pages.
    """
    if request.method == "POST":
        # Dictionary determining what information is added
        # when user submits a review
        review = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre_name": request.form.get("genre_name"),
            "review_body": request.form.get("review_body"),
            "user_name": session["user"],
            "book_cover": request.form.get("book_cover"),
            "date_posted": datetime.now()
        }
        # Inserts Review
        mongo.db.reviews.insert_one(review)
        return redirect(url_for(
                    "profile", username=session["user"]))

    # Allows genre db to be displayed in write_review form
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("write_review.html", genre=genre)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    This route allows logged in user to edit reviews they have posted
    """
    if request.method == "POST":
        # Dictionary determining what information is to be edited
        edit = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre_name": request.form.get("genre_name"),
            "review_body": request.form.get("review_body"),
            "user_name": session["user"],
            "book_cover": request.form.get("book_cover"),
            "date_posted": datetime.now()
        }
        # Sends review edits to db
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edit)
        return redirect(url_for('review', review_id=review_id))

    # Tells app which review to edit
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genre=genre)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    This route deletes selected review
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for('profile', username=session['user']))


@app.route("/comment/<review_id>", methods=["GET", "POST"])
def comment(review_id):
    """
    This route saves comments to db, it also saves the mongo _id
    of the review page comment is posted on so that when comments
    are displayed app can identify which page to display it on.

    I did struggle with this one a bit but found a solution in code institute
    where someone was trying to do something similar
    """
    if request.method == "POST":
        discussion_id = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        comment = {
            "comment_body": request.form.get("comment_body"),
            "user_name": session["user"],
            "book_id": discussion_id["_id"]
        }
        mongo.db.comments.insert_one(comment)
        flash("Comment Uploaded")
    return redirect(url_for('review', review_id=review_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
