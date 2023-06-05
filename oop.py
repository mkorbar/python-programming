"""
- variables
- list and dictionaries
- function
"""


class SportsPerson():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def eat_pasta(self, plate_size_kg):
        self.weight_kg += plate_size_kg

    def workout(self):
        self.weight_kg -= 0.5

    def print_weight(self):
        print(self.weight_kg)

    def print_weight_in_lbs(self):
        print(self.weight_kg * 2.204)

    def __add__(self, other):
        return self.weight_kg + other.weight_kg


class BasketballPlayer(SportsPerson):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __eq__(self, other):
        return self.points == other.points


class FootballPlayer(SportsPerson):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def __eq__(self, other):
        return self.goals == other.goals


def kg_to_lbs(kg):
    return kg * 2.204


lebron = BasketballPlayer(first_name="Lebron",
                          last_name="James",
                          height_cm=203,
                          weight_kg=113,
                          points=123,
                          rebounds=38.3,
                          assists=7.4
                          )

kev_dur = BasketballPlayer(first_name="Kevin",
                           last_name="Durant",
                           height_cm=210,
                           weight_kg=108,
                           points=123,
                           rebounds=68.3,
                           assists=8.4
                           )

####

ronaldo = FootballPlayer(
    first_name="Christiano",
    last_name="Ronaldo",
    height_cm=184,
    weight_kg=74,
    goals=123,
    yellow_cards=23,
    red_cards=1
)

messi = FootballPlayer(
    first_name="Lionel",
    last_name="Messi",
    height_cm=196,
    weight_kg=23,
    goals=253,
    yellow_cards=53,
    red_cards=5
)

print(f"{lebron.first_name} {lebron.last_name}'s weight: {lebron.weight_kg}")

lebron.eat_pasta(4)
lebron.workout()

lebron.print_weight()
lebron.print_weight_in_lbs()

print(f"{lebron.first_name} {lebron.last_name}'s weight: {lebron.weight_kg}")


print(f"{messi.first_name} {messi.last_name}'s weight: {messi.weight_kg}")
print(f"{ronaldo.first_name} {ronaldo.last_name}'s weight: {ronaldo.weight_kg}")



"".split()