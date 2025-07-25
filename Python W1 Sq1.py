from datetime import datetime

def calculate_age():
    try:
        #user input
        birth_input = input("Enter your DOB (mm/dd/yyyy): ")
        #parsing and validating the date
        birth_date = datetime.strptime(birth_input, "%m/%d/%Y")
        #to fetch current date
        today = datetime.today()
        #to calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"You are {age} years old.")
        #to print it in EU format
        eu_format = birth_date.strftime("%d/%m/%Y")
        print(f"Your birth date in EU format: {eu_format}")
    
    except ValueError:
        print("incorrect date format! the required format is : mm/dd/yyyy")

calculate_age()
