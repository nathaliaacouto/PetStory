import json

class Model(object):
    def read():
        with open("data.json", "r", encoding="utf-8") as db:
            json_data = json.loads(db.read())
            return json_data

    def create(data: dict):
        json_data = Model.read()
        with open("data.json", "w", encoding="utf-8") as db:
            json_data["queue"].append(data)
            json.dump(json_data, db, ensure_ascii=False, indent=4)

    def delete(data: dict):
        json_data = Model.read()
        updated_json_data = [entry for entry in json_data['queue'] if entry.get("dog") != data["dog"]]
        json_data['queue'] = updated_json_data
        with open("data.json", "w", encoding="utf-8") as db:
            json.dump(updated_json_data, db, ensure_ascii=False, indent=4)