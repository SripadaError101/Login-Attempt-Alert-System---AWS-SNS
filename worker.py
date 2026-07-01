import boto3
import os
import time

# Use environment variables so you don't leak your keys!
sns = boto3.client(
    'sns',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1' # Make sure this matches your SNS region
)

def send_alert():
    print("Checking for threats...")
    # This is the ARN you copied from your SNS Topic
    topic_arn = os.environ.get('TOPIC_ARN')
    
    sns.publish(
        TopicArn=topic_arn,
        Message="CRITICAL: Unauthorized access attempt blocked.",
        Subject="Security Alert"
    )
    print("Alert sent to your email!")

if __name__ == "__main__":
    # Simulate a detection event
    send_alert()