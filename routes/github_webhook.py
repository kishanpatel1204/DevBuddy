from flask import Blueprint, request
import hmac, hashlib, os
from dotenv import load_dotenv
from utils.github_api import get_pr_diff, post_comment
from services.ai_review import review_code

load_dotenv()
print("✅ Loaded .env file")
print("🔍 ENV VAR:", os.getenv("WEBHOOK_SECRET"))

webhook = Blueprint('webhook', __name__)
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET").encode()
print("🔐 Loaded webhook secret:", WEBHOOK_SECRET)

@webhook.route('/webhook', methods=['POST'])
def github_webhook():
    print("✅ Webhook received")

    signature = request.headers.get('X-Hub-Signature-256', '').split('=')[-1]
    computed = hmac.new(WEBHOOK_SECRET, request.data, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, computed):
        print("❌ Signature mismatch")
        return "Unauthorized", 401
    
    payload = request.json


    if payload.get("action") == "opened":
        print("🎯 Pull request opened event detected")

        diff_urls = payload["pull_request"]["diff_url"]
        repo = payload["repository"]["full_name"]
        pr_number = payload["pull_request"]["number"]

        print("🔗 Diff URL:", diff_urls)
        print("📘 Repo:", repo, "PR Number:", pr_number)

        diff = get_pr_diff(diff_urls)
        comment = review_code(diff)
        post_comment(repo, pr_number, comment)

    return "OK", 200

