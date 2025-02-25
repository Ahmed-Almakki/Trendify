from app import db
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref


class RoleUser(db.Model):
    __tablename__ = "roles_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    fs_uniquifier:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    role = relationship('Role', secondary='roles_users', backref=backref('users', lazy="dynamic"))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(String(255))