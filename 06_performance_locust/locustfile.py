from locust import HttpUser, task, between

class CounterUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(3, 5)

    @task(1)
    def load_index_page(self):
        self.client.get("/")

    @task(3)
    def hit_counter(self):
        self.client.post("/hit")