import json


class Visitor:
    def __init__(
        self,
        full_name,
        age,
        date_of_visit,
        time_of_visit,
        comments,
        name_of_person_who_assisted_the_visitor,
    ):
        self.full_name = full_name
        self.age = age
        self.date_of_visit = date_of_visit
        self.time_of_visit = time_of_visit
        self.comments = comments
        self.name_of_person_who_assisted_the_visitor = (
            name_of_person_who_assisted_the_visitor
        )

    @staticmethod
    def file_name_format(name):
        return "visitor_" + (name.lower()).replace(" ", "_") + ".json"


    def save(self):
        visitor_info = {
            "full_name": self.full_name,
            "age": self.age,
            "date_of_visit": self.date_of_visit,
            "time_of_visit": self.time_of_visit,
            "comments": self.comments,
            "name_of_person_who_assisted_the_visitor": self.name_of_person_who_assisted_the_visitor,
        }
        with open(Visitor.file_name_format(self.full_name), "w+") as file:
            file.write(json.dumps(visitor_info, indent=4))

    @staticmethod
    def load(name):
        assert name == str(name), "Incorrect input given, input should be a full name"
        with open(Visitor.file_name_format(name), "r") as file:
            return Visitor(**json.load(file))
        
