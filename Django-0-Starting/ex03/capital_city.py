import sys

def find_capital():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if len(sys.argv) == 2:
        if sys.argv[1] in states:
            abrv = states[sys.argv[1]]
            if abrv in capital_cities:
                print(capital_cities[abrv])
            else:
                print("Unknown state")
        else:
            print("Unknown state")

if __name__ == '__main__':
    find_capital()