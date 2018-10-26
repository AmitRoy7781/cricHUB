from flask import render_template, request, redirect, session, Blueprint, json
from bs4 import BeautifulSoup
import requests
from cricMongoDB.database import db

app = Blueprint('blog', __name__)

@app.route('/blog/')
def show_blog():

    if 'username' not in session.keys():
        return redirect('/auth/signin')

    data = []
    data = db.blog.find()

    message = []
    for item in data:
        tmp = []
        tmp.append(item["title"])
        tmp.append(item["author"])
        tmp.append(item["date"])
        tmp.append(item["content"])
        message.append(tmp)
        print(tmp[0]+" "+tmp[1]+" "+tmp[2]+" "+tmp[3])

    return render_template("/blog/show_blog.html", blog_data=message)
