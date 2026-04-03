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
    
    if len(sys.argv) ==  2:
        name_list = sys.argv[1].split(',')
        for name in name_list:
            if name.strip() == '':
                continue
            for each in states:
                if name.lower().strip() == each.lower():
                    print(capital_cities[states[each]] + " is the capital of " + each)
                    break
            else:
                for each in capital_cities:
                    if name.lower().strip() == capital_cities[each].lower():
                        abrv = each
                        for each in states:
                            if abrv in states[each]:
                                print(capital_cities[abrv] + " is the capital of " + each)
                        break
                else:
                    print(name.strip() + " is neither a capital city nor a state")
    


if __name__ == '__main__':
    find_capital()
