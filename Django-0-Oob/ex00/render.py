import sys
import os

def generateHTML(output, name):
    with open(f"{name}.html", "w") as f:
        f.write(output)

def parseTemplate(templateFile, dictionnary):
    with open(templateFile, "r") as f:
        content = f.read()
        try:
            result = content.format(**dictionnary)
            return result
        except KeyError as e:
            print(f"Missing key: {e}")
            return None
        
def parseSettings(settingsFile):
    with open(settingsFile, "r") as f:
        content = f.read()
        dictionnary = {}
        exec(content, dictionnary)
        dictionnary.pop("__builtins__", None)
    return dictionnary

def main():
    if (len(sys.argv) == 2):
        name, ext = os.path.splitext(sys.argv[1])
        if (ext == ".template"):
            if (os.path.exists(sys.argv[1])):
                if (os.path.exists("./settings.py")):
                    settingsDict = parseSettings("./settings.py")
                    parsed = parseTemplate(sys.argv[1], settingsDict)
                    if parsed is not None:
                        generateHTML(parsed, name)
                else:
                    print("settings.py not found.")
            else:
                print("File not found.")
        else:
            print("Wrong file extension.")
    else:
        print("Wrong number of arguments")
            

if __name__ == "__main__":
    main()