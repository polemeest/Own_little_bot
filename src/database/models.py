"""
Tables for the database
"""

from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Boolean
from sqlalchemy.orm import relationship
from .db_settings import Base


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    level = Column(Integer)
    nicknames = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=True)
    user = relationship("User", backref=("heroes"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    chat_id = Column(Integer)
    role = Column(String)
    user_id = Column(String)


class CityRegion(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String)
    current_budget = Column(BigInteger)
    income = Column(BigInteger)
    weekly_expenses = Column(BigInteger)


class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    accepted = Column(Boolean, nullable=True)
    votes_for = Column(Integer, nullable=True)
    votes_against = Column(Integer, nullable=True)


