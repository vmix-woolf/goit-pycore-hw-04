import pathlib

def total_salary(filename: str) -> tuple:
    '''Calculates total salary and average salary for the staff enumerated in the text file\n
    ARGS:
        the name of the text file as a string
    RETURNS:
        tuple with total_salary and average_salary in float format    
    '''
    staff = load_data(filename)
    prepared_data = clean_data(staff)
    total_salary = 0
    number_of_staff = len(prepared_data)
    
    for person in prepared_data:
        total_salary += float(person["salary"])
    
    try:    
        average_salary = total_salary / number_of_staff
    except ZeroDivisionError as e:
        average_salary = 0
        
    return (total_salary, average_salary)


def load_data(filename: str) -> list[str]:
    current_dir = pathlib.Path(__file__).parent
    file = current_dir / filename
    try:
        with open(file, 'r', encoding='utf-8') as file_handler:
            staff = []
            while True:
                person = file_handler.readline()
                if  person == "" or person == "\n":
                    break
                staff.append(person)
            if len(staff) == 0:
                raise EmptyListException()
            else:    
                return staff
    except IOError:
        print(f"Error: File not found")
        return []
    except EmptyListException:
        print(f"Error: This list is empty")
        return []


def clean_data(staff: list) -> list[dict]:
    result = []
    for person in staff:
        stripped = person.strip()
        person_info = stripped.split(',')
        staff_member = {
            "full_name": person_info[0],
            "salary": person_info[1]
        }
        result.append(staff_member)

    return result


class EmptyListException(Exception):
    '''Raise specific situation when the file is found but it is empty'''


print(f"Correct file:", format(total_salary("salaries.txt")))
print(f"Missing file:",format(total_salary("missing-file.txt")))
print(f"Empty file:", format(total_salary("empty-file.txt")))