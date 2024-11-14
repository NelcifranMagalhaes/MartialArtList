from flask import render_template, request, redirect, session, flash, url_for
from models.users import Users
from objects.userForm import UserForm, UserFormCreate
from app import app, db
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    form = UserForm()
    if next_page:
        return render_template('login.html', next_page=next_page, form=form)
    else:
        return render_template('login.html', next_page=url_for('index'), form=form)

@app.route('/auth', methods=['POST', ])
def auth():
  form = UserForm(request.form)
  user = Users.query.filter_by(nickname=form.nickname.data).first()
  password = check_password_hash(user.password, form.password.data)

  if user and password:
       session['user_logged'] = user.nickname
       flash(user.nickname + ' Logged with sucess!!')
       next_page = request.form['next_page']
       return redirect(next_page)
  else:
      flash('Error, Fill again!!')
      return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('Logout with Sucess!')
    return redirect(url_for('index'))


@app.route('/newUser')
def newUser():
  form = UserFormCreate()
  return render_template('new_user.html', title='New User', form=form)


@app.route('/userCreate', methods=['POST', ])
def userCreate():
  form = UserFormCreate(request.form)
  if not form.validate_on_submit():
    return redirect(url_for('newUser'))
  name = form.name.data
  nickname = form.nickname.data
  password = form.password.data
  password_crypt = generate_password_hash(password).decode('utf-8')
  user = Users.query.filter_by(nickname=nickname).first()
  if user:
    flash('user already in database!')
    return redirect(url_for('newUser'))

  new_user = Users(name=name, nickname=nickname, password=password_crypt)
  db.session.add(new_user)
  db.session.commit()    
  flash('User added with sucess!')
  return redirect(url_for('index'))