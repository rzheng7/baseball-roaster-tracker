

file_to_save = "players.txt"

def save_to_file():
    with open(file_to_save, "w") as fp:
        for player in players:
            fp.write(player[0] + "\t" +  player[1] + "\t" + player[2] + "\n")


def read_from_file(players):
    lines = None
    with open(file_to_save, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            players.append(line.rstrip().split("\t"))

def print_menu():
    print("""
    a -> Add new players
    u -> Update a new player
    d -> Delete a player
    l -> List the team roaster
    c -> Create a lineup
    p -> print lineup card
    q -> Quit
    """)

def add_player(players):
    while True:
        print("Enter 'Q' to stop enter player." )

        jersey_number = input("\tJersey number: ")
        if jersey_number == "Q":
            break
        name = input("\tPlayer name: ")
        position = input("\tEnter field position: ")

        players.append([jersey_number, name, position])

def print_roaster(players):
    print("\t##\tName\t\tPosition")
    for player in players:
        print("\t" + player[0] + "\t" + player[1] + "\t" + player[2])

    total = len(players)
    print("\n\t\tTotal " + str(total) + " players")

def delete_a_player(players):

    jersey_number = input("Enter player jersey number to delete: ")

    for indx, player in enumerate(players):
        if player[0] == jersey_number:
            del players[indx]
            print(player[1] + " deleted")
            break
    print("No jersey number " + str(jersey_number) + " found")

def update_a_player(players):
    jersey_number = input("Enter player jersey number to update: ")
    name = input("Enter player name: ")
    position = input("Enter player position: ")

    for indx, player in enumerate(players):
        if player[0] == jersey_number:
            player[1] = name
            player[2] = position
            print(player[1] + " updated")
            break
    print("No jersey number "+ str(jersey_number) + " found")

def get_name_from_jersey_number(jersey_number):
    for player in players:
        if player[0] == jersey_number:
            return player[1]
    return None

def create_line_up(lineup_card):
    position = 0
    for card in lineup_card:
        jersey_number = input("Enter position " + str(position+1) + " jersey number: ")
        lineup_card[position] = get_name_from_jersey_number(jersey_number)
        position += 1

def print_line_up(lineup_card):
    order = 1
    for name in lineup_card:
        print("#" + str(order) + ": " + name)
        order += 1

if __name__ == "__main__":
    players = list()
    lineup_card = [""] * 10
    read_from_file(players)

    while True:
        print_menu()

        answer = input("Enter your action number: ").upper()
        if answer == 'Q':
            break

        if answer == 'A':
            add_player(players)
            save_to_file()

        if answer == 'L':
            print_roaster(players)

        if answer == 'D':
            delete_a_player(players)
            save_to_file()

        if answer == 'U':
            update_a_player(players)
            save_to_file()

        if answer == "C":
            create_line_up(lineup_card)

        if answer == "P":
            print_line_up(lineup_card)