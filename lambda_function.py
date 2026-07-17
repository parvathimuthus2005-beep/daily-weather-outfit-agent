import json
import boto3
from datetime import datetime

bedrock=boto3.client("bedrock-runtime",region_name="ap-south-1")
s3=boto3.client("s3",region_name="ap-south-1")

BUCKET_NAME="daily-weather-outfit-agent"

def lambda_handler(event, context):
    weather="""
Location: Chennai
Temperature: 33°C
Condition: Sunny
Humidity: 70%
"""
    prompt=f"""You are a helpful AI weather assistant.

Based on the following weather:

{weather}

Generate:
1. Weather Summary
2. Outfit Recommendation
3. Accessories to Carry
4. Health Tips
5. One Motivational Quote

Keep the response under 150 words."""
    response=bedrock.converse(
        modelId="apac.amazon.nova-lite-v1:0",
        messages=[{"role":"user","content":[{"text":prompt}]}]
    )
    report=response["output"]["message"]["content"][0]["text"]
    filename=f"weather-report-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    s3.put_object(Bucket=BUCKET_NAME,Key=filename,Body=report,ContentType="text/plain")
    return {
        "statusCode":200,
        "body":json.dumps({"message":"Success","file":filename,"report":report})
    }
