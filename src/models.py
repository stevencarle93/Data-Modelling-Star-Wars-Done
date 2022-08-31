import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "lastname":self.lastname,
            "email":self.email
        }

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return{
            "id":self.id,
            "user_from_id":self.user_from_id,
            "user_to_id":self.user_to_id
        }

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id
        }

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return{
            'id':self.id,
            "comment_text":self.comment_text,
            "author_id":self.author_id,
            "post_id":self.post_id
        }
 
class Mediatype(enum.Enum):
    imagen=1
    video=2
    galeria=3

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column('type', Enum(Mediatype))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return{
            "id":self.id,
            "type":self.type,
            "url":self.url,
            "post_id":self.post_id
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')