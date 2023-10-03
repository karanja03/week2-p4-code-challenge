from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates
# from sqlalchemy_serializer import SerializerMixin
from config import db

# Heroes model
class Heroes(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True, nullable= False)
    name=db.Column(db.String(60), nullable=False)
    super_name=db.Column(db.String(60), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    
    def __repr__(self):
        return f'{self.name} {self.super_name} {self.created_at} {self.updated_at}'
    
    @validates('strength')
    def validate_strength(self, key, value):
        # Add validations for the 'strength' attribute here
        if not value:
            raise ValueError("Strength attribute cannot be empty.")
        if len(value) < 3:
            raise ValueError("Strength must be at least 3 characters long.")
        # Add any other validations you need, e.g., checking allowed values
        return value
        
        
       # heroes_powers model
class Heroes_Powers(db.Model):
    __tablename__='heroes_powers'
    
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    strength=db.Column(db.String(10), nullable=False)
    hero_id = db.Column(
        db.Integer, db.ForeignKey("heroes.id"), nullable=False
    )
    
    # the relationship between the three models

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

    

# powers models
class Powers(db.Model):
    __tablename__='powers'
    
    id = db.Column(db.Integer, primary_key=True, nullable= False)
    name=db.Column(db.String(60), nullable=False)
    description=db.Column(db.String(60), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f'{self.name} {self.description}  {self.created_at} {self.updated_at}'
    
    
    @validates('description')
     
    def validate_description(self, key, value):
        # Add validations for the 'description' 
        if not value:
            raise ValueError("Description cannot be empty.")
        if len(value) < 10:
            raise ValueError("Description must be at least 10 characters long.")
        # Add any other validations you need
        return value


    


# add any models you may need. 