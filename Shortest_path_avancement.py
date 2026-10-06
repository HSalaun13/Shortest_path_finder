map = [
    ["S", ".", ".", "#", "."],
    [".", ".", ".", "#", "."],
    ["#", "#", ".", ".", "."],
    [".", ".", ".", ".", "D"]
]


def calculate_distance(row, column, dest_row, dest_col):
    """Calculate the distance to the destination."""
    row_dif = dest_row - row
    col_dif = dest_col - column

    if row_dif < 0:
        row_dif = -row_dif

    if col_dif < 0:
        col_dif = -col_dif

    distance = row_dif + col_dif    

    return dist

def display_map(map):
    """This function display the map and the current location of the player ."""
    for row in map:
        print(row)


def is_valid_move(row, column):
    """This function look if the position we selected is in the map."""
    if row >= 0 and row <= 3:
        if column >= 0 and column <= 4:
            return True
    return False


def good_pos(row, column, map):
    """See if the position selected is good or is there any obstacle."""
    if map[row][column] == "#":
        return False
    else:
        return True


def player_movement(row, column, direction):
    """Calculate the new position according to the direction."""
    new_row = row
    new_column = column

    if direction == "up":
        new_row = row - 1
    elif direction == "down":
        new_row = row + 1
    elif direction == "left":
        new_column = column - 1
    elif direction == "right":
        new_column = column + 1

    return new_row, new_column


def menu():
    """Display the main menu and process the user's choice."""
    print("1. Start")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        main()
    elif choice == "2":
        print("Goodbye.")
    else:
        print("Invalid option.")


def tests():
    """Test the functions of the program."""
    if calculate_distance(0, 0, 3, 4) == 7:
        print("calculate_distance test 1: OK")
    else:
        print("calculate_distance test 1: ERROR")

    if calculate_distance(1, 1, 4, 2) == 4:
        print("calculate_distance test 2: OK")
    else:
        print("calculate_distance test 2: ERROR")

    if is_valid_move(2, 3) == True:
        print("is_valid_move test 1: OK")
    else:
        print("is_valid_move test 1: ERROR")

    if is_valid_move(5, 2) == False:
        print("is_valid_move test 2: OK")
    else:
        print("is_valid_move test 2: ERROR")

    if is_free_position(0, 1, game_map) == True:
        print("is_free_position test 1: OK")
    else:
        print("is_free_position test 1: ERROR")

    if is_free_position(0, 3, game_map) == False:
        print("is_free_position test 2: OK")
    else:
        print("is_free_position test 2: ERROR")

    new_row, new_column = move_player(1, 1, "right")

    if new_row == 1 and new_column == 2:
        print("move_player test 1: OK")
    else:
        print("move_player test 1: ERROR")

    new_row, new_column = move_player(2, 2, "up")

    if new_row == 1 and new_column == 2:
        print("move_player test 2: OK")
    else:
        print("move_player test 2: ERROR")


def main():
    """Run the shortest path program."""
    row = 0
    column = 0

    destination_row = 3
    destination_column = 4

    while row != destination_row or column != destination_column:
        display_map(game_map)

        distance = calculate_distance(
            row, column, destination_row, destination_column
        )

        print("Distance to destination:", distance)
        print("Current position:", row, column)

        direction = input(
            "Enter a direction (up, down, left, right): "
        )

        new_row, new_column = move_player(
            row, column, direction
        )

        if is_valid_move(new_row, new_column):
            if is_free_position(new_row, new_column, game_map):
                game_map[row][column] = "."
                row = new_row
                column = new_column
                game_map[row][column] = "P"
            else:
                print("There is an obstacle there.")
        else:
            print("This position is outside the map.")

    print("You reached the destination!")


tests()
menu()
