# 🤖 DevBuddy – AI Code Review Assistant

DevBuddy is an AI-powered GitHub Pull Request assistant built with Flask and OpenAI.  
It automatically analyzes pull requests, identifies bugs, code smells, and improvement suggestions, and posts a detailed comment on the PR using GPT.

---

## 🚀 Features

- 🔍 **Automatic code reviews** on pull request creation
- 🤖 Powered by **OpenAI GPT** to detect bugs, vulnerabilities, and bad practices
- 🔔 Posts review comments directly to GitHub PRs
- 🔐 Secure Webhook verification with HMAC signature
- 🧪 Supports local development with tools like **ngrok** or **localtunnel**

---

## 🛠 Tech Stack

- **Python 3.11**
- **Flask**
- **OpenAI API**
- **GitHub Webhooks**
- **Requests / dotenv**
- Optional: SonarQube integration for static analysis

---

## 📦 Project Structure
<pre> ```text DevBuddy/ 
  ├── app.py # Main Flask app 
  ├── .env # Environment variables (never commit this) 
  ├── routes/ 
  │   └── github_webhook.py # Webhook endpoint for GitHub PRs 
  ├── services/ 
  │   └── ai_review.py # Code that connects to OpenAI 
  ├── utils/ 
  │   └── github_api.py # Helpers to fetch diffs and post PR comments 
  └── requirements.txt # Python dependencies ``` </pre>

---

## ⚙️ Setup Instructions

1. **Clone the repo:**
   git clone https://github.com/your_username/DevBuddy.git
   cd DevBuddy

2. **Set up virtual environment:**
    python -m venv venv
    venv\Scripts\activate  # Windows

3. **Install dependencies:**
    pip install -r requirements.txt
   
5. **Create .env file:**
    OPENAI_API_KEY=your_openai_key
    GITHUB_TOKEN=your_github_token
    WEBHOOK_SECRET=your_webhook_secret
   
6. **Run Flask app:**
    python app.py

7. **Expose your localhost (optional):**
        # If ngrok doesn’t work, use:
        npx localtunnel --port 5000

8. **Set up GitHub Webhook:**
  * Go to your GitHub repo → Settings → Webhooks
  * Payload URL: https://your-tunnel-url/webhook
  * Content type: application/json
  * Secret: same as WEBHOOK_SECRET in .env
 ---

## 🧠 Example Prompt for GPT
    “Analyze this code diff and highlight any bugs, security risks, and possible improvements.”

---
## 🧰 Coming Soon
     *✅ SonarQube integration for static analysis
     *📊 Dashboard for tracking code health
     *🧠 Multiple model support (GPT-3.5 / GPT-4 / Claude)
---
## 📄 License
    This project is licensed under the MIT License.
---
## 🙌 Contributions
    Pull requests and issues are welcome!
    Let’s make code reviews smarter together 🚀
