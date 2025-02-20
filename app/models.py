"""
Create All the Models (Tables)
"""
from enum import Enum
from app import db
from sqlalchemy import Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column


class CategoryType(Enum):
    """
    Enum class to define category for the Category
    """
    Men = "Men"
    Women = "Women"
    Kids = "Kids"


class LengthTpe(Enum):
    """
    Enum class to define category for the Top and Bottom
    """
    Long = "Long"
    Short = "Short"


class Category(db.Model):
    """
    Categroy Model represent the categroy (men - women - kids)
    """
    __tablename__ = "Category"
    id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, primary_key=True)
    name: Mapped[CategoryType] = mapped_column(SqlEnum(CategoryType), nullable=False)


class Clothing(db.Model):
    """
    Clothing Model represent high level detail of the cloth
    """
    __tablename__ = "Clothing"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=True, unique=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey(Category.id))
    color: Mapped[str] = mapped_column(String(10), nullable=False)
    company: Mapped[str] = mapped_column(String(10), nullable=False)
    image_url: Mapped[str] = mapped_column(String(10), nullable=False)

    def to_dict(self):
        return {'id': self.id,
                'category_id': self.category_id,
                'color': self.color,
                'company': self.company,
                'image_url': self.image_url
                }

    @classmethod
    def filterSearch(cls, kwargs):
        """
        filtring the search
        :param kwargs: query to filter on
        :return: filtered search qurey
        """
        key, val = kwargs
        print('inside the search method')
        if hasattr(cls, key):
            qury = cls.query.filter(getattr(cls, key) == val)
        return qury

    def __repr__(self):
        return f"Cloth Brand is {self.company}"


class Top(db.Model):
    """
    Top Model reprenst more detail on the top clothes (T-shirts, dress, ertc..)
    """
    __tablename__ = "top_detail"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=True, unique=True)
    clothing_id: Mapped[int] = mapped_column(Integer, ForeignKey(Clothing.id))
    sleeve: Mapped[LengthTpe] = mapped_column(SqlEnum(LengthTpe), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'colth_id': self.clothing_id, 'sleeve': self.sleeve}

    @classmethod
    def filterSearch(cls, kwargs):
        """
        filtring the search
        :param kwargs: query to filter on
        :return: filtered search qurey
        """
        key, val = kwargs
        print('inside the search method')
        if hasattr(cls, key):
            qury = cls.query.filter(getattr(cls, key) == val)
        return qury


class Bottom(db.Model):
    """
    Bottom Model represent more detail on the bottom part of the cloth (Jeans, shorts, etc...)
    """
    __tablename__ = "bottom_detail"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=True, unique=True)
    clothing_id: Mapped[int] = mapped_column(Integer, ForeignKey(Clothing.id))
    length: Mapped[LengthTpe] = mapped_column(SqlEnum(LengthTpe), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'cloth_id': self.clothing_id, 'length': self.length}

    @classmethod
    def filterSearch(cls, kwargs):
        """
        filtring the search
        :param kwargs: query to filter on
        :return: filtered search qurey
        """
        key, val = kwargs
        print('inside the search method')
        if hasattr(cls, key):
            qury = cls.query.filter(getattr(cls, key) == val)
        return qury
