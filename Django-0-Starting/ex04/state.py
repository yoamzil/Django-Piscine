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
        for each in capital_cities:
            if sys.argv[1] in capital_cities[each]:
                abrv = each
                for each in states:
                    if abrv in states[each]:
                        print(each)
                        break
                else:
                    print("Unknown capital city")
                break
        else:
            print("unknown capital city")

if __name__ == '__main__':
	find_capital()
