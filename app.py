from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Project 10 - Full DevOps Pipeline</h1>

    <h2>Application Running Successfully</h2>

    <p>GitHub → Jenkins → Docker → Amazon ECR → Amazon EKS</p>

    <p>Terraform • CloudWatch • S3 • IAM</p>
    """

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
