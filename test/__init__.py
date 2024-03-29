from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))


# app.py 인곳을 입구로 찾음
# python 은 main 함수가 따로 없기 때문에 파일 명을 구분자로 확인
# 또는 FLASK_APP 이라는 환경변수의 이름을 파일명으로 변경한다.
# set FLASK_APP = ???
# 맥북음 export FLASK_APP = ??
# wsgi.py 에 직접 키 = 밸류 로 여러 환경 변수들을 기입한다. 


# db = SQLAlchemy()
migrate = Migrate()


def create_app(): # 어플리케이션 팩토리
    test = Flask(__name__)
    test.config.from_object(config)
    
    # ORM 
    db.init_app(test)
    migrate.init_app(test, db)
    
    if test.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(test, db, render_as_batch=True)
    else:
        migrate.init_app(test, db)
    #블루 프린트
    from .views import main_views # views 폴더 밑에 main_views 가져옴
    test.register_blueprint(main_views.bp)
    
    #블루 프린트
    from .views import board_views # views 폴더 밑에 main_views 가져옴
    test.register_blueprint(board_views.board)

    from .views import answer_views # views 폴더 밑에 main_views 가져옴
    test.register_blueprint(answer_views.answer)

    from .filters import format_datetime
    test.jinja_env.filters['date_time'] = format_datetime

    from .views import auth_views
    test.register_blueprint(auth_views.auth)
    

    return test