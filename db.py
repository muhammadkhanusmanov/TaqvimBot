import json

class DB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)
    
    def checkin(self,user_id):
        if user_id is not self.db.keys():
            self.db['users'][user_id]={'til':'uz','obuna':False}
    
    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def get(self):
        admin = self.db['admin']['admins']
        obuna = self.db['admin']['obuna']
        return {'admin':admin,'obuna':obuna}
    
    def get_lang(self,user_id):
        return self.db['users'][user_id]['til']
    
    def add_lang(self,user_id,lang):
        self.db['users'][user_id]['til']=lang