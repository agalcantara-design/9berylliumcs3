class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.__points_scored = 0
    def score_points(self, points):
        self.__points_scored += points
        print(f"{self.name} scored {points} points! Total points: {self.__points_scored}")
    def get_stats(self):
        return f"Player: {self.name}, Position: {self.position}, Points Scored: {self.__points_scored} pts"

class Teams:
    def __init__(self, name, players, coach, championships=0):
        self.name = name
        self.players = players
        self.__coach = coach
        self.__championships = championships
        self.roster = []  # List to hold Player objects
    def recruit_player(self, position):
        self.players += 1
        print(f"{self.name} recruited a new {position}. Roster size is now {self.players}.")
    def win_championship(self):
        self.__championships += 1
        print(f"{self.name} won a championship! Total championships: {self.__championships}")
    def change_coach(self, new_coach):
        if new_coach and isinstance(new_coach, str):
            self.__coach = new_coach
            print(f"{self.name} has a new coach: {self.__coach}")
        else:
            print("Invalid coach name. Please provide a valid string.")
    def get_team_summary(self):
        return f"Team: {self.name}, Players: {self.players}, Coach: {self.__coach}, Championships: {self.__championships}"
    def add_player(self, player):
        self.roster.append(player)
        print(f"{player.name} has been added to {self.name}'s roster.")
    def list_roster(self):
        print(f"Roster for {self.name}:")
        for player in self.roster:
            print(f" - {player.name} ({player.position})")
if __name__ == "__main__":
    Lakers = Teams("Lakers", 12, "JJ Redick", 17)
    p1 = Player("LeBron James", "Forward")
    p2 = Player("Austin Reaves", "Guard")
    p3 = Player("Rui Hachimura", "Forward")

    print("--- BEFORE RELATIONSHIP ---")
    print(Lakers.get_team_summary())
    print("Roster is currently empty:", Lakers.roster)
 
    print("\n--- BUILDING RELATIONSHIP ---")
    Lakers.add_player(p1)
    Lakers.add_player(p2)
    Lakers.add_player(p3)
 
    p1.score_points(28)
    p2.score_points(15)
 
    print("\n--- AFTER RELATIONSHIP ---")
    print(Lakers.get_team_summary())
    print("Related object(s):")
    Lakers.list_roster()