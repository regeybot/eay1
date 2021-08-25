import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
TOKEN = os.environ.get("1979807081:AAEjNFqkdq2UAWoLqQc1Yzoc9TlR6saMhfk")
WEBHOOK_URL = os.environ.get("https://noteay.herokuapp.com")
REDIS_URL = os.environ.get("redis://h:asdfqwer1234asdf@ec2-111-1-1-1.compute-1.amazonaws.com:111")
WORKER_URL = os.environ.get("WORKER_URL")
WORKER_HEADERS = {"X-API-Key": os.environ.get("WORKER_API_KEY")}
