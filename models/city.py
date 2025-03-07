#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    if storage_type == "db":
        places = relationship("Place", cascade="all, delete-orphan",
                              backref="cities")
