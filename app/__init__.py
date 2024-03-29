from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')



db = SQLAlchemy(app)
migrate = Migrate(app, db) # A instancia do migrate cuida das migrações pra isso ele recebe a aplicação e o banco


manager = Manager(app) # O manager cuida dos comandos de inicialçiação da aplicação 
manager.add_command('db', MigrateCommand)# Este comando pega os comandos preparados pelo migrate e traz para o app


lm = LoginManager()
lm.init_app(app)

from app.models import tables, form
from app.controllers import default
