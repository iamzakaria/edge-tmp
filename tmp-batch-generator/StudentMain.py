import random
import string
import pandas as pd

# Define random data generators
def generate_random_name():
    first_names = ["Ali", "Hasan", "Sami", "Nadia", "Maya", "Rahim", "Kamal", "Farzana", "Anika", "Tariq"]
    last_names = ["Ahmed", "Chowdhury", "Khan", "Rahman", "Islam", "Hossain", "Bari", "Mollah", "Sultana", "Umer", "Vaseem", "Waqas", "Yawar", "Zaheer", "Amin", "Aziz", "Badi", "Daud", "Faisal", "Ghani"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_parent_name():
    return generate_random_name()

def generate_bangladeshi_phone():
    prefixes = ["017", "018", "019", "016", "015"]
    prefix = random.choice(prefixes)
    number = ''.join(random.choices(string.digits, k=8))
    return f"{prefix}{number}"

def generate_random_email():
    domains = ["test.com", "dummy.com", "example.org", "fakemail.com"]
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_date():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day}/{month}/{year}"

def generate_nid():
    return ''.join(random.choices(string.digits, k=10))

def generate_address():
    streets = ["Main St", "High St", "Park Ave", "2nd Ave", "3rd St"]
    return f"{random.randint(1, 999)} {random.choice(streets)}, City, Country"

# Generate data for trainees
def generate_data_for_excel(course_name, organizer_univ, organizer_dept, batch_number, row_count=20):
    data = {
        "SL No.": list(range(1, row_count + 1)),
        "Training Track/ Course name": [course_name] * row_count,
        "Training Organizer Univ.": [organizer_univ] * row_count,
        "Organizer Dept./Institute/Center": [organizer_dept] * row_count,
        "Batch Number": [batch_number] * row_count,
        "Trainee's Name": [generate_random_name() for _ in range(row_count)],
        "Father's name": [generate_random_parent_name() for _ in range(row_count)],
        "Mother's Name": [generate_random_parent_name() for _ in range(row_count)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(row_count)],
        "Religion": [random.choice(["Islam", "Hinduism", "Christianity", "Buddhism"]) for _ in range(row_count)],
        "DoB (d/m/YYYY)": [generate_random_date() for _ in range(row_count)],
        "Nationality": ["Bangladeshi" for _ in range(row_count)],
        "National ID Card No./ Birth Registration No.": [generate_nid() for _ in range(row_count)],
        "Present Address": [generate_address() for _ in range(row_count)],
        "Permanent Address": [generate_address() for _ in range(row_count)],
        "Mobile": [generate_bangladeshi_phone() for _ in range(row_count)],
        "Guardian's Mobile": [generate_bangladeshi_phone() for _ in range(row_count)],
        "eMail": [generate_random_email() for _ in range(row_count)],
        "Level of Education": [random.choice(["SSC", "HSC", "Bachelor's", "Master's", "Diploma"]) for _ in range(row_count)],
        "Subject/Diploma/Group": [random.choice(["Science", "Arts", "Commerce", "Engineering", "Business"]) for _ in range(row_count)],
        "Trainee's University Name": [organizer_univ] * row_count,
        "Name of Dept./Institute/Center": [organizer_dept] * row_count,
        "Training Location": [generate_address() for _ in range(row_count)],
        "Photo": ["" for _ in range(row_count)] # Keep Photo column empty
    }

    return pd.DataFrame(data)

# Main program
if __name__ == "__main__":
    # User inputs
    course_name = input("Enter the Course Name: ")
    organizer_univ = input("Enter the Training Organizer Univ.: ")
    organizer_dept = input("Enter the Organizer Dept./Institute/Center: ")
    batch_number = input("Enter the Batch Number: ")

    # Generate data
    output_data = generate_data_for_excel(course_name, organizer_univ, organizer_dept, batch_number, 20)

    # Output file path
    output_file_path = r"C:\Users\LENOVO\Desktop\edge-tmp\tmp-batch-generator\Generated_20_Student_Trainees_Data.xlsx"

    # Save to Excel
    output_data.to_excel(output_file_path, index=False, engine='openpyxl')
    print(f"Generated Excel file saved at: {output_file_path}")
