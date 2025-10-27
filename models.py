from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Edital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    orgao = db.Column(db.String(200), nullable=False)
    modalidade = db.Column(db.String(50), nullable=False)
    objeto = db.Column(db.Text, nullable=False)
    valor_estimado = db.Column(db.String(50))
    data_abertura = db.Column(db.String(20), nullable=False)
    hora_abertura = db.Column(db.String(10), nullable=False)
    local_abertura = db.Column(db.Text)
    endereco_retirada = db.Column(db.Text)
    informacoes_adicionais = db.Column(db.Text)
    arquivo_anexo = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Edital {self.numero}>'
