import random
import string
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect

# Excel Generation Functions
def generate_random_name():
    first_names = [
        "Ali", "Hasan", "Sami", "Nadia", "Maya", "Rahim", "Kamal", "Farzana", "Anika", "Tariq", 
        "Aisha", "Bashir", "Dilara", "Emran", "Farhad", "Gulshan", "Hafsa", "Irfan", "Jasmine", 
        "Khadija", "Lamia", "Munir", "Nashita", "Omar", "Parvin", "Qasim", "Rafiq", "Saima", 
        "Tanvir", "Urmila", "Vikar", "Wasim", "Yasmin", "Zahid", "Farah", "Ashraf", "Nadir", 
        "Safia", "Imran", "Razia", "Javed", "Anwar", "Babar", "Sumaiya", "Neha", "Amin", "Latif", 
        "Shamim", "Musa", "Sana", "Taslima", "Arif", "Bilkis", "Kaiser", "Rubina", "Arafat", 
        "Shahana", "Azhar", "Humayun", "Nafisa", "Junaid", "Rashida", "Saleh", "Rumana", "Wahid", 
        "Adiba", "Abdul", "Asma", "Iqbal", "Ishrat", "Jahanzeb", "Kausar", "Manzoor", "Misbah", 
        "Mahmood", "Nazim", "Rehana", "Salim", "Sadiq", "Shamila", "Wajid", "Yusuf", "Zainab", 
        "Asif", "Habib", "Tasnim", "Burhan", "Tanima", "Zubair", "Rihana", "Nasir", "Akib", 
        "Rupa", "Jahida", "Ajmal", "Kamran", "Tabassum", "Tanisha", "Nabila", "Shereen"
    ]
    last_names = [
        "Ahmed", "Chowdhury", "Khan", "Rahman", "Islam", "Hossain", "Bari", "Mollah", "Sultana", 
        "Akter", "Ali", "Alam", "Munir", "Ashraf", "Begum", "Haque", "Jahan", "Mirza", "Nahar", 
        "Parveen", "Rashid", "Shafiq", "Taher", "Uddin", "Waheed", "Yusuf", "Zaman", "Anwar", 
        "Badar", "Bashar", "Choudhury", "Dewan", "Fahim", "Ghani", "Habib", "Iqbal", "Jahangir", 
        "Kaiser", "Lutfur", "Mahmud", "Naeem", "Osman", "Pasha", "Qadir", "Rauf", "Sajid", 
        "Tariq", "Usman", "Vikar", "Wahid", "Yasmin", "Zahid", "Altaf", "Basit", "Dastagir", 
        "Faiz", "Gulzar", "Hamid", "Idris", "Jamil", "Kamran", "Latif", "Mahtab", "Nadim", 
        "Omar", "Qureshi", "Rumi", "Sabir", "Tauseef", "Umer", "Vaseem", "Waqas", "Yawar", 
        "Zaheer", "Amin", "Aziz", "Badi", "Daud", "Faisal", "Ghani", "Hassan", "Ismail", 
        "Javed", "Karim", "Masood", "Naseem", "Owais", "Pervaiz", "Qasim", "Rana", "Sarwar", 
        "Tariq", "Ubaid", "Waleed", "Yawar", "Zubair", "Farooq", "Anis", "Rauf", "Sheikh", "Harold"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

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
        "Tech Solutions Ltd.", "Digital Bangladesh Initiative",
        "Future Tech Enterprises", "Smart Solutions Inc.", "Innovative Systems",
        "Tech Pioneers Group", "Digital Transformation Hub", "AI Innovations Ltd.", 
        "Cyber Security Agency", "Tech Support Services", "Software Solutions BD", 
        "Cloud Computing Corp", "Green Tech Group", "Tech Savvy Solutions", 
        "Data Analytics Co.", "E-Governance Services", "IoT Development Center", 
        "Tech Prodigy Labs", "Future Vision Systems", "Tech Fusion Ltd.", 
        "Virtual Reality Hub", "Blockchain Solutions BD", "IT Consultancy Services", 
        "Big Data Insights", "Advanced Tech Hub", "AI Research Institute", 
        "Digital Marketing Experts", "Mobile App Development", "Software Engineering Firm", 
        "Robotics Solutions", "Tech Growth Partners", "Web Development Studio", 
        "Digital Innovations", "Tech Ventures Ltd.", "Creative IT Solutions", 
        "Cloud Services BD", "Tech Evolution Group", "Data Science Company", 
        "Innovative IT Services", "Tech Education Center", "E-Commerce Solutions", 
        "IT Infrastructure Services", "Smart City Initiative", "Tech Ecosystem Ltd.", 
        "Digital Health Solutions", "Tech Revolution Labs", "Information Security Firm", 
        "AI & Machine Learning Co.", "Green IT Solutions", "Future Ready Tech", 
        "Tech Deployment Services", "Digital Literacy Campaign", "Internet of Things BD", 
        "AI Integration Hub", "Data Management Corp", "E-Gov Development Center", 
        "Tech Disruptors Ltd.", "Innovative Business Solutions", "Next Gen Tech Group", 
        "Cyber Defense Agency", "Software Development House", "Tech Sustainability Initiative", 
        "AI Implementation Services", "Tech Training Academy", "Digital Transformation Experts", 
        "Blockchain Innovations", "Mobile Tech Solutions", "Tech Strategy Consultants", 
        "Cloud Integration Services", "Green Tech Innovations", "Smart IT Solutions", 
        "Digital Economy Hub", "Tech Empowerment Co.", "Data Visualization Experts", 
        "Tech Research Lab", "Smart Manufacturing Solutions", "AI-Powered Solutions", 
        "Digital Infrastructure BD", "Tech Partnership Group", "Future Tech Services", 
        "IT Systems Integration", "Digital Solutions Company", "Tech Enhancement Hub", 
        "AI Ecosystem Ltd.", "Green Tech Initiative", "Innovative Digital Solutions", 
        "Tech Leadership Academy", "Smart Tech Innovations", "Cyber Security Solutions", 
        "Tech Frontier Group", "Digital Empowerment Initiative", "Cloud Optimization Services", 
        "AI-driven Solutions"
    ]
    return random.choice(organizations)

