from sqlalchemy import create_engine

import pymysql

class DBConnection():
    def __init__(self):
        self.ip_address = '192.168.50.123'
        self.db_name = 'investing_data'
        self.sq_con = None
        self.py_con = None
        
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_sqlalchemy_connect_ip(self):
        engine = create_engine("mysql+pymysql://admin:"
                    +"big15" # user password
                    +f"@{self.ip_address}:3306/{self.db_name}?charset=utf8"
                    , encoding='utf8')
        self.sq_con = engine.connect()
        return self.sq_con
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_pymysql_connection(self):
        conn = pymysql.connect(host=self.ip_address, user='admin', password='big15'
                            , db=self.db_name, charset='utf8')
        self.py_con = conn
        return self.py_con

class DBConnection_stock():
    def __init__(self):
        self.ip_address = '192.168.50.123'
        self.db_name = 'stock_info'
        self.sq_con = None
        self.py_con = None
        
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_sqlalchemy_connect_ip(self):
        engine = create_engine("mysql+pymysql://admin:"
                    +"big15" # user password
                    +f"@{self.ip_address}:3306/{self.db_name}?charset=utf8"
                    , encoding='utf8')
        self.sq_con = engine.connect()
        return self.sq_con
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_pymysql_connection(self):
        conn = pymysql.connect(host=self.ip_address, user='admin', password='big15'
                            , db=self.db_name, charset='utf8')
        self.py_con = conn
        return self.py_con

class DBConnection_trading():
    def __init__(self):
        self.ip_address = '192.168.50.123'
        self.db_name = 'trading_data'
        self.sq_con = None
        self.py_con = None
        
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_sqlalchemy_connect_ip(self):
        engine = create_engine("mysql+pymysql://admin:"
                    +"big15" # user password
                    +f"@{self.ip_address}:3306/{self.db_name}?charset=utf8"
                    , encoding='utf8')
        self.sq_con = engine.connect()
        return self.sq_con
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_pymysql_connection(self):
        conn = pymysql.connect(host=self.ip_address, user='admin', password='big15'
                            , db=self.db_name, charset='utf8')
        self.py_con = conn
        return self.py_con
    
    
class DBConnection_predict():
    def __init__(self):
        self.ip_address = '192.168.50.123'
        self.db_name = 'predict_data'
        self.sq_con = None
        self.py_con = None
        
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_sqlalchemy_connect_ip(self):
        engine = create_engine("mysql+pymysql://admin:"
                    +"big15" # user password
                    +f"@{self.ip_address}:3306/{self.db_name}?charset=utf8"
                    , encoding='utf8')
        self.sq_con = engine.connect()
        return self.sq_con
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_pymysql_connection(self):
        conn = pymysql.connect(host=self.ip_address, user='admin', password='big15'
                            , db=self.db_name, charset='utf8')
        self.py_con = conn
        return self.py_con

class DBConnection_target():
    def __init__(self):
        self.ip_address = '192.168.50.123'
        self.db_name = 'target_data'
        self.sq_con = None
        self.py_con = None
        
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_sqlalchemy_connect_ip(self):
        engine = create_engine("mysql+pymysql://admin:"
                    +"big15" # user password
                    +f"@{self.ip_address}:3306/{self.db_name}?charset=utf8"
                    , encoding='utf8')
        self.sq_con = engine.connect()
        return self.sq_con
     # mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
    def get_pymysql_connection(self):
        conn = pymysql.connect(host=self.ip_address, user='admin', password='big15'
                            , db=self.db_name, charset='utf8')
        self.py_con = conn
        return self.py_con