def calcul_dist(x1, y1, x2, y2):
    """Calculate the distance between two points"""
    dist = abs(x2 - x1) + abs(y2 - y1)
    return dist


def menu():
    """Menu display"""
    print("1. Calcul of the distance")
    print("2. Valid position ?")
    print("3. Exit")


def tests():
    """Test Functions."""
    if calcul_dist(0, 0, 3, 4) == 7:
        print("Test 1 --> ok")
    else:
        print("Test 1 --> Error")

    if calcul_dist(1, 1, 4, 2) == 4:
        print("Test 2 --> ok")
    else:
        print("Test 2 --> Error")   


def main():
    """Run the main program."""
    menu()
    
    
    
    
tests()
main()
    