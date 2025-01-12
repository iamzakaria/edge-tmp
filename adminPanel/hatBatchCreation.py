import random
import string
import pandas as pd
import time

from playwright.sync_api import Page, sync_playwright, expect

# Define random data generators
def generate_random_name():
    first_names = [
        "Ali", "Hasan", "Sami", "Nadia", "Maya", "Rahim", "Kamal", "Farzana", "Anika", "Tariq",
        "Jessica", "Michael", "Emily", "David", "Sarah", "Daniel", "Laura", "Christopher", "Emma",
        "John", "Robert", "Patricia", "Jennifer", "Linda", "Elizabeth", "James", "Mary", "Joseph", "Charles",
        "Sophia", "Benjamin", "Matthew", "Anthony", "Andrew", "Thomas", "Joshua", "Alexander", "Ryan", "Nicholas"
    ]
    last_names = [
        "Ahmed", "Chowdhury", "Khan", "Rahman", "Islam", "Hossain", "Bari", "Mollah", "Sultana", 
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Wilson", "Anderson", "Taylor", "Thomas", "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_parent_name():
    return generate_random_name()

def generate_bangladeshi_phone():
    prefixes = ["017", "018", "019", "016", "015"]
    prefix = random.choice(prefixes)
    number = ''.join(random.choices(string.digits, k=8))
    return f"{prefix}{number}"

def generate_random_email():
    domains = ["test1.com", "dummy1.com", "example1.org", "fakemail1.com"]
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_organization_name():
    organizations = [
        "ICT Division", "Bangladesh Computer Council", "Department of IT", "Tech Solutions Ltd.",
        "Digital Bangladesh Initiative", "Future Tech Enterprises", "Smart Solutions Inc.", 
        "Innovative Systems", "Tech Pioneers Group", "Digital Transformation Hub",
        "AI Innovations Ltd.", "Cyber Security Agency", "Tech Support Services", "Software Solutions BD", 
        "Cloud Computing Corp", "Green Tech Group", "Tech Savvy Solutions", "Data Analytics Co.", "E-Governance Services"
    ]
    return random.choice(organizations)

def generate_designation():
    designations = [
        "Assistant Programmer", "Junior Analyst", "Project Manager", "Software Developer", 
        "System Administrator", "Data Analyst", "Senior Developer", "IT Consultant", 
        "Network Engineer", "Database Administrator", "Cyber Security Specialist", "DevOps Engineer",
        "AI Engineer", "Cloud Architect", "Business Analyst", "Front-end Developer", "Back-end Developer", "Full Stack Developer"
    ]
    return random.choice(designations)

def generate_random_date():
    year = random.randint(1980, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{month:02d}/{day:02d}/{year}"


def generate_nid():
    first_digit = random.choice('123456789')
    other_digits = ''.join(random.choices(string.digits, k=12))
    return first_digit + other_digits


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
        "DoB (mm/dd/YYYY)": [generate_random_date() for _ in range(row_count)],
        "Nationality": ["Bangladeshi" for _ in range(row_count)],
        "NID Number": [str(generate_nid()) for _ in range(row_count)], # Ensure NID is saved as text
        "Present Address": [generate_address() for _ in range(row_count)],
        "Permanent Address": [generate_address() for _ in range(row_count)],
        "Mobile Number": [generate_bangladeshi_phone() for _ in range(row_count)],
        "Emergency Contact": [generate_bangladeshi_phone() for _ in range(row_count)],
        "email": [generate_random_email() for _ in range(row_count)],
        "Level of Education": [random.choice(["SSC", "HSC", "Bachelor's", "Master's", "Diploma"]) for _ in range(row_count)],
        "Subject/Diploma/Group": [random.choice(["Science", "Arts", "Commerce", "Engineering", "Business"]) for _ in range(row_count)],
        "Position Hold": [generate_designation() for _ in range(row_count)],
        "Salary": [random.randint(20000, 50000) for _ in range(row_count)],
        "Joining Date (mm/dd/YYYY)": [generate_random_date() for _ in range(row_count)]
    }
    return pd.DataFrame(data)
# Generate data and save to Excel with xlsxwriter 
df = generate_data_for_excel() 
# Use xlsxwriter to save as plain text 
with pd.ExcelWriter(r"C:\Users\LENOVO\Desktop\edge-tmp\adminPanel\Generated_20_HAT_Trainees_Data.xlsx", engine='xlsxwriter') as writer: 
    df.to_excel(writer, index=False, sheet_name='Sheet1') 
    # Get the xlsxwriter workbook and worksheet objects. 
    workbook = writer.book 
    worksheet = writer.sheets['Sheet1'] 
    # Set the format for the NID Number column to text. 
    text_format = workbook.add_format({'num_format': '@'}) 
    worksheet.set_column('I:I', None, text_format) 
    print("Excel file generated successfully!")

from playwright.sync_api import Page, sync_playwright, expect

# Playwright automation for batch creation
def hat_batch_creation(page: Page, excel_file_path: str, pdf_file_path: str, batch_number: str) -> None:
    try:
        page.goto("https://dev-training.sla.gov.bd/")
        page.wait_for_load_state('networkidle')
        page.get_by_role("link", name="Sign in").click()
        page.get_by_placeholder("Email Address").click()
        page.get_by_placeholder("Email Address").fill("hatpm@mail.com")
        page.get_by_placeholder("Password").click()
        page.get_by_placeholder("Password").fill("123456a@R")
        page.get_by_role("button", name="SIGN IN").click()
        page.get_by_role("link", name="Hire and Train").first.click()
        page.get_by_role("link", name="Batches").first.click()
        page.get_by_role("link", name=" Add New").click()
        page.get_by_role("textbox", name="Select Organizer Dept./").click()
        page.get_by_role("option", name="All Training Organization").click()
        page.get_by_label("Batch No").click()
        page.get_by_label("Batch No").fill(batch_number)
        page.get_by_role("textbox", name="Select Training Track").click()
        page.get_by_role("option", name="Blockchain", exact=True).click()
        page.get_by_label("Title of Training").click()
        page.get_by_label("Title of Training").fill("Fundamentals of Blockchain")
        page.get_by_role("textbox", name="Select Company").click()
        page.get_by_role("option", name="Ubisoft").click()
        page.get_by_role("textbox", name="Select District").click()
        page.get_by_role("option", name="Cox's Bazar").click()
        page.get_by_role("textbox", name="Select One").click()
        page.get_by_role("option", name="Chakaria").click()
        page.get_by_label("Training Venue").click()
        page.get_by_label("Training Venue").fill("Testvenue test data")
        page.get_by_role("textbox", name="Select First Trainer").click()
        page.get_by_role("option", name="Bon Jovi").click()
        page.get_by_role("textbox", name="Select Second Trainer").click()
        page.get_by_role("option", name="Reagan Rivas").click()
        page.get_by_role("textbox", name="Select Third Trainer").click()
        page.get_by_role("option", name="Cheryl Cochran").click()
        page.get_by_label("Coordinator Name").click()
        page.get_by_label("Coordinator Name").fill("Test Coordinator")
        page.get_by_label("Mobile Number").click()
        page.get_by_label("Mobile Number").fill("01756565656")
        page.get_by_label("Email Address").click()
        page.get_by_label("Email Address").fill("dummy@tes.com")
        page.get_by_label("Start Date").click()
        page.get_by_role("cell", name="2", exact=True).first.click()
        page.get_by_label("End Date").click()
        page.get_by_role("cell", name="15", exact=True).click()
        page.get_by_label("Mid Term Assessment Date").click()
        page.get_by_role("cell", name="2", exact=True).first.click()
        page.get_by_label("Final Term Assessment Date").click()
        page.get_by_role("cell", name="20", exact=True).click()
        page.locator("input[name=\"trainee_attendance_report\"]").click()
        page.locator("input[name=\"trainee_attendance_report\"]").set_input_files(pdf_file_path)
        page.get_by_label("Trainee Data").click()
        page.get_by_label("Trainee Data").set_input_files(excel_file_path)
        page.get_by_label("Photo Gallery Link").click()
        page.get_by_label("Photo Gallery Link").fill("https://www.w3schools.com/css/css_image_gallery.asp")
        page.get_by_label("Remarks").click()
        page.get_by_role("button", name="Submit").click()
        page.wait_for_load_state('networkidle')
        page.get_by_role("button", name="Validate & Submit").click()

        # Print success message 
        
        print("Batch creation successful!")
     
    except Exception as e:
        print(f"An error occurred during batch creation: {e}")

# Main program to run Playwright script
if __name__ == "__main__":
    excel_file_path = r"C:\Users\LENOVO\Desktop\edge-tmp\adminPanel\Generated_20_HAT_Trainees_Data.xlsx"
    pdf_file_path = r"C:\Users\LENOVO\Desktop\edge-tmp\adminPanel\git-cheat-sheet-education.pdf"
    
    # Prompt user for Batch Number input
    batch_number = input("Enter the Batch Number: ")
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        hat_batch_creation(page, excel_file_path, pdf_file_path, batch_number)

        context.close()
        browser.close()
