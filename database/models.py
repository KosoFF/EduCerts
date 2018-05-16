from database.db import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref

class UserUserRole (Base):
    __tablename__ = 'user_user_role'
    __table_args__ = {'autoload': True}

class UserRole(Base, RoleMixin):
    __tablename__ = 'user_role'
    __table_args__ = {'autoload': True}


class UserAccount(Base, UserMixin):
    __tablename__ = 'user_account'
    __table_args__ = {'autoload': True}
    # Custom User Payload
    roles = relationship('UserRole', secondary='user_user_role',
                         backref=backref('users', lazy='dynamic'))

    documents = relationship("NationalDocument", backref="user")
    def get_security_payload(self):
        return {
            'id': self.account_code,
            'email': self.email,
            'password': self.id
        }

class Certificate(Base):
    __tablename__ = 'certificate'
    __table_args__ = {'autoload': True}

class Organisation(Base):
    __tablename__ = 'organisation'
    __table_args__ = {'autoload': True}

class OrganisationRole(Base):
    __tablename__ = 'organisation_role'
    __table_args__ = {'autoload': True}

class OrganisationType(Base):
    __tablename__ = 'organisation_type'
    __table_args__ = {'autoload': True}

class UserAccountOrganisation(Base):
    __tablename__ = 'user_account_organisation'
    __table_args__ = {'autoload': True}

class UserProfile(Base):
    __tablename__ = 'user_profile'
    __table_args__ = {'autoload': True}

class DocumentType(Base):
    __tablename__ = 'document_type'
    __table_args__ = {'autoload': True}

class NationalDocument(Base):
    __tablename__ = 'national_document'
    __table_args__ = {'autoload': True}


