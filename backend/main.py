
from flask import request, jsonify
from config import app, db
from models import Contact 



@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all() #get the contact in python 
    #convert to json 
    json_contacts = list(map(lambda x: x.to_json(), contacts)) #for each object in contacts has the to_json function so we ise it.
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    # Get the input from the user and validate that it is not null
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must give a first name, last name, and email"}), 400
    
    # Create a new contact
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    
    try:
        db.session.add(new_contact)
        db.session.commit()  # Commit will add to the db all the things in the session, so always need add & commit
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id) #Find the user in the db that have that user_id 

    if not contact:
        return jsonify({"message": "user not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name) #get function look for the Key and if not found take the second paremeter
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User update"}),  200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    
    contact = Contact.query.get(user_id) #Find the user in the db that have that user_id 

    if not contact:
        return jsonify({"message": "user not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}),  200



if __name__ == "__main__":
    with app.app_context():
        db.create_all() #make sure that the database is created 

    app.run(debug=True)


