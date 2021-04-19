from flask import Flask , render_template
from data import Articles

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    # return "Hello World!"
    return render_template("index.html") #첫번째 인자로 파일 경로를 받음. 두번째 인자로 전달할 데이터를 받는다.

@app.route('/about')
def about():
    return render_template("about.html", hello = "Gary Kim") 
    
@app.route('/articles')
def articles():
    articles = Articles()
    # print(articles[0]['title']) 콘솔창에 잘 뜨는지 확인
    return render_template("articles.html", articles = articles) 

@app.route('/article/<int:id>') #params를 써먹음...params..? <>를하고 변수를 이용한다.
def article(id):
    print(id)
    return "Success"

if __name__ == '__main__': # 처음 서버 띄울때 쓰임.
    app.run()