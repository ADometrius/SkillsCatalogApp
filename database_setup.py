#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///techSkillsCatalog.db')


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Category(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'name': self.name, 'id': self.id,
                'creator': self.user.name}


class Item(Base):

    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'creator': self.user.name,
        }


class ItemCategory(Base):

    __tablename__ = 'itemcategory'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'name': self.item.name,
            'description': self.item.description,
            'id': self.item.id,
            'creator': self.item.user.name,
        }


DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)

USERS = [User(name='Alex Dometrius', email='adometrius@gmail.com')]

CATEGORIES = [
    Category(name='Data Analysis', user_id=1),
    Category(name='Big Data Tools/Technologies', user_id=1),
    Category(name='Data Visualization', user_id=1),
    Category(name='Front End Development', user_id=1),
    Category(name='Back End Development', user_id=1),
    Category(name='Agile/Scrum/SAFe', user_id=1),
    Category(name='JIRA Project Admin', user_id=1),
]

ITEMS = [
    Item(name='R', 
         description="R is a free software environment for statistical computing and graphics. The R language is wiely used among statisticians and data miners for developing statistical software and data analysis",
         user_id=1),
    Item(name='Python for data analysis',
         description="Similar to R, python is also a widely used tool for data analysis and visualization. It has a variety of libraries Pandas, NumPy, SciKitLearn, MatPlotLib, etc. created to help solve data science problems",
         user_id=1),
    Item(name='Hive',
         description="The Apache Hive data warehouse software facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. Structure can be projected onto data already in storage.",
         user_id=1),
    Item(name='JavaScript',
         description="A front end dynamic language used to manipulate HTML and CSS as well as send API calls",
         user_id=1),
    Item(name='HTML',
         description="HyperText Markup Language, used for setting the structure of your web page",
         user_id=1),
    Item(name='SQL',
         description="A very widely used database manipulation language for creating databases and editing them.",
         user_id=1),
    Item(name='D3', 
         description="D3 (Data-Driven Documents or D3.js) is a JavaScript library for visualizing data using web standards. D3 helps you bring data to life using SVG, Canvas and HTML. D3 combines powerful visualization and interaction techniques with a data-driven approach to DOM manipulation, giving you the full capabilities of modern browsers and the freedom to design the right visual interface for your data.",
         user_id=1),
    Item(name='MongoDB',
         description="MongoDB stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time",
         user_id=1),
    Item(name='SAFe',
         description="The Scaled Agile Framework (SAFe) helps businesses address the significant challenges of developing and delivering enterprise-class software and systems in the shortest sustainable lead time. SAFe synchronizes alignment, collaboration, and delivery for multiple Agile teams.",
         user_id=1),
    Item(name='JIRA',
         description="Jira is an issue tracking product, developed by Atlassian. It provides bug tracking, issue tracking, and project management functions.",
         user_id=1),
    Item(name='CSS',
         description="Cascading Style Sheets are used to style the HTML on a web page.",
         user_id=1),
]

ITEMCATEGORIES = [
    ItemCategory(category_id=1, item_id=1),
    ItemCategory(category_id=1, item_id=2),
    ItemCategory(category_id=2, item_id=3),
    ItemCategory(category_id=2, item_id=4),
    ItemCategory(category_id=3, item_id=5),
    ItemCategory(category_id=3, item_id=6),
    ItemCategory(category_id=4, item_id=7),
    ItemCategory(category_id=4, item_id=8),
    ItemCategory(category_id=5, item_id=9),
    ItemCategory(category_id=5, item_id=10),
    ItemCategory(category_id=6, item_id=11),
    ItemCategory(category_id=6, item_id=1),
    ItemCategory(category_id=7, item_id=2),
    ItemCategory(category_id=7, item_id=3),
]


def addUsers():
    for user in USERS:
        session.add(user)
    session.commit()


def addCategories():
    session.bulk_save_objects(CATEGORIES)
    session.commit()


def addItems():
    session.bulk_save_objects(ITEMS)
    session.commit()


def addItemCategories():
    session.bulk_save_objects(ITEMCATEGORIES)
    session.commit()


if __name__ == '__main__':
    addUsers()
    addCategories()
    addItems()
    addItemCategories()
