# EDGE Training Management Portal Automation
This script is a Python-based automation project that uses Playwright to automate a web-based batch creation process for government training. It also generates synthetic trainee data in an Excel file using pandas.

**🔹 Project Breakdown**
Excel Data Generation (Simulating Real-world Data)
Automated Web Interaction (Using Playwright)
User Input Handling (Batch Number Prompt)
File Uploading & Form Submission
Validation & Confirmation (Checking Success Messages)

**📂 Project Structure**
📁 github-automation-project/
│── 📄 main.py                    # Main script for data generation & automation
│── 📄 requirements.txt            # Dependencies (Playwright, pandas, etc.)
│── 📄 README.md                   # Project documentation
│── 📄 .gitignore                   # Ignore unnecessary files (e.g., .xlsx, __pycache__)
│── 📂 automation/
│   ├── 📄 data_generator.py        # Functions for generating names, emails, phone numbers
│   ├── 📄 playwright_script.py     # Web automation using Playwright
│── 📂 test/
│   ├── 📄 test_playwright.py       # Automated tests for Playwright workflow
│── 📂 logs/
│   ├── 📄 automation.log           # Log file for debugging

**🔹 How the Script Works**
1️⃣ Excel Data Generation
The script generates random trainee data including:

Name (From predefined lists)
Gender (Randomly Male/Female)
Mobile Number (Bangladeshi format)
Email (Random with fake domains)
Organization Name
Designation

**2️⃣ Playwright Web Automation**
Launches Chromium browser
Logs into the Training Portal
Fills out the Batch Creation Form
Uploads the Generated Excel File
Submits the form & verifies success

**3️⃣ Verification & Logging**
After submission, the script validates the success message
