class Config(object):
    pass

class ProdConfig(Config):
    SECRET_KEY = "dc85edf0ae0905fcf4234feba4679f5f9e8a0696751b10d3"
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS=False
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Frankline@localhost/maps_db"
    SECRET_KEY = "dc85edf0ae0905fcf4234feba4679f5f9e8a0696751b10d3"
    SQLALCHEMY_TRACK_MODIFICATIONS=True