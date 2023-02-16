

from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Save Method  we are now creating a new User to add to a dojo
#we add dojo id as an attribute because we are joining tables and data together
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
        #result = connectToMySQL('dojos_and_ninjas').query_db(query,data)