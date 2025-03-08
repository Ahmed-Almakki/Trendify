"""
Admin route to delete create and update products to database
"""
import base64
import requests
from flask import Blueprint, request, redirect, jsonify, current_app
from werkzeug.utils import secure_filename
from ..models import Clothing, Top, Bottom
from ..utils.helper import checkCorrectParameter
from ..utils.decorator import role_required

admin = Blueprint('Admin', __name__, template_folder='../template')


@admin.route('/admin', methods=['POST'])
@role_required
def createTable():
    check = False

    if 'company' not in request.form.to_dict().keys():
        return jsonify({'error': "Company missing"}), 404
    elif 'color' not in request.form.to_dict().keys():
        return jsonify({'error': "Color is Missing"}), 404
    elif 'gender' not in request.form.to_dict().keys():
        return jsonify({'error': 'Gender is not Set'}), 404
    elif 'image' not in request.files:
        return jsonify({"error": "You didn't upload file"}), 404

    else:
        from app import db

        color = request.form['color']
        if request.form.get('sleeve'):
            sleeve = request.form['sleeve']
            check = True

        if request.form.get('length'):
            length = request.form['length']

        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "you didn't select file to upload"}), 400
        img_url = uploadImage(file)
        # print(img_url['data']['url'])

        company = request.form['company']
        gender = request.form['gender']
        price = request.form['price']
        count = request.form['count']

        try:

            cloth = Clothing(color=color,
                             company=company, gender=gender, price=price,
                             count=count, image_url=img_url['data']['url']) #dont forget image
            db.session.add(cloth)
            db.session.commit()
            if check:
                top = Top(sleeve=sleeve, clothing_id=cloth.id)
                db.session.add(top)
            else:
                bottom = Bottom(length=length, clothing_id=cloth.id)
                db.session.add(bottom)
            db.session.commit()
            return redirect(request.referrer)
        except Exception as e:
            return jsonify({'error': f'Cannot create Table because of {e}'}), 400


@admin.route('/admin/<int:cloth_id>', methods=['PUT', 'DELETE'])
@role_required
def updateCloth(cloth_id):
    from app import db

    try:
        if request.method == 'PUT':
            holder = list(request.form.to_dict().keys())

            if not request.form.to_dict().keys():
                return jsonify({"error": "Data Doesn't exists"}), 400
            try:
                change = request.form.to_dict()
                if "sleeve" in change:
                    query = Top.update(cloth_id, **change)
                    if 'sleeve' in holder:
                        holder.remove('sleeve')
                if "length" in change:
                    query = Bottom.update(cloth_id, **change)
                    if 'length' in change:
                        holder.remove('length')
                if not checkCorrectParameter(holder, lst=["color", "company", "gender"]): #dont forget image
                    return jsonify({"error": "Wrong paramters Name (Clothing param)"})
                query = Clothing.update(cloth_id, **change)
                db.session.commit()
                return jsonify({"message": "updated successfully"})
            except Exception as e:
                return jsonify({"error": f"could not update due to {e}"}), 400
        else:
            query = db.session.query(Clothing).\
                join(Top, Top.clothing_id == Clothing.id, isouter=True).\
                join(Bottom, Bottom.clothing_id == Clothing.id, isouter=True).\
                filter(Clothing.id == cloth_id).all()
            if query:
                Clothing.query.filter(Clothing.id == cloth_id).delete()
                db.session.commit()
                return jsonify({"message": "sucssuffuly Delete"}), 200
            return jsonify({"error": "Data dosen't exsist in database"}), 404
    except Exception as e:
        return jsonify({"error": f"can't update due to {e}"})


def uploadImage(imageName):
    api_img = current_app.config['IMG_API_KEY']
    url ='https://api.imgbb.com/1/upload'
    imgFile = imageName.read()
    image_base64 = base64.b64encode(imgFile).decode('ascii')
    payload = {
        "key": api_img,
        "image": image_base64
    }
    response = requests.post(url, data=payload)
    return response.json()
    