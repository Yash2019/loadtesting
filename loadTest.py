import random 
from locust import HttpUser, between, tag, task

class StudentPortalUser(HttpUser):
    wait_time = between(0.2, 1.0)

    @tag('valid_result')
    @task(9)

    def get_valid_result(self):
        roll_id = random.randint(1, 100000)
        roll_number = f"2026{roll_id:07d}"

        with self.client.get(
            f"/get_results/{roll_number}",
            name='/get_result/[valid_roll_number]',
            catch_response=True
        ) as res:
            if res.status_code == 200:
                res.success()

            else:
                res.failure(f"Unexpected status: {res.status_code}")

    @tag('invalid_result')
    @task(1)

    def get_invlalid_task(self):
        invalid_roll = "202699999991"
        with self.client.get(
            f'/get_result/{invalid_roll}',
            name='/get_result/[invalid_roll_number]',
            catch_response=True
        ) as res:
            if res.status_code in (200, 404):
                res.success()
            else:
                res.failure(f'Expected 404 or empty response, got: {res.status_code}')