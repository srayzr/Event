from customtime import Time
from date import Date
from Event import Event
from money import Money
from person import Person

p1 = Person("Name", "Surname", 32, "Female")
d = Date(2023, 8, 14)
d1 = Date(2023,8,16)
t = Time(18, 0, 0)
t1 = Time(20, 0, 0)
m = Money("USD", 10)
m1 = Money("RUB", 700)
event = Event("Meeting", d, t, t1, "Yerevan", m, p1.get_gender())
event.change_location("Abu-dhabi")
event.change_date(d1)
event.change_cost(m1)
event.is_available(p1.gender)
print(event)
