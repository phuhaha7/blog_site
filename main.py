from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
data_posts = requests.get(url).json()
posts = []
for data in data_posts:
    post1 = Post(data["id"], data["title"], data["subtitle"], data["body"])
    posts.append(post1)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<num>')
def get_post(num):
    post = None
    for blog in posts:
        if blog.id == int(num):
            post = blog
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
