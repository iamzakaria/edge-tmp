from locust import HttpUser, task, between
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebsiteUser(HttpUser):
    host = "https://dev-training.sla.gov.bd"
    wait_time = between(1, 5)

    @task(1)
    def view_homepage(self):
        response = self.client.get("/")
        if response.status_code == 200:
            logger.info("Viewed homepage successfully.")
        else:
            logger.error(f"Failed to view homepage. Status code: {response.status_code}")

    @task(2)
    def hire_train(self):
        response = self.client.get("/hat-training")
        if response.status_code == 200:
            logger.info("Viewed hat training page successfully.")
        else:
            logger.error(f"Failed to view hat training page. Status code: {response.status_code}")

    @task(3)
    def acmp_training(self):
        response = self.client.get("/acmp-training")
        if response.status_code == 200:
            logger.info("Viewed ACMP training page successfully.")
        else:
            logger.error(f"Failed to view ACMP training page. Status code: {response.status_code}")

    @task(4)
    def student_training(self):
        response = self.client.get("/student-training")
        if response.status_code == 200:
            logger.info("Viewed student training page successfully.")
        else:
            logger.error(f"Failed to view student training page. Status code: {response.status_code}")

    @task(5)
    def govt_training(self):
        response = self.client.get("/govt-training")
        if response.status_code == 200:
            logger.info("Viewed government training page successfully.")
        else:
            logger.error(f"Failed to view government training page. Status code: {response.status_code}")

    @task(6)
    def login(self):
        response = self.client.get("/login")
        csrf_token = self.extract_csrf_token(response.text)

        if csrf_token:
            login_response = self.client.post("/login", data={
                "email": "fxf0i@example.org",
                "password": "123456a@R",
                "_token": csrf_token
            }, cookies=response.cookies)

            if login_response.status_code == 200:
                logger.info("Login successful.")
            else:
                logger.error(f"Login failed with status code {login_response.status_code}")
        else:
            logger.error("CSRF token extraction failed.")

    @task(7)
    def view_profile(self):
        response = self.client.get("/my-profile")
        if response.status_code == 200:
            logger.info("Viewed profile page successfully.")
        else:
            logger.error(f"Failed to view profile page. Status code: {response.status_code}")

    @task(8)
    def view_exam(self):
        response = self.client.get("/my-exams")
        if response.status_code == 200:
            logger.info("Viewed exam page successfully.")
        else:
            logger.error(f"Failed to view exam page. Status code: {response.status_code}")

    @task(9)
    def quiz_test(self):
        response = self.client.get("quiz-test/instruction/2")
        if response.status_code == 200:
            logger.info("Viewed quiz test page successfully.")
        else:
            logger.error(f"Failed to view quiz test page. Status code: {response.status_code}")

    @task(10)
    def view_result(self):
        response = self.client.get("/quiz-test/results/5")
        if response.status_code == 200:
            logger.info("Viewed quiz test results page successfully.")
        else:
            logger.error(f"Failed to view quiz test results page. Status code: {response.status_code}")

    @task(11)
    def complete_profile(self):
        response = self.client.get("/users/profile/complete")
        if response.status_code == 200:
            logger.info("Viewed complete profile page successfully.")
        else:
            logger.error(f"Failed to view complete profile page. Status code: {response.status_code}")

    @task(12)
    def view_certificates(self):
        response = self.client.get("/my-certificates")
        if response.status_code == 200:
            logger.info("Viewed certificates page successfully.")
        else:
            logger.error(f"Failed to view certificates page. Status code: {response.status_code}")

    def extract_csrf_token(self, response_text):
        """Extracts the CSRF token from the response text using regex."""
        match = re.search(r'name="_token" value="(.+?)"', response_text)
        if match:
            return match.group(1)
        return None
