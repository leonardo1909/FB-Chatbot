# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# from decouple import config

# from src.config import config as conf
# from src.api.hello import configure_api


# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}:5432/{config("DB_NAME")}'
# db = SQLAlchemy()


# def create_app():
#     app = Flask('api-authenticator')

#     app.config.from_object(
#         {
#             'FLASK_ENV': 'development',
#             'DEBUG': True
#         }
#     )

#     db.init_app(app)

#     configure_api(app)

#     return app
