import pathlib


class EmptyListException(Exception):
    '''Raise specific situation when the file is found but it is empty'''


def total_salary(filename: str) -> tuple:
    '''Calculates total salary and average salary for the staff enumerated in the text file\n
    ARGS:
        the name of the text file as a string
    RETURNS:
        tuple with total_salary and average_salary in float format    
    '''
    raw_data = load_data(filename)
    staff = clean_data(raw_data)
    
    total_salary = 0
    number_of_staff = len(staff)
    
    for person in staff:
        total_salary += float(person["salary"])
    
    try:    
        average_salary = total_salary / number_of_staff
    except ZeroDivisionError as e:
        average_salary = 0
        
    return (total_salary, average_salary)


def load_data(filename: str) -> list:
    '''Loads data from the file with names and salaries\n
    ARGS:
        filename where data is saved
    RETURNS:
        list of lines from the file
    '''
    current_dir = pathlib.Path(__file__).parent
    file = current_dir / filename
    try:
        with open(file, 'r', encoding='utf-8') as file_handler:
            raw_data = []
            while True:
                line = file_handler.readline()
                if  line == "" or line == "\n":
                    break
                raw_data.append(line)
            if len(raw_data) == 0:
                raise EmptyListException()
            else:    
                return raw_data
    except IOError:
        print(f"Error: File not found")
        return []
    except EmptyListException:
        print(f"Error: This list is empty")
        return []


def clean_data(raw_data: list) -> list[dict]:
    '''Processes the raw data from the file\n
    ARGS:
        List of lines corresponding to lines from the data file
    RETURNS:
        List of dictionaries with personal info about each member of staff 
    '''
    staff = []
    for person in raw_data:
        stripped = person.strip()
        person_info = stripped.split(',')
        staff_member = {
            "full_name": person_info[0],
            "salary": person_info[1]
        }
        staff.append(staff_member)

    return staff


print(f"Correct file:", format(total_salary("salaries.txt")))
print(f"Missing file:",format(total_salary("missing-file.txt")))
print(f"Empty file:", format(total_salary("empty-file.txt")))