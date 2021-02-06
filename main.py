players = list()
lineup_card = [None] * 10

file_to_save = "players.txt"

def save_to_file():
    with open(file_to_save, "w") as fp:
        for player in players:
            fp.write(f"{player[0]}\t{player[1]}\t{player[2]}\n")

def read_from_file():
    global players
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

def add_player():
    global players
    while True:
        print("Enter 'Q' to stop enter player." )

        jersey_number = input("\tJersey number: ")
        if jersey_number == "Q":
            break
        name = input("\tPlayer name: ")
        position = input("\tEnter field position: ")

        players.append([jersey_number, name, position])

def print_roaster():
    print("\t##\tName\t\tPosition")
    for player in players:
        print(f"\t{player[0]}\t{player[1]}\t{player[2]}")

    print(f"\n\t\tTotal {len(players)} players")

def delete_a_player():
    global players

    jersey_number = input("Enter player jersey number to delete: ")

    for indx, player in enumerate(players):
        if player[0] == jersey_number:
            del players[indx]
            print(f"{player[1]} deleted")
            break
    print(f"No jersey number {jersey_number} found")

def update_a_player():
    jersey_number = input("Enter player jersey number to update: ")
    name = input("Enter player name: ")
    position = input("Enter player position: ")

    for indx, player in enumerate(players):
        if player[0] == jersey_number:
            player[1] = name
            player[2] = position
            print(f"{player[1]} updated")
            break
    print(f"No jersey number {jersey_number} found") 

def get_name_from_jersey_number(jersey_number):
    for player in players:
        if player[0] == jersey_number:
            return player[1]
    return None

def create_line_up():
    global lineup_card
    for order, _ in enumerate(lineup_card):
        jersey_number = input(f"Enter order {order+1} jersey number: ")
        lineup_card[order] = get_name_from_jersey_number(jersey_number)

def print_line_up():
    for order, name in enumerate(lineup_card):
        print(f"#{order+1}: {name}")

if __name__ == "__main__":
    read_from_file()

    while True:
        print_menu()

        answer = input("Enter your action number: ").upper()
        if answer == 'Q':
            break

        if answer == 'A':
            add_player()
            save_to_file()

        if answer == 'L':
            print_roaster()

        if answer == 'D':
            delete_a_player()
            save_to_file()

        if answer == 'U':
            update_a_player()
            save_to_file()

        if answer == "C":
            create_line_up()

        if answer == "P":
            print_line_up()