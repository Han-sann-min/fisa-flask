from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# app.py 인곳을 입구로 찾음
# python 은 main 함수가 따로 없기 때문에 파일 명을 구분자로 확인
# 또는 FLASK_APP 이라는 환경변수의 이름을 파일명으로 변경한다.
# set FLASK_APP = ???
# 맥북음 export FLASK_APP = ??
# wsgi.py 에 직접 키 = 밸류 로 여러 환경 변수들을 기입한다. 

import config
db = SQLAlchemy()
migrate = Migrate()


def create_app(): # 어플리케이션 팩토리
    test = Flask(__name__)
    
    # ORM 
    test.config.from_object(config)
    db.init_app(test)
    migrate.init_app(test, db)
    
    
    #블루 프린트
    from .views import main_views # views 폴더 밑에 main_views 가져옴
    test.register_blueprint(main_views.bp)
    
    #블루 프린트
    from .views import board_views # views 폴더 밑에 main_views 가져옴
    test.register_blueprint(board_views.board)

    return test