from flask import render_template, request, redirect, session, Blueprint, json
from bs4 import BeautifulSoup
import requests

import datetime
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




@app.route('/blog/add/', methods=['GET', 'POST'])

#To post something in
#in this feature blog
def add():

    if request.method == 'POST':

        title = request.form['title']

        content = request.form['content']
        if title=="" or content =="":
            return redirect('/blog/add/')
        else:
            blog_message = {}

            blog_message["author"] =session['username']

            blog_message["title"] = title

            blog_message["content"] = content

            now = datetime.datetime.now()

            now=now.replace(second=0, microsecond=0)

            blog_message["date"]=str(now)

            posts = db.blog

            posts.insert_one(blog_message)

            print(title+content+str(now))

            return show_blog()

    else:

        return render_template("/blog/add.html")
