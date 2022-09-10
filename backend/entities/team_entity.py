class team_entity():
    def __init__(self, name, date_registered, group) -> None:
        self.name = name
        self.date_registered = date_registered
        self.group = group

    def json(self):
        return {"name": self.name, "date_registered": self.date_registered, "group": self.group}

    def __repr__(self):
        return f"{self.name}"
    