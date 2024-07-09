from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Вывод введённых данных в консоль
    print(f"Имя пользователя: {username}")
    print(f"Email: {email}")
    print(f"Пароль: {password}")

    return "Регистрация прошла успешно!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
