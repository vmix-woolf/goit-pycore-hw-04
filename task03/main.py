from visualization import parse_directory
import sys 

def main():
    if len(sys.argv) > 1:
        pathname = sys.argv[1]
        parse_directory(pathname, True)  # True or False: recursive or not
    else:
        print(f"No directory to be parsed")

if __name__ == "__main__":
    main()
