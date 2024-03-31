class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_signifance ):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_signifance = historical_signifance

    def get_location(self):
        pass

class Location:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.events = []

    def add_artwork(self, artwork):
        self.events.append(artwork)

class Event:
    def __init__(self, event_type, duration, location):
        self.event_type = event_type
        self.duration = duration
        self.location = location
        self.artworks = []
        self.visitors = []
        self. guides = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def add_guide(self, guide):
        self.guides.append(guide)

class Visitor:
    def __init__(self, ticket_id, demographics ):
        self.ticket_id = ticket_id
        self.demographics = demographics
        self.tickets = []

    def purchase_ticket(self, event):
        self.tickets.append(event)


class Ticket:
    def __init__(self, event_type, price):
        self.event_type = event_type
        self.price = price

    def calculate_price(self):
        pass

class Guide:
    def __init__(self, guide_id, name, specialization ):
        self.guide_id = guide_id
        self.name = name
        self.specialization = specialization




def add_new_artwork():
    artwork = Artwork("flower board", "Mariam", "14/3", " portrait")

    location = Location("block 3", "temporary")

    location.add_artwork(artwork)

    assert artwork in location.events

def new_exhibition():

    location_of_exhibition = Location(" ART", "Temporary")

    Exhibition2 = Event("Painting", "4 weeks", location_of_exhibition)

    assert Exhibition2.event_type == "Painting"
    assert Exhibition2.location == location_of_exhibition

def tickets_purchase():

    location_of_event=Location("first floor", "temporary")
    Event_of_ticket = Event("ART", "6 hours",location_of_event )

    visitor1 = Visitor("3467","child")

    visitor1.purchase_ticket(Event_of_ticket)

    assert Event_of_ticket in visitor1.tickets

def receipt():

    ticket1 = Ticket(" ART", 45.0)
    ticket2 = Ticket("ART", 45.0)

    visitor1 = Visitor("3435", "Adult")
    visitor1.ticket.extend[ticket1, ticket2]

    total = sum(ticket.price for ticket in visitor1.tickets)

    print(f"total :{total}")

if __name__ == " __main__":
    add_new_artwork()
    new_exhibition()
    tickets_purchase()
    receipt()

