"""Создать форму для регистрации пользователей на сайте.
 Форма должна содержать поля "Имя", "Фамилия", 
"Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных,
 а пароль должен быть зашифрован."""

from flask import Flask, render_template, request, make_response, redirect
from flask import session
from flask import url_for
from form import LoginForm, RegisterForm, RegistrationForm
from models import db, Users
from random import choice, randint


app = Flask(__name__)
app.secret_key = '1231frf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_02.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_user():
    for i in register():
        users = Users(name=f'name{i}', last_name=f'last_name{i}', email=f'email{i}', password=f'password{i}')
        db.session.add(users)
    db.session.commit()



@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for(login))
    

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        print(email, password)

    return render_template('register.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)
