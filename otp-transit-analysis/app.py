import boto3
import base64

def main():

    user_data_script = base64.b64encode(bytes('touch /test.txt', 'utf-8')).decode("ascii")

    client = boto3.client('ec2')
    response = client.request_spot_instances(
        DryRun=False,
        SpotPrice='0.10',
        InstanceCount=1,
        Type='one-time',
        LaunchSpecification={
            'ImageId': 'ami-04681a1dbd79675a5',
            # 'KeyName': 'awskey.pem',
            'SecurityGroups': [],
            'InstanceType': 't1.micro',
            'Placement': {
                'AvailabilityZone': 'us-east-1a',
            },
            'SecurityGroupIds': [

            ],
            'UserData': user_data_script
        }
    )

    print(response)
    ec2 = boto3.resource('ec2')
    print(ec2.instances)


if __name__ == "__main__":
    main()
