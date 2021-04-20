# 파이썬 언어로 마이에스큐엘 접속해서 크레이에이트하고있음. 커넥트하고 커서. 익스큐트하고

import pymysql

db = pymysql.connect(  #db에 접속하기 위해 connect메소드를 쓴다.->접속환경설정. url 비번, db명, port
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)

sql = '''
    CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''

# sql_2 = "INSERT INTO `users` (name, email, username, password) VALUES ('Cheon Jihui', 'cheon3281@naver.com', '천지희','12345');"

sql_1 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네 ㅠㅠ', '김태경');"

sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"

# title = input("제목을 적으세요")
# body = input("내용을 적으세요")
# author = input("누구세요?")
# input_data = [title, body, author]

cursor = db.cursor()
# cursor.execute(sql_3, input_data)
# db.commit()
# db.close()

# cursor.execute(sql)

# cursor.execute(sql_1)
# cursor.execute(sql_2)
# db.commit()
# db.close()

 # db인스턴스 생성. 쿼리문을 날리기위해 cursor메소드를 실행.
cursor.execute('SELECT * FROM topic;') #excute 메소드 안에 인자값을 쿼리문으로 받음.
# cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall() # fetchall로 조회해서 쿼리문을 가져옴. return값으로 users를 받음.

print(users)