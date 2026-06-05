from local_lib.path import Path

def main():
    Path("Folder").mkdir_p()
    Path("Folder/file.txt").write_text("Hello Worlddddd!")
    print(Path("Folder/file.txt").read_text())

if __name__ == "__main__":
    main()