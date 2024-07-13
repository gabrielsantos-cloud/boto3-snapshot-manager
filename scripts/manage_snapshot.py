import boto3
import yaml
from datetime import datetime, timedelta

def manage_snapshots(config_file='../config/config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    client_ec2 = boto3.client('ec2')

    retention_seconds = config['retention_seconds']
    delete_time = datetime.utcnow() - timedelta(seconds=retention_seconds)

    snapshots = client_ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in snapshots['Snapshots']:
        if snapshot['StartTime'].replace(tzinfo=None) < delete_time:
            client_ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            print(f"Snapshot deletada: {snapshot['SnapshotId']}")

if __name__ == "__main__":
    manage_snapshots()