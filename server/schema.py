from app import ma
from config.models import Heroes, Powers, Heroes_Powers
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class HeroesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Heroes

    id = ma.auto_field()
    name = ma.auto_field()
    super_name= ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()



# Create instances of the Restaurant schema for single and multiple objects
hero_schema = HeroesSchema()
heroes_schema = HeroesSchema(many=True)


class PowersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Powers

    id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()


# Create instances of the Pizza schema for single and multiple objects
power_schema = PowersSchema()
powers_schema = PowersSchema(many=True)


class  HeroesPowersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Heroes_Powers

    id = ma.auto_field()
    strength = ma.auto_field()
    power_id = ma.auto_field()
    hero_id = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()


# Create instances of the Pizza schema for single and multiple objects
heroespower_schema = HeroesPowersSchema()
heroespowers_schema = HeroesPowersSchema(many=True)