def generate_designation():
    designations = [
        "Assistant Programmer", "Junior Analyst", "Project Manager",
        "Software Developer", "System Administrator", "Data Analyst"
    ]
    return random.choice(designations)

def generate_data_for_excel(row_count=20):
    data = {
        "Serial/ ID No.": list(range(1, row_count + 1)),
        "Trainee's Name": [generate_random_name() for _ in range(row_count)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(row_count)],
        "Mobile": [generate_bangladeshi_phone() for _ in range(row_count)],
        "email": [generate_random_email() for _ in range(row_count)],
        "Organization Name": [generate_organization_name() for _ in range(row_count)],
        "Current Designation": [generate_designation() for _ in range(row_count)]
    }
    return pd.DataFrame(data)

# Playwright Automation
def run(playwright: Playwright) -> None:
    # Generate the Excel file
    excel_filepath = "Generated_20_Govt_Trainees_Data.xlsx"
    output_data = generate_data_for_excel(20)
    output_data.to_excel(excel_filepath, index=False)
    
    # Playwright Automation
def run(playwright: Playwright) -> None:
    # Generate the Excel file
    excel_filepath = r"C:\Users\LENOVO\Desktop\edge-tmp\adminPanel\Generated_20_Govt_Trainees_Data.xlsx"
    output_data = generate_data_for_excel(20)
    output_data.to_excel(excel_filepath, index=False)
    
    # Prompt user for Batch Number input
    batch_number = input("Enter the Batch Number: ")

    # Start browser automation
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dev-training.sla.gov.bd/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_placeholder("Email Address").click()
    page.get_by_placeholder("Email Address").fill("test@mail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Password")
    page.get_by_role("button", name="SIGN IN").click()
    page.get_by_role("link", name="Govt. Official Training").first.click()
    page.get_by_role("link", name="Batches").first.click()
    page.get_by_role("link", name=" Add New").click()
    page.get_by_label("Batch No").click()
    page.get_by_label("Batch No").fill(batch_number)
    page.get_by_label("Training Topic").fill("Fundamentals of Big Data")
    page.get_by_role("textbox", name="Select Organizer Dept./").click()
    page.get_by_role("option", name="RISE", exact=True).click()
    page.get_by_role("textbox", name="RISE").click()
    page.get_by_role("option", name="RISE 2.O").click()
    page.get_by_role("textbox", name="Select Training Track").click()
    page.get_by_role("option", name="Big Data").click()
    page.get_by_label("Start Date").click()
    page.get_by_role("cell", name="20").nth(1).click()
    page.get_by_label("End Date").click()
    page.get_by_role("cell", name="25").nth(1).click()
    page.get_by_label("Duration (in hour)").fill("20")
    page.get_by_role("combobox").nth(2).click()
    page.get_by_role("option", name="Bon Jovi").click()
    page.get_by_label("Training Venue").click()
    page.get_by_label("Training Venue").fill("Test Web Automation")
    page.locator("input[name=\"csv_file\"]").click()
    page.locator("input[name=\"csv_file\"]").set_input_files(excel_filepath)
    page.get_by_role("button", name="Create").click()
    page.get_by_role("button", name="Close").click()

    expect(page.locator("text=Batch created successfully")).to_be_visible()
    print("Batch creation was successful!")

    # Close browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
