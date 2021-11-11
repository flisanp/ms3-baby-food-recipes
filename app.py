import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from typing import Union
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# code from mentor Reuben Ferrante
def is_logged_in() -> Union[str, None]:
    """
    Returns None if the user isn't logged in otherwise returns the username
    """
    return session.get("user")


# landing page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# breakfast category page
@app.route("/breakfast")
def breakfast():
    recipes = list(mongo.db.recipes.find())
    return render_template("breakfast.html", recipes=recipes)


# lunch category page
@app.route("/lunch")
def lunch():
    recipes = list(mongo.db.recipes.find())
    return render_template("lunch.html", recipes=recipes)


# dinner category page
@app.route("/dinner")
def dinner():
    recipes = list(mongo.db.recipes.find())
    return render_template("dinner.html", recipes=recipes)


# snack category page
@app.route("/snack")
def snack():
    recipes = list(mongo.db.recipes.find())
    return render_template("snack.html", recipes=recipes)


# all recipes page
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# search recipes function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Hi, {}".format(request.form.get("username")))
                return redirect(url_for("account", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# account page (Mentor Reuben Ferrante helped
# me with parts of the code for this function)
@app.route("/account", methods=["GET", "POST"])
def account():
    if is_logged_in():
        # grab the session user's username from db
        user = mongo.db.users.find_one({"username": session["user"]})
        recipes = list(mongo.db.recipes.find({"created_by": user["username"]}))

        if session["user"]:
            return render_template("account.html", user=user, recipes=recipes)
        return redirect(url_for("login"))


# logout function
@app.route("/logout")
def logout():
    if is_logged_in():
        # remove user from session cookie
        flash("You have been logged out, see you soon!")
        session.pop("user", None)
    return redirect(url_for("login"))


# create recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if is_logged_in() and request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# update recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if is_logged_in() and request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your Recipe Is Updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if is_logged_in():
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Your Recipe is Deleted")
    return redirect(url_for("get_recipes"))


# manage categories page
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add category function
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit category function
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete category function
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("get_categories"))


# mentor Reuben Ferrante helped me with these
# functions for error handling and to make them more efficiently
# 404 error page, code from:
# https://blog.miguelgrinberg.com/post/
# the-flask-mega-tutorial-part-vii-error-handling
@app.errorhandler(404)
def not_found_error(error):
    return (
        render_template(
            "error.html",
            error_message="We can't find the page you're looking for",
            error_title="Oooopss...",
        ),
        404,
    )


@app.errorhandler(Exception)
def server_error(error):
    # optional
    error_title = "Oooops..."
    if isinstance(error, bson.errors.InvalidId):
        error_message = "Couldn't find it in the database"
    else:
        error_message = "Something went wrong"
    return (
        render_template(
            "error.html", error_message=error_message, error_title=error_title
        ),
        500,
    )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
