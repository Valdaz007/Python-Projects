from database import Posts
from flask import Flask, render_template, request, url_for, redirect
import time

app = Flask(__name__) #Instantiated Flask Object
newpost = Posts()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home01.html', posts = newpost.posts, comment = len(newpost.posts))

@app.route("/about")
def about():
    return render_template('about01.html', title = 'about')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/create", methods = ["POST"])
def create_post():
    author = request.form['author']
    title = request.form['title']
    date_posted = time.strftime("%e %B, %Y", time.localtime())
    content = request.form['content']
    newpost.get_Dict(author, title, content, date_posted)
    newpost.StoreDatabase()
    return redirect(url_for('home'))
    
if __name__ == "__main__":
    app.run(debug=True)