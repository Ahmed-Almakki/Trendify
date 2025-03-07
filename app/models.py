"""
Create All the Models (Tables)
"""
from enum import Enum
from app import db
from sqlalchemy import Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4, UUID


class CategoryType(Enum):
    """
    Enum class to define category for the Category
    """
    Men = "men"
    Women = "women"


class LengthTpe(Enum):
    """
    Enum class to define category for the Top and Bottom
    """
    Long = "long"
    Short = "short"

class Clothing(db.Model):
    """
    Clothing Model represent high level detail of the cloth
    """
    __tablename__ = "Clothing"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    color: Mapped[str] = mapped_column(String(10), nullable=False)
    company: Mapped[str] = mapped_column(String(10), nullable=False)
    gender: Mapped[str] = mapped_column(SqlEnum(CategoryType), nullable=False)
    price: Mapped[str] = mapped_column(String(20))
    count: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(String(10), nullable=False)

    def to_dict(self):
        return {'id': self.id,
                'gender': self.gender,
                'color': self.color,
                'company': self.company,
                'price': self.price,
                'count': self.count
                # 'image_url': self.image_url
                }

    @classmethod
    def update(cls, id, **kwargs):
        """
        update the tabel
        :param kwargs: dictionary of parameter to update the table
        :return: true if the all dictionary belongs to this class
        """
        instance = cls.query.get(id)
        if not instance:
            return None

        lenghtCheck = 0
        for key, val in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, val)
                lenghtCheck += 1
        if len(kwargs.keys()) == lenghtCheck:
            return True
        return False

    def __repr__(self):
        return f"Cloth Brand is {self.company}"


class Top(db.Model):
    """
    Top Model reprenst more detail on the top clothes (T-shirts, dress, ertc..)
    """
    __tablename__ = "top_detail"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    clothing_id: Mapped[UUID] = mapped_column(ForeignKey(Clothing.id, ondelete='CASCADE'))
    sleeve: Mapped[LengthTpe] = mapped_column(SqlEnum(LengthTpe), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'colth_id': self.clothing_id, 'sleeve': self.sleeve}

    @classmethod
    def filterSearch(cls, **kwargs):
        """
        filtring the search
        :param kwargs: query to filter on
        :return: filtered search qurey
        """
        query = cls.query
        for key, val in kwargs.items():
            if hasattr(cls, key):
                query = query.filter(getattr(cls, key) == val)
        return query

    @classmethod
    def update(cls, id, **kwargs):
        """
        update the tabel
        :param kwargs: dictionary of parameter to update the table
        :return: true if the all dictionary belongs to this class
        """
        instance = cls.query.get(id)
        if not instance:
            return None

        lenghtCheck = 0
        for key, val in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, val)
                lenghtCheck += 1
        # db.session.commit()
        if len(kwargs.keys()) == lenghtCheck:
            return True
        return False


class Bottom(db.Model):
    """
    Bottom Model represent more detail on the bottom part of the cloth (Jeans, shorts, etc...)
    """
    __tablename__ = "bottom_detail"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    clothing_id: Mapped[UUID] = mapped_column(ForeignKey(Clothing.id, ondelete='CASCADE'))
    length: Mapped[LengthTpe] = mapped_column(SqlEnum(LengthTpe), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'cloth_id': self.clothing_id, 'length': self.length}

    @classmethod
    def filterSearch(cls, **kwargs):
        """
        filtring the search
        :param kwargs: query to filter on
        :return: filtered search qurey
        """
        query = cls.query
        for key, val in kwargs.items():
            if hasattr(cls, key):
                query = query.filter(getattr(cls, key) == val)
        return query

    @classmethod
    def update(cls, id, **kwargs):
        """
        update the tabel
        :param kwargs: dictionary of parameter to update the table
        :return: true if the all dictionary belongs to this class
        """
        instance = cls.query.get(id)
        if not instance:
            return None

        lenghtCheck = 0
        for key, val in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, val)
                lenghtCheck += 1
        # db.session.commit()
        if len(kwargs.keys()) == lenghtCheck:
            return True
        return False

