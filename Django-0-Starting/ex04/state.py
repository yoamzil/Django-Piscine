import sys

def find_state():
    states = {
        "Oregon": "OR", "Alabama": "AL",
        "New Jersey": "NJ", "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem", "AL": "Montgomery",
        "NJ": "Trenton", "CO": "Denver"
    }

    if len(sys.argv) == 2:
        inverted = {v: k for k, v in capital_cities.items()}
        if sys.argv[1] in inverted:
            abrv = inverted[sys.argv[1]]
            for state, code in states.items():
                if code == abrv:
                    print(state)
                    break
        else:
            print("Unknown capital city")

if __name__ == '__main__':
	find_state()
