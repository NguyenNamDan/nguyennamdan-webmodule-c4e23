import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249583.mlab.com:49583/nguyennamdanc4e_23

host = "ds249583.mlab.com"
port = 49583
db_name = "nguyennamdanc4e_23"
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