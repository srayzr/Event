from person import Person


class Event:
    def __init__(self, name, date, start_time, end_time, location, cost):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.cost = cost

    def __repr__(self):
        return "Event: {}\nDate: {}\nTime: {} - {}\nLocation: {}\nCost: {}".format(
            self.name, self.date, self.start_time, self.end_time, self.location, self.cost
        )

    def change_location(self, new_location):
        self.location = new_location

    @staticmethod
    def is_available(gender):
        if gender == "Male":
            print("Sorry event is not available for you")
        else:
            print("You're welcome")

    def change_date(self, new_date):
        self.date = new_date

    def change_cost(self, new_cost):
        self.cost = new_cost
