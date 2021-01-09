


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username): 
    # get session user's details from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Get session user's reviews
    current_user = session["user"]
    review = mongo.db.reviews.find({"user_name": current_user})

    bio = mongo.db.users.find_one()["bio"]
    email = mongo.db.users.find_one()["email"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, bio=bio, email=email, review=review)

    return redirect(url_for("log_in"))
