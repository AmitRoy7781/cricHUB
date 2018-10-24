import string
from flask import Flask, make_response
from flask import render_template, request, redirect, session, Blueprint
from cricMongoDB.database import db

app = Blueprint('auth', __name__)


@app.route("/auth/signup")
def signUp(data=None):

    if 'username' in session.keys():
        return redirect('/')
    #print(data)
    return render_template('auth/signup.html', userinfo=data)



@app.route("/auth/signup-validation", methods=['POST', 'GET'])
def signup_validation():
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data['name']
        username = data['username']
        password = data['password']
        c_password = data['c_password']
        email = data['email']
        phone_number = data['phone_number']
        flag = True

        if len(name)<6:
            flag = False
            data['name_msg'] = 'Name must be atleast 6 characters.'

        for ch in name:
            if ch not in string.ascii_letters and ch != ' ':
                flag = False
                data['name_msg'] = 'Name can contain [a-z][A-Z] and whitespace only.'

        if len(username) < 6:
            flag = False
            data['username_msg'] = 'Username must be atleast 6 characters.'

        find = db.users.find_one({"username": str(username)})
        if find is not None:
            flag = False
            data['username_msg'] = 'Username already exists'

        for ch in username:
            if ch not in string.ascii_letters and ch not in string.digits:
                flag = False
                data['username_msg'] = 'Username can contain [a-z][A-z][0-9] only.'

        if len(password) < 6:
            flag = False
            data['password_msg'] = 'Password length must be at least 6.'

        elif password != c_password:
            flag = False
            data['c_password_msg'] = 'Password did not match.'

        find = db.users.find_one({"email": str(email)})
        if find is not None:
            flag = False
            data['email_msg'] = 'Email alreadye exists'

        if '@' not in email:
            flag = False
            data['email_msg'] = 'Email format is not correct'
        elif '.' not in email.split('@')[1]:
            flag = False
            data['email_msg'] = 'Email format is not correct'

        for ch in phone_number:
            if ch not in string.digits:
                flag = False
                data['phone_number_msg'] = 'Phone Number can contain only digits'

        #print(flag)

        if flag is True:
            data.pop('c_password')
            posts = db.users
            posts.insert_one(data)
            return redirect('/auth/signin')

        return signUp(data)


@app.route("/auth/signin")
def signin(data=None):
    # if 'username' in session.keys():
    #     return redirect('/profile/' + session['username'])
    return render_template('auth/signin.html',userinfo=data)


@app.route("/auth/signin-validation", methods=['POST', 'GET'])
def login_validation():
    if request.method == 'POST':
        data = request.form.to_dict()
        username = data['username']
        password = data['password']

        flag = True

        find = db.users.find_one({"username": str(username)})

        if find is None:
            flag = False
            data['username_msg'] = 'Username does not Exist'
        elif find['password'] != password:
            flag = False
            data['password_msg'] = 'Wrong password. Try again.'
        if flag is False:
            return signin(data)
        session['username'] = username
        #return redirect('/profile/'+session['username'])

        res = make_response(redirect('/'))
        res.set_cookie('realtime-chat-nickname', session['username'])
        print(res)

        return res

        #return redirect('/')


@app.route("/auth/logout")
def logout():
    if 'username' in session.keys():
        session.pop('username')

    if request.cookies.get('realtime-chat-nickname') is None:
        # do nothing
        print("No cookies")
    else:
        res = make_response(redirect('/'))
        res.set_cookie('realtime-chat-nickname', "")
        print(res)

        return res

    #return redirect('/')

