SNS Security Alert

Python script that publishes a security alert to an Amazon SNS topic. Subscribers (e.g. email) receive the alert.

Requirements
Python 3.8+
boto3 (pip install boto3)
An SNS topic with a confirmed subscription
AWS credentials with sns:Publish permission on the topic
Configuration

Set the following environment variables:

bash
export AWS_ACCESS_KEY_ID="your-access-key"

export AWS_SECRET_ACCESS_KEY="your-secret-key"

export TOPIC_ARN="arn:aws:sns:us-east-1:123456789012:security-alerts"

The region is set to us-east-1 in the script. Change region_name if your topic is elsewhere.

Usage
bash
python alert.py

The script sends a simulated alert ("CRITICAL: Unauthorized access attempt blocked.") to the topic. Replace it with your own detection logic as needed.

Security
Do not commit AWS credentials. Use an IAM user or role limited to sns:Publish on this topic.
