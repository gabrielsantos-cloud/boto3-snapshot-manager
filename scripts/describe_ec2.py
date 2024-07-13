import boto3

client_ec2 = boto3.client('ec2')

response = client_ec2.describe_instances()

next_token = None

while True:
    if next_token:
        response = client_ec2.describe_instances(NextToken=next_token)
    else:
        response = client_ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] != 'running':
                break

            instances_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            print(f"ID da instância: {instances_id}, Tipo: {instance_type}, Estado: {state}")


    next_token = response.get('NextToken')

    if not next_token:
        break
