from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from afazer.ext.db import db, Base
from flask_login import UserMixin


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(60))

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)


class Atividade(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship("Pessoa")
    status = Column(String(80))

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()


class Usuario(Base, UserMixin):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))
    tipo_usuario = Column(String(20))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship("Pessoa")

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()



