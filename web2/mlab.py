import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds113640.mlab.com:13640/movies

host = "ds113640.mlab.com"
port = 13640
db_name = "movies"
user_name = "admin"
password = "admin1"

#connect data
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())