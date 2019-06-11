from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    id = request.args.get('id')
    conn = sqlite3.connect(r"C:\Users\Administrator\PycharmProjects\xiaoshuo_read\小说阅读\cszatxy.db")
    cursor = conn.cursor()
    sql = 'select id,title,content from atxy'
    rows = cursor.execute(sql)
    all_chapter = []  # 列表保存所有章节内容[{},{},{}...]
    for row in rows:
        chapter = {}
        chapter['id'] = row[0]
        chapter['title'] = row[1]
        chapter['content'] = row[2]
        all_chapter.append(chapter)
    return render_template('index.html', all_chapter=all_chapter)


@app.route('/show/')
def show():
    conn = sqlite3.connect(r"C:\Users\Administrator\PycharmProjects\xiaoshuo_read\小说阅读\cszatxy.db")
    cursor = conn.cursor()
    sql = 'select id,title,content from atxy where id=%s' % request.args.get('id')
    rows = cursor.execute(sql)
    all_chapter = {}  # 单章节内容{}
    for row in rows:
        all_chapter['id'] = row[0]
        all_chapter['title'] = row[1]
        all_chapter['content'] = row[2]
    return render_template('show.html', all_chapter=all_chapter)


if __name__ == '__main__':
    app.run(debug='ON')
