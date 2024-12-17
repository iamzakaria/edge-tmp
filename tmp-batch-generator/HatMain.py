import random
import string
import pandas as pd

# Define random data generators
def generate_random_name():
    first_names = ["Ali", "Hasan", "Sami", "Nadia", "Maya", "Rahim", "Kamal", "Farzana", "Anika", "Tariq", "Jessica", "Michael", "Emily", "David", "Sarah", "Daniel", "Laura", "Christopher", "Emma", "Sofia", "Micchael", "Luna", "Jacob", "Grace", "William", "Chloe"]
    last_names = ["Ahmed", "Chowdhury", "Khan", "Rahman", "Islam", "Hossain", "Bari", "Mollah", "Sultana", "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "Lucas", "Isabella", "Mason", 
    "Mia", "James", "Amelia", "Benjamin", "Harper", "Ethan", "Evelyn", "Alexander", "Abigail", "Jackson", "Aiden", "Charlotte", "Samuel", "Aria", "Sebastian", "Ella", "Jack", "Avery", "Daniel", "Scarlett", 
    "Henry"]
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

def generate_organization_name():
    organizations = [
        "ICT Division", "Bangladesh Computer Council", "Department of IT",
        "Tech Solutions Ltd.", "Digital Bangladesh Initiative"
    ]
    return random.choice(organizations)

def generate_designation():
    designations = [
        "Assistant Programmer", "Junior Analyst", "Project Manager",
        "Software Developer", "System Administrator", "Data Analyst"
    ]
    return random.choice(designations)

def generate_random_date():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}/{month:02d}/{year}"

def generate_nid():
    return ''.join(random.choices(string.digits, k=10))

def generate_address():
    streets = ["Main St", "High St", "Park Ave", "2nd Ave", "3rd St"]
    return f"{random.randint(1, 999)} {random.choice(streets)}, City, Country"

# Generate data for trainees
def generate_data_for_excel(row_count=20):
    data = {
        "Serial/ ID No.": list(range(1, row_count + 1)),
        "Trainee's Name": [generate_random_name() for _ in range(row_count)],
        "Father's name": [generate_random_parent_name() for _ in range(row_count)],
        "Mother's Name": [generate_random_parent_name() for _ in range(row_count)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(row_count)],
        "Religion": [random.choice(["Islam", "Hinduism", "Christianity", "Buddhism"]) for _ in range(row_count)],
        "DoB (dd/mm/YYYY)": [generate_random_date() for _ in range(row_count)],
        "Nationality": ["Bangladeshi" for _ in range(row_count)],
        "NID Number": [generate_nid() for _ in range(row_count)],
        "Present Address": [generate_address() for _ in range(row_count)],
        "Permanent Address": [generate_address() for _ in range(row_count)],
        "Mobile Number": [generate_bangladeshi_phone() for _ in range(row_count)],
        "Emergency Contact": [generate_bangladeshi_phone() for _ in range(row_count)],
        "email": [generate_random_email() for _ in range(row_count)],
        "Level of Education": [random.choice(["SSC", "HSC", "Bachelor's", "Master's", "Diploma"]) for _ in range(row_count)],
        "Subject/Diploma/Group": [random.choice(["Science", "Arts", "Commerce", "Engineering", "Business"]) for _ in range(row_count)],
        "Position Hold": [generate_designation() for _ in range(row_count)],
        "Salary": [random.randint(20000, 50000) for _ in range(row_count)],
        "Joining Date (dd/mm/YYYY)": [generate_random_date() for _ in range(row_count)]
    }
    return pd.DataFrame(data)

# Main program
if __name__ == "__main__":
    output_data = generate_data_for_excel(20)
    output_file_path = r"C:\Users\LENOVO\Desktop\edge-tmp\tmp-batch-generator\Generated_20_HAT_Trainees_Data.xlsx"
    output_data.to_excel(output_file_path, index=False, engine='openpyxl') 
    print(f"Generated Excel file saved at: {output_file_path}")
