from flask import Blueprint
from flask import render_template,request,redirect,flash
mod=Blueprint('api',__name__,template_folder='templates')
from app.api.function import city,cuisines,result

city_id=None
cuisine_id=None
@mod.route('/',methods = ['GET', 'POST'])
def feed():
    if request.method=='POST':
        global city_id
        city_id=city(request.form['place'])
        if city_id is not None:
            return redirect('/cuisine')
        else:
            flash("city not available")
            return redirect('/')
    return render_template('feed.html')


@mod.route('/cuisine',methods = ['GET', 'POST'])
def cuisine():
    data_cuisine=cuisines(city_id)
    length=len(data_cuisine)
    if request.method=='POST':
        global cuisine_id
        cuisine_id= (request.form['my_cuisine_List'])
        data=result(cuisine_id,city_id)
        return render_template("result.html",data=data,length=len(data))
    return render_template('cuisine.html',dat=data_cuisine,length=length)
