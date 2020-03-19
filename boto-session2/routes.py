#!/usr/bin/env python
""" Route table creation module
"""

import awsops
import parsing
import config

def main():
    """ Create public and private route tables
    """
    parser = parsing.Parsing()
    args = parser.args_parser()
    aws = awsops.AwsOperations(args)
    public_route_table_id = aws.create_route_table()
    aws.create_tags(public_route_table_id, config.PUBLIC_TAG)
    aws.add_internet_gateway_route(public_route_table_id, config.DESTINATION)
    public_subnet_id = aws.get_subnet_id(config.PUBLIC_TAG)
    aws.associate_route_table(public_route_table_id, public_subnet_id)
    # create private route table
    # create tags for the private route table
    # get private subnet id
    # create nat gateway route
    # associate the private subnet with the private route table
    private_route_table_id = aws.create_route_table()
    aws.create_tags(private_route_table_id, config.PRIVATE_TAG)
    private_subnet_id = aws.get_subnet_id(config.PRIVATE_TAG)
    aws.add_nat_gateway_route(private_route_table_id, config.DESTINATION, args.natgw)
    aws.associate_route_table(private_route_table_id, private_subnet_id)
if __name__ == '__main__':
    main()
