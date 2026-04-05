# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
#Exp 6.1: Event Management System


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def register_participant(self, participant):
        self.participants.append(participant)
        print(f"Registered {participant.name} for {self.name}.")

    def show_participants(self):
        print(f"Participants for {self.name}:")
        for p in self.participants:
            print(f"- {p}")

class EventManager:
    def __init__(self):
        self.events = {}

    def create_event(self, name, date):
        self.events[name] = Event(name, date)
        print(f"Event '{name}' created for {date}.")

    def get_event(self, name):
        return self.events.get(name)

def main():
    print(" Event Management System ")
    system = EventManager()
    
    # Create events
    system.create_event("TechFest", "2026-02-15")
    system.create_event("Cultural Night", "2026-01-20")

    # Interactive registration
    tech_fest = system.get_event("TechFest")
    if tech_fest:
        p1 = Participant("Shreyas", "shreyas@example.com")
        p2 = Participant("Trilok", "trilok@example.com")
        tech_fest.register_participant(p1)
        tech_fest.register_participant(p2)
        tech_fest.show_participants()

if __name__ == "__main__":
    main()

