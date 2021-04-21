from flask import Flask , render_template, request, redirect # flask에 있는 request갖고오기
from data import Articles
import pymysql

app = Flask(__name__)
app.debug = True

db = pymysql.connect(  #db에 접속하기 위해 connect메소드를 쓴다.->접속환경설정. url 비번, db명, port
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)


@app.route('/', methods=['GET'])
def index():
    cursor = db.cursor()
    # return "Hello World!"
    return render_template("index.html", data = "KIM") #첫번째 인자로 파일 경로를 받음. 두번째 인자로 전달할 데이터를 받는다.

@app.route('/about')
def about():
    cursor = db.cursor()
    return render_template("about.html", hello = "Gary Kim") 
    
@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    # print(topics)
    # articles = Articles()
    # print(articles[0]['title']) 콘솔창에 잘 뜨는지 확인
    return render_template("articles.html", articles = topics) 

@app.route('/article/<int:id>') #params를 써먹음...params..? <>를하고 변수를 이용한다.
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id) # id는 db에 있는 id이다.
    cursor.execute(sql)
    topic = cursor.fetchone()
    # print(topic)
    # articles=Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=["GET","POST"]) #속성은 methods라고 쓰고
def add_articles():
    cursor = db.cursor()
    if request.method == "POST": # request는 method라고 씀.
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]

        # print(author)
        # print(title)
        # print(desc)
        # print(request.form['desc'])
        
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()

        return redirect("/articles")

    # return "<h1>글쓰기 페이지</h1>"
    else:
        return render_template("add_articles.html")

# @app.route('/add_articles', methods = ["POST"]) -> 겟과 포스트방식 따로 쓸때
# def insert_articles():
#     return "Success"

@app.route('/delete/<int:id>', methods=['post']) #params 써먹음. # 팔암스로 보낼아이디
def delete(id): #팔암스에서 받은 아이디
    cursor = db.cursor()
    # sql = 'DELETE FROM topic WHERE id = %s;' 
    # id = [id] #리스트에서 받은 아이디 = 팔암스 아이디
    # cursor.execute(sql, id) #리스트에서 받은 아이디
    sql = 'DELETE FROM topic WHERE id = {};'.format(id) 
    cursor.execute(sql)
    db.commit()

    return redirect("/articles")

@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    cursor = db.cursor()
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        sql = 'UPDATE topic SET title = %s, body = %s WHERE id = {};'.format(id)
        input_data = [title, desc]
        cursor.execute(sql, input_data)
        db.commit()
        print(request.form['title'])
        return redirect('/articles')
    
    else:
        sql = "SELECT * FROM topic WHERE id = {}".format(id) # db아이디임.
        cursor.execute(sql)
        topic = cursor.fetchone()
        # print(topic[1])
        return render_template("edit_article.html", article = topic)


if __name__ == '__main__': # 처음 서버 띄울때 쓰임.
    app.run() 