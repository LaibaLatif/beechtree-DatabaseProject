from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client.BeechTree  # Database

# Collections
customer_collection = db.Customer  # Customer Collection
jewelry_collection = db.Jewelry  # Jewelry Collection
unstitch_collection = db.UnstitchCollection  # Unstitch Collection
cushion_collection = db.CushionCollection  # Cushion Collection
arts_collection = db.ArtsCollection  # Arts Collection
scarfs_collection = db.ScarfsCollection  # Scarfs Collection
campaigns_collection = db.CampaignsCollection  # Campaigns Collection
stitched_collection = db.StitchedCollection  # Stitched Collection

# Helper function to convert ObjectId to string
def convert_object_id(data):
    for item in data:
        item['_id'] = str(item['_id'])

# Index routes
@app.route('/')
def index():
    return render_template('index.html')

# customer routes
@app.route('/customer')
def customers():
    customers = list(customer_collection.find())
    convert_object_id(customers)
    return render_template('customer.html', customers=customers)

#jewelry routes
@app.route('/jewelry')
def jewelry():
    jewelry_items = list(jewelry_collection.find())
    convert_object_id(jewelry_items)
    return render_template('jewelry.html', jewelry=jewelry_items)

#unstitch routes
@app.route('/unstitch')
def unstitch():
    unstitch_items = list(unstitch_collection.find())
    convert_object_id(unstitch_items)
    return render_template('unstitch.html', unstitch=unstitch_items)

#cushions routes
@app.route('/cushions')
def cushions():
    cushion_items = list(cushion_collection.find())
    convert_object_id(cushion_items)
    return render_template('cushions.html', cushions=cushion_items)

# arts routes
@app.route('/arts')
def arts():
    arts_items = list(arts_collection.find())
    convert_object_id(arts_items)
    return render_template('arts.html', arts=arts_items)

#scarfs routes
@app.route('/scarfs')
def scarfs():
    scarfs_items = list(scarfs_collection.find())
    convert_object_id(scarfs_items)
    return render_template('scarfs.html', scarfs=scarfs_items)

#campaign routes
@app.route('/campaigns')
def campaigns():
    campaigns_items = list(campaigns_collection.find())
    convert_object_id(campaigns_items)
    return render_template('campaigns.html', campaigns=campaigns_items)

# stitched routes
@app.route('/stitched')
def stitched():
    stitched_items = list(stitched_collection.find())
    convert_object_id(stitched_items)
    return render_template('stitched.html', stitched=stitched_items)


# Customer routes
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        customer_data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form['address']
            }
        customer_collection.insert_one(customer_data)
        return redirect(url_for('customers'))
    return render_template('add_customer.html')

@app.route('/edit_customer/<id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = customer_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form['address']
        }
        customer_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('customers'))
    
    customer['_id'] = str(customer['_id'])
    return render_template('edit_customer.html', customer=customer)

@app.route('/delete_customer/<id>', methods=['POST'])
def delete_customer(id):
    customer_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('customers'))

# Jewelry routes
@app.route('/add_jewelry', methods=['GET', 'POST'])
def add_jewelry():
    if request.method == 'POST':
        jewelry_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        jewelry_collection.insert_one(jewelry_data)
        return redirect(url_for('jewelry'))
    return render_template('add_jewelry.html')

@app.route('/edit_jewelry/<id>', methods=['GET', 'POST'])
def edit_jewelry(id):
    jewelry = jewelry_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        jewelry_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('jewelry'))
    
    jewelry['_id'] = str(jewelry['_id'])
    return render_template('edit_jewelry.html', jewelry=jewelry)

@app.route('/delete_jewelry/<id>', methods=['POST'])
def delete_jewelry(id):
    jewelry_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('jewelry'))

# Unstitch Collection routes
@app.route('/add_unstitch', methods=['GET', 'POST'])
def add_unstitch():
    if request.method == 'POST':
        unstitch_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
        }
        unstitch_collection.insert_one(unstitch_data)
        return redirect(url_for('unstitch'))
    return render_template('add_unstitch.html')

@app.route('/edit_unstitch/<id>', methods=['GET', 'POST'])
def edit_unstitch(id):
    unstitch = unstitch_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
        }
        unstitch_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('unstitch'))
    
    unstitch['_id'] = str(unstitch['_id'])
    return render_template('edit_unstitch.html', unstitch=unstitch)

@app.route('/delete_unstitch/<id>', methods=['POST'])
def delete_unstitch(id):
    unstitch_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('unstitch'))

