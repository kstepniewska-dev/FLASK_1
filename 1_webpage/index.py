from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Tu możesz dodać obsługę wysyłania wiadomości (np. email)
        return render_template('contact.html', success=True)
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=3333)