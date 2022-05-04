from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.schema import MetaData, Table
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.util.langhelpers import hybridproperty
from src.settings import DATABASE_CONNECTION_STRING

Base = declarative_base()


def db_connect() -> Engine:
    """
    Performs database connection using database settings from settings.py
    """
    return create_engine(DATABASE_CONNECTION_STRING, echo=False)  # NOTE: Set `echo=True` to print SQL


def create_table(engine: Engine) -> None:
    """
    Creates database table
    """
    Base.metadata.create_all(engine)


metadata = MetaData(bind=db_connect())


class Price(Base):
    """
    Reflect Price database table using metadata from database
    """
    __table__ = Table('price', metadata, autoload=True)


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (UniqueConstraint('quantity', 'url'),)

    id = Column(Integer, primary_key=True)
    platform = Column(String(), nullable=False)

    name = Column(String(), index=True, nullable=False)
    url = Column(String(), nullable=False)

    brand = Column(String(), nullable=True, default=None)
    style = Column(String(), nullable=True, default=None)
    origin = Column(String(), nullable=True, default=None)

    abv = Column(Float(), nullable=True, default=None)
    volume = Column(Integer(), nullable=True, default=None)
    quantity = Column(Integer(), nullable=False)

    image_url = Column(String(), nullable=True, default=None)

    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    last_price = column_property(
        select([Price.price]).
        where(Price.product_id == id).
        order_by(Price.id.desc()).
        limit(1).  # NOTE: Limit this as 1 to prevent `CardinalityViolation: more than one row returned by a subquery used as an expression`
        as_scalar(),
    )

    @hybridproperty
    def price_per_quantity(self) -> float:
        return self.last_price / self.quantity

    def __repr__(self) -> str:
        return f'Product({self.name}, platform={self.platform})'