# Cushion Collection routes
@app.route('/add_cushions', methods=['GET', 'POST'])
def add_cushions():
    if request.method == 'POST':
        cushion_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        cushion_collection.insert_one(cushion_data)
        return redirect(url_for('cushions'))
    return render_template('add_cushions.html')

@app.route('/edit_cushions/<id>', methods=['GET', 'POST'])
def edit_cushions(id):
    cushion = cushion_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        cushion_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('cushions'))
    
    cushion['_id'] = str(cushion['_id'])
    return render_template('edit_cushions.html', cushion=cushion)

@app.route('/delete_cushions/<id>', methods=['POST'])
def delete_cushions(id):
    cushion_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('cushions'))

# Arts Collection routes
@app.route('/add_arts', methods=['GET', 'POST'])
def add_arts():
    if request.method == 'POST':
        arts_data = {
            "artist": request.form['artist'],
            "title": request.form['title'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        arts_collection.insert_one(arts_data)
        return redirect(url_for('arts'))
    return render_template('add_arts.html')

@app.route('/edit_arts/<id>', methods=['GET', 'POST'])
def edit_arts(id):
    arts = arts_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "artist": request.form['artist'],
            "title": request.form['title'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        arts_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('arts'))
    
    arts['_id'] = str(arts['_id'])
    return render_template('edit_arts.html', arts=arts)

@app.route('/delete_arts/<id>', methods=['POST'])
def delete_arts(id):
    arts_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('arts'))

# Scarfs Collection routes
@app.route('/add_scarf', methods=['GET', 'POST'])
def add_scarf():
    if request.method == 'POST':
        scarf_data = {
            "product_id": request.form['product_id'],
            "color": request.form['color'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        scarfs_collection.insert_one(scarf_data)
        return redirect(url_for('scarfs'))
    return render_template('add_scarf.html')

@app.route('/edit_scarf/<id>', methods=['GET', 'POST'])
def edit_scarf(id):
    scarf = scarfs_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "product_id": request.form['product_id'],
            "color": request.form['color'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity'])
        }
        scarfs_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('scarfs'))
    
    scarf['_id'] = str(scarf['_id'])
    return render_template('edit_scarf.html', scarf=scarf)

@app.route('/delete_scarf/<id>', methods=['POST'])
def delete_scarf(id):
    scarfs_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('scarfs'))

# Campaigns Collection routes
@app.route('/add_campaign', methods=['GET', 'POST'])
def add_campaign():
    if request.method == 'POST':
        campaign_data = {
            "name": request.form['name'],
            "goal_amount": float(request.form['goal_amount']),
            "current_amount": float(request.form['current_amount']),
            "deadline": request.form['deadline']
        }
        campaigns_collection.insert_one(campaign_data)
        return redirect(url_for('campaigns'))
    return render_template('add_campaign.html')

@app.route('/edit_campaign/<id>', methods=['GET', 'POST'])
def edit_campaign(id):
    campaign = campaigns_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "goal_amount": float(request.form['goal_amount']),
            "current_amount": float(request.form['current_amount']),
            "deadline": request.form['deadline']
        }
        campaigns_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('campaigns'))
    
    campaign['_id'] = str(campaign['_id'])
    return render_template('edit_campaign.html', campaign=campaign)

@app.route('/delete_campaign/<id>', methods=['POST'])
def delete_campaign(id):
    campaigns_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('campaigns'))

# Stitched Collection routes
@app.route('/add_stitched', methods=['GET', 'POST'])
def add_stitched():
    if request.method == 'POST':
        stitched_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
        }
        stitched_collection.insert_one(stitched_data)
        return redirect(url_for('stitched'))
    return render_template('add_stitched.html')

@app.route('/edit_stitched/<id>', methods=['GET', 'POST'])
def edit_stitched(id):
    stitched = stitched_collection.find_one({"_id": ObjectId(id)})
    
    if request.method == 'POST':
        updated_data = {
            "product_id": request.form['product_id'],
            "name": request.form['name'],
            "price": float(request.form['price']),
            "quantity": int(request.form['quantity']),
        }
        stitched_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return redirect(url_for('stitched'))
    
    stitched['_id'] = str(stitched['_id'])
    return render_template('edit_stitched.html', stitched=stitched)

@app.route('/delete_stitched/<id>', methods=['POST'])
def delete_stitched(id):
    stitched_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('stitched'))

# About us
@app.route('/about')
def about_us():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run(debug=True)

###



