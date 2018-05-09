from app.database.db import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

class UserUserRole (Base):
    __tablename__ = 'user_user_role'
    __table_args__ = {'autoload': True}

class UserRole(Base):
    __tablename__ = 'user_role'
    __table_args__ = {'autoload': True}


class UserAccount(Base, UserMixin):
    __tablename__ = 'user_account'
    __table_args__ = {'autoload': True}
    # Custom User Payload
    roles = relationship('UserRole', secondary='user_user_role',
                         backref=backref('users', lazy='dynamic'))

    def get_security_payload(self):
        return {
            'id': self.account_code,
            'email': self.email,
            'password': self.password_hash
        }
