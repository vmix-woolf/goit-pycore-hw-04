import pathlib


def get_cats_info(filename):
    '''Reads the file and collects the info about each cat
    ARGS: 
        filename with the info about cats
    RETURNS:
        The list of dictionaries with classified info about cats
    '''
    current_dir = pathlib.Path(__file__).parent
    try:
        with open(current_dir / filename, 'r', encoding='utf-8') as fh:
            cats = []
            cat = {}
            while True:
                content = fh.readline()
                if not content:
                    break
                line = content.split(',')
                cat['id'] = line[0]
                cat['name'] = line[1]
                cat['age'] = line[2].strip()
                cats.append(cat)
            
        return cats    
    except FileNotFoundError:
        print(f"Error: File not found")


print(get_cats_info('cats.txt'))
