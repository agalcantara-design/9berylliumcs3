class Teams: 
    def __init__(self, name, players, coach, championships=0):
        self.name = name
        self.players = players
        self.__coach = coach
        self.__championships = championships

    def recruit_player(self, position):
        self.players += 1
        print(f"{self.name} recruited a new {position}. "
              f"Roster size is now {self.players}.")

    def win_championship(self):
        self.__championships += 1
        print(f"{self.name} won a championship! Total championships: {self.__championships}")

    def change_coach(self, new_coach):
        self.__coach = new_coach
        print(f"{self.name} has a new coach: {self.__coach}")

    def get_team_summary(self):
        return f"Team: {self.name}, Players: {self.players}, Coach: {self.__coach}, Championships: {self.__championships}"

if __name__ == "__main__":
    # Step 6 - Instantiate two independent objects
    team1 = Teams("Lakers", 12, "JJ Redick", 17)
    team2 = Teams("Warriors", 13, "Steve Kerr", 7)
 
    print("--- BEFORE ---")
    print("Object 1:", team1.get_team_summary())
    print("Object 2:", team2.get_team_summary())
 
    # Step 7 - Change only Object 1
    print("\nPerforming actions on Object 1 (Lakers) only...\n")
    team1.recruit_player("center")
    team1.win_championship()
    team1.change_coach("Darvin Ham")
 
    print("\n--- AFTER ---")
    print("Object 1:", team1.get_team_summary())
    print("Object 2:", team2.get_team_summary())