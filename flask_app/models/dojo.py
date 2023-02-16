from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja
#the dot notation means you're in the same file as teh class...in this case we're in the file with the ninja class


#next time insert db variable so you don't have to spell out the database name...avoid spelling errors
#next insert above line 9...db = "dojos_and_ninjas"
#and when you have to list the name of your databse you would put cls.db

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#READ ALL METHOD
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

#CREATE METHOD
    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        #we say result and not result(s) because this renders an ID...in the read all method we used result(s) because we were creating an empty list
        return result


#READ MEthod (1)
#
    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        #to see that teh data being passed is a dictionary
        print(results)
        
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo