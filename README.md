# 🌤️ Daily Weather & Outfit Suggestion Agent

An AI-powered **Always-On Agent** built for the **AWS Weekend Agent Challenge**.

This project automatically runs every morning using Amazon EventBridge Scheduler, generates a weather-based outfit recommendation using Amazon Bedrock (Amazon Nova Lite), and stores the AI-generated report in Amazon S3.

---

## 🚀 Features

- 🤖 AI-generated weather summary
- 👕 Outfit recommendations
- 🧢 Accessories suggestion
- ❤️ Health tips
- 💡 Daily motivational quote
- ⏰ Runs automatically every day
- ☁️ Stores reports in Amazon S3

---

## 🏗️ AWS Services Used

- Amazon Bedrock (Amazon Nova Lite)
- AWS Lambda
- Amazon EventBridge Scheduler
- Amazon S3
- IAM

---

## 📋 Architecture

```
           Amazon EventBridge Scheduler
                      │
                      ▼
                AWS Lambda Function
                      │
                      ▼
      Amazon Bedrock (Nova Lite)
                      │
                      ▼
         AI Weather & Outfit Report
                      │
                      ▼
              Amazon S3 Bucket
```

---

## ⚙️ How It Works

1. Amazon EventBridge Scheduler triggers the Lambda function every day at **7:00 AM**.
2. Lambda prepares sample weather information.
3. Amazon Bedrock (Nova Lite) generates:
   - Weather Summary
   - Outfit Recommendation
   - Accessories to Carry
   - Health Tips
   - Motivational Quote
4. Lambda saves the generated report as a text file in Amazon S3.
5. The report is ready for the user to access without manual interaction.

---

## 📂 Project Structure

```
daily-weather-outfit-agent/
│
├── lambda_function.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Deployment Steps

### 1. Create an Amazon S3 Bucket

Example:

```
daily-weather-outfit-agent
```

---

### 2. Create an AWS Lambda Function

- Runtime: Python 3.13
- Region: ap-south-1 (Mumbai)

---

### 3. Configure IAM Permissions

Attach:

- AmazonBedrockFullAccess
- AmazonS3FullAccess

---

### 4. Enable Amazon Bedrock

Enable **Amazon Nova Lite** and use the APAC Inference Profile.

---

### 5. Deploy the Lambda Code

Copy the provided `lambda_function.py` into the Lambda function and deploy it.

---

### 6. Create an EventBridge Schedule

Schedule:

```
cron(0 7 * * ? *)
```

Runs every day at **7:00 AM**.

---

## 📸 Expected Output

A text file is created automatically in the S3 bucket:

```
weather-report-YYYY-MM-DD-HH-MM-SS.txt
```

Example:

```
Weather Summary

Temperature: 33°C
Condition: Sunny

Outfit Recommendation:
Wear light cotton clothes with sunglasses.

Accessories:
Water bottle, cap, sunscreen.

Health Tip:
Stay hydrated and avoid direct sunlight during peak hours.

Motivational Quote:
"Success comes from consistency."
```

---

## 🎯 Challenge Objective

This project was created for the **AWS Weekend Agent Challenge**.

It demonstrates an AI-powered agent that:

- Runs automatically
- Requires no manual interaction
- Uses AWS serverless services
- Generates useful daily recommendations

---

## 📚 What I Learned

During this project I learned how to:

- Build serverless applications with AWS Lambda
- Schedule automatic jobs using Amazon EventBridge
- Generate AI content with Amazon Bedrock (Nova Lite)
- Store generated reports in Amazon S3
- Design an always-on AI agent using AWS services

---

## 👩‍💻 Author

**Parvathi Muthu S**

Built for the **AWS Weekend Agent Challenge 2026** 🚀
