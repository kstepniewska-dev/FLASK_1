from flask import Flask, redirect, request, url_for, render_template, session, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"

users = {
    "alice": { "name" : "Alice", "pass": "alice123"},
    "dave": { "name" : "Dave", "pass": "dave123"},
    "eve": { "name" : "Eve", "pass": "eve123"}
}


def find_user(username, password):
    user = users.get(username)
    if user and user['pass'] == password:
        return user
    return None


@app.route("/")
def index():
    return render_template("users.html", users=users)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        name = request.form.get("name", "").strip()
        password = request.form.get("password", "")

        if not username or not name or not password:
            flash("Wszystkie pola są wymagane.")
            return redirect(url_for("register"))

        if username in users:
            flash("Nazwa użytkownika już istnieje.")
            return redirect(url_for("register"))

        users[username] = {"name": name, "pass": password}
        session["user"] = username
        flash("Zarejestrowano pomyślnie.")
        return redirect(url_for("dashboard"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = find_user(username, password)
        if user:
            session["user"] = username
            flash("Zalogowano pomyślnie.")
            return redirect(url_for("dashboard"))

        flash("Nieprawidłowa nazwa użytkownika lub hasło.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    username = session.get("user")
    if not username:
        flash("Musisz się zalogować.")
        return redirect(url_for("login"))

    user = users.get(username)
    return render_template("dashboard.html", user=user, username=username)


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Wylogowano.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=3333)