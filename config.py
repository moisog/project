class Config:
    SECRET_KEY = 'adsi'

class  DevelopmentConfig(Config):
    #userpass = 'mysql://root:@'
    #basedir = '127.0.0.1'
    #dbname = '/project_web'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
