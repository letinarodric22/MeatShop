# app.py
from flask import Flask, render_template, redirect, url_for
from form import MeatProductForm
from database import MeatProduct, session, init_db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# @app.before_first_request
# def create_tables():
#     init_db()

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = MeatProductForm()
    if form.validate_on_submit():
        new_product = MeatProduct(name=form.name.data, price=form.price.data)
        session.add(new_product)
        session.commit()
        return redirect(url_for('product_list'))
    return render_template('add_product.html', form=form)

@app.route('/products')
def product_list():
    products = session.query(MeatProduct).all()
    return render_template('product_list.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
