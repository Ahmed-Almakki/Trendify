from flask import Blueprint, request, render_template
from ..models import Clothing, Top, Bottom, Category

admin = Blueprint('Admin', __name__)


@admin.route('/admin', methods=['POST'])
def CU_op():
    from app import db
    color = request.form['color']
    sleeve = request.form['sleeve']
    length = request.form['length']
    company = request.form['company']
    gender = request.form['gender']
    category = Category(gender=gender)
    db.session.add(category)
    db.session.commit()

    cloth = Clothing(color=color, company=company, category_id=category.id)
    db.session.add(cloth)
    db.session.commit()

    top = Top(sleeve=sleeve, clothing_id=cloth.id)
    bottom = Bottom(length=length, clothing_id=cloth.id)
    db.session.add(top)
    db.session.add(bottom)

    db.session.commit()
    return render_template("admin.html")

# @admin.route('/admin/<int: cloth_id>', method=['PUT'])
# def updateCloth(cloth_id):
#     cloth_id = Clothing.query.get_or_404(cloth_id)
