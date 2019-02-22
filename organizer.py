import random
import groups

class Organizer():
    def __init__(self, count):
        self.count = count
        self.attendees = []

    def generate_attendees(self):
        for i in range(0, self.count):
            id = self.generate_id(i)
            self.attendees.append((id, self.generate_score()))

    def generate_id(self, index):
        return "a" + str(index)

    def generate_score(self):
        return random.randrange(101)



def main():
    team = groups.Groups()
    chippy = Organizer(team.count)
    chippy.generate_attendees()
    sorted_list = sorted(chippy.attendees, key=lambda x: x[1])
    print(sorted_list)

if __name__ == '__main__':
    main()
