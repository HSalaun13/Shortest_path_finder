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

    return distance


def display_map(map, row, column):
    """Display the map and the current location of the player."""

    row_index = 0

    for map_row in map:
        column_index = 0
        display_line = ""

        for cell in map_row:
            if row_index == row and column_index == column:
                display_line = display_line + "P "
            else:
                display_line = display_line + cell + " "

            column_index = column_index + 1

        print(display_line)
        row_index = row_index + 1


def is_valid_move(row, column):
    """Check if the selected position is inside the map."""

    if row >= 0 and row <= 3:
        if column >= 0 and column <= 4:
            return True

    return False


def good_pos(row, column, map):
    """Check if the selected position is good or has an obstacle."""

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


def is_valid_direction(direction):
    """Check if the direction entered by the player is valid."""

    if direction == "up" or direction == "down":
        return True

    if direction == "left" or direction == "right":
        return True

    return False


def count_moves(movement_history):
    """Count the number of movements made by the player."""

    number_of_moves = 0

    for direction in movement_history:
        number_of_moves = number_of_moves + 1

    return number_of_moves


def display_history(movement_history):
    """Display all the movements made by the player."""

    print("Movement history:")

    if movement_history == []:
        print("No movement yet.")

    else:
        for direction in movement_history:
            print(direction)


def menu():
    """Display the main menu and process the user's choice."""

    choice = ""

    while choice != "2":
        print()
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

    if good_pos(0, 1, map) == True:
        print("good_pos test 1: OK")
    else:
        print("good_pos test 1: ERROR")

    if good_pos(0, 3, map) == False:
        print("good_pos test 2: OK")
    else:
        print("good_pos test 2: ERROR")

    new_row, new_column = player_movement(1, 1, "right")

    if new_row == 1 and new_column == 2:
        print("player_movement test 1: OK")
    else:
        print("player_movement test 1: ERROR")

    new_row, new_column = player_movement(2, 2, "up")

    if new_row == 1 and new_column == 2:
        print("player_movement test 2: OK")
    else:
        print("player_movement test 2: ERROR")

    if is_valid_direction("up") == True:
        print("is_valid_direction test 1: OK")
    else:
        print("is_valid_direction test 1: ERROR")

    if is_valid_direction("hello") == False:
        print("is_valid_direction test 2: OK")
    else:
        print("is_valid_direction test 2: ERROR")

    movement_history = ["right", "down", "left"]

    if count_moves(movement_history) == 3:
        print("count_moves test 1: OK")
    else:
        print("count_moves test 1: ERROR")


def main():
    """Run the shortest path program."""

    row = 0
    column = 0

    dest_row = 3
    dest_col = 4

    movement_history = []

    while row != dest_row or column != dest_col:

        display_map(map, row, column)

        distance = calculate_distance(
            row, column, dest_row, dest_col
        )

        print("Distance to destination:", distance)
        print("Current position:", row, column)
        print("Number of moves:", count_moves(movement_history))

        direction = input(
            "Enter a direction (up, down, left, right): "
        )

        while is_valid_direction(direction) == False:
            print("Invalid direction.")
            direction = input(
                "Enter a direction (up, down, left, right): "
            )

        new_row, new_column = player_movement(
            row, column, direction
        )

        if is_valid_move(new_row, new_column):

            if good_pos(new_row, new_column, map):

                row = new_row
                column = new_column

                movement_history.append(direction)

            else:
                print("There is an obstacle there.")

        else:
            print("This position is outside the map.")

    print()
    display_map(map, row, column)

    print("You reached the destination!")
    print("Total number of moves:", count_moves(movement_history))

    display_history(movement_history)


tests()
