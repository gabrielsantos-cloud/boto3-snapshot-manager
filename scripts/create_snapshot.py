import boto3
import yaml

client_ec2 = boto3.client('ec2')

def create_snapshots(config_file='../config/config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    for instance_id in config['instances']:
            volumes = client_ec2.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])
            for volume in volumes['Volumes']:
                snapshot = client_ec2.create_snapshot(VolumeId=volume['VolumeId'], Description=f"Backup of {instance_id}")
                print(f"Snapshot criada:: {snapshot['SnapshotId']} para o Volume: {volume['VolumeId']}")

if __name__ == "__main__":
     create_snapshots()