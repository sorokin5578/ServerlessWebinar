# 📘 Serverless Note API – Deployment Guide

This project demonstrates a simple serverless API using AWS Lambda, API Gateway, DynamoDB, CloudFormation, and Budget alerting.

---

## 📦 What’s Included

* `template.yaml` – CloudFormation template to deploy infrastructure
* `index.py` – Python Lambda function to handle GET, POST, DELETE for /notes

---

## 🚀 Deployment Steps

### 1. 🛠️ Launch the CloudFormation Stack

1. Register in AWS if you haven't already: [AWS Free Tier](https://aws.amazon.com/free/). Documentation: [doc](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html).
2. Go to AWS Console → CloudFormation → Create stack → "Choose an existing template (standard)"
3. Upload the `template.yaml` file
4. Click through steps and create the stack (use default options)

⚠️ Budget alert will be created with a \$1 monthly threshold. Replace email in the template with your own before deployment.

---

### 2. 🧠 (Optional) Update Lambda Function Code if needed (manually via AWS Console)

1. Go to AWS Console → Lambda → find function named `NoteApiFunction`
2. Replace the existing code in the Code Editor with the contents of `index.py`
3. Click **Deploy**

---

### 3. 🧪 Test the API

1. Go to API Gateway → `NoteApi` → Stages → `default`
2. Copy the **Invoke URL**, e.g., `https://abc123.execute-api.us-east-1.amazonaws.com/default`
3. Test the API using the `ServerlessWebinar.postman_collection.json` for Postman (don't forget to override API_URL variable) or examples below

#### Test with `curl`:

```bash
# Create a note
curl -X POST -d '{"text": "Hello World"}' -H "Content-Type: application/json" https://<invoke-url>/notes

# Get all notes
curl https://<invoke-url>/notes

# Delete a note
curl -X DELETE https://<invoke-url>/notes/<note-id>
```

---

## 🧹 Cleanup

To avoid charges:

* Delete the CloudFormation stack after the demo
* Remove notes from DynamoDB manually if needed

---

## 💡 Notes

* The project uses AWS Free Tier–friendly options (Lambda, DynamoDB on-demand, API Gateway)
* Budget notifications are sent via email when usage exceeds 80% of \$1

---

## 📬 Need help?

You can ask your instructor or AWS documentation for:

* [Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [API Gateway Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
* [CloudFormation Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
