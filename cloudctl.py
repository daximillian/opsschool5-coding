#!/usr/bin/env python

import click
import boto3
from prettytable import PrettyTable
              
@click.group()

@click.option('-t','--tags', nargs=2, type=str, help='Query resources by tags')
@click.option('-c','--cloud',type=click.Choice(['aws', 'gcp', 'azure']), help='Cloud provider to query', default='aws', 
              show_default=True)

@click.pass_context       
def cloudctl(ctx, **kwargs):
    """Cloud Manager cli"""
    if kwargs['tags']:
        print(kwargs['tags'])

@cloudctl.group()
def get():
    """get action"""
    pass

@get.command()
def instances():
    """Instances command"""
    instance_table = PrettyTable()
    instance_table.field_names = ["Instance ID", "State", "Public DSN", "Private DSN"]
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_table.add_row([instance["InstanceId"], instance["State"]["Name"], instance["PublicDnsName"],instance["PrivateDnsName"]])
    
    print(instance_table)
    
    
cloudctl.add_command(get)

@cloudctl.group()
def stop():
    """stop action"""
    pass

@stop.command()
def instances():
    """Instances command"""
    pass

cloudctl.add_command(stop)

if __name__ == '__main__':
    cloudctl()
    