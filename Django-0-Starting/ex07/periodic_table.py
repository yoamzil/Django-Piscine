import sys


def parseFile(file):
    elements = []
    with open(file, "r") as f:
        for line in f:
            elementName, attributes = line.strip().split("=")
            element = {"name": elementName.strip()}
            for pair in attributes.strip().split(","):
                key, value = pair.strip().split(":")
                element[key.strip()] = value.strip()
            elements.append(element)
    return elements


def getRow(number):
    number = int(number)
    if number <= 2:
        return 1
    elif number <= 10:
        return 2
    elif number <= 18:
        return 3
    elif number <= 36:
        return 4
    elif number <= 54:
        return 5
    elif number <= 86:
        return 6
    else:
        return 7


def makeGrid(elements):
    grid = {}
    for element in elements:
        row = getRow(element["number"])
        col = int(element["position"])
        grid[(row, col)] = element
    return grid


def generateHTML(grid):
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Periodic Table</title>
    <style>
        table { border-collapse: collapse; }
        td { vertical-align: top; }
        h4 { margin: 0 0 5px 0; }
        ul { margin: 0; padding-left: 15px; font-size: 12px; }
    </style>
</head>
<body>
<table>
"""
    for row in range(1, 8):
        html += "  <tr>\n"
        for col in range(0, 18):
            if (row, col) in grid:
                element = grid[(row, col)]
                electron_count = element["electron"]
                electron_word = "electron" if electron_count == "1" else "electrons"
                html += '    <td style="border: 1px solid black; padding: 10px;">\n'
                html += f"      <h4>{element['name']}</h4>\n"
                html += "      <ul>\n"
                html += f"        <li>No {element['number']}</li>\n"
                html += f"        <li>{element['small']}</li>\n"
                html += f"        <li>{element['molar']}</li>\n"
                html += f"        <li>{electron_count} {electron_word}</li>\n"
                html += "      </ul>\n"
                html += "    </td>\n"
            else:
                html += "    <td></td>\n"
        html += "  </tr>\n"
    html += "</table>\n</body>\n</html>"

    with open("periodic_table.html", "w") as f:
        f.write(html)


def main():
    if len(sys.argv) != 2:
        print("Please provide a data file as an argument.")
        return
    elements = parseFile(sys.argv[1])
    grid = makeGrid(elements)
    generateHTML(grid)


if __name__ == "__main__":
    main()
