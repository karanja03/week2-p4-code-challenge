from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Heroes(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.String(60), primary_key=True)
    name=db.Column(db.String(60), nullable=False)
    super_name=db.Column(db.String(60), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    
    def __repr__(self):
        return f'{self.name} {self.super_name} {self.created_at} {self.updated_at}'
        
        
class Heroes_Powers(db.Model):
    __tablename__='heroes_powers'
    
    id = db.Column(db.String(60), primary_key=True)
    strength=db.Column(db.String(60), nullable=False)
    hero_id = db.Column(
        db.Integer, db.ForeignKey("heroes.id"), nullable=False
    )

    heroes = db.relationship(
        "Heroes", backref=db.backref("heroes_powers", lazy=True)
    )

    power_id = db.Column(
        db.Integer, db.ForeignKey("powers.id"), nullable=False
    )
    
    power= db.relationship("Powers", backref=db.backref("heroes_powers", lazy=True))

    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __repr__(self):
        return f'{self.strength} {self.hero_id} {self.power_id} {self.created_at} {self.updated_at}'

    

class Powers(db.Model):
    __tablename__='powers'
    
    id = db.Column(db.String(60), primary_key=True)
    name=db.Column(db.String(60), nullable=False)
    description=db.Column(db.String(60), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'{self.name} {self.description}  {self.created_at} {self.updated_at}'


    


# add any models you may need. 