# -*- coding: utf-8 -*- 
import utils
import json
from flask import Flask, request, render_template
app = Flask(__name__)

PRE_PATH = "./blogs/"

@app.route('/')
def index():
    return render_template('post_blog.html').encode('utf-8')

@app.route('/blog', methods=['POST'])
def post_blog():
    print('title:')
    title = request.form['title']
    print(title)
    content = request.form['content']
    content = content
    print(content)
    fname = PRE_PATH + title
    utils.write_md(fname, content)
    return json.dumps({'status':'OK', 'message':'success'})

@app.route('/blog_update', methods=['POST'])
def update_blog():
    print('title:')
    title = request.form['title']
    print(title)
    content = request.form['content']
    content = content
    print(content)
    fname = PRE_PATH + title
    utils.append_md(fname, content)
    return json.dumps({'status':'OK', 'message':'success'})

@app.route('/test', methods=['POST'])
def test():
    print("get request test")
    return json.dumps({'status':'OK', 'message':'success'})

def main():
    print("test")
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
