import json

class DB:
    def __init__(self):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        try:
            with open('db.json', 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open('db.json', 'w') as f:
                json.dump(self.db, f, indent=4)
    
    def checkin(self,user_id):
        self.db['users'][user_id]={'til':'uz','obuna':False}