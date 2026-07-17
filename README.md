# Daily Weather & Outfit Suggestion Agent

## Overview
An always-on AI agent built with AWS for the AWS Weekend Agent Challenge.

## AWS Services
- Amazon EventBridge Scheduler
- AWS Lambda
- Amazon Bedrock (Amazon Nova Lite)
- Amazon S3

## Workflow
1. EventBridge triggers Lambda every day.
2. Lambda uses sample weather data.
3. Amazon Bedrock generates outfit suggestions.
4. Report is saved to Amazon S3.

## Deployment
1. Create an S3 bucket.
2. Create a Lambda function.
3. Grant Bedrock and S3 permissions.
4. Deploy the code.
5. Create an EventBridge schedule.
