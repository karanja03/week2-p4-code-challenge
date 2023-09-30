from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.String, primary_key=True)
    name=db.Column(db.String, nullable=False)
    super_name=db.column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    
    def __repr__(self):
        return f'{self.name} {self.super_name} {self.created_at} {self.updated_at}'
        
        
class Hero_Powers(db.Model):
    __tablename__='hero_powers'
    
    id = db.Column(db.String, primary_key=True)
    strength=db.Column(db.String, nullable=False)
    hero_id=db.column(db.Integer, nullable=False)
    power_id=db.column(db.Integer, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __repr__(self):
        return f'{self.strength} {self.hero_id} {self.power_id} {self.created_at} {self.updated_at}'

    

class Powers(db.Model):
    __tablename__='powers'
    
    id = db.Column(db.String, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'{self.name} {self.description}  {self.created_at} {self.updated_at}'


    


# add any models you may need. 