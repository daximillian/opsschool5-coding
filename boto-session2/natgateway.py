#!/usr/bin/env python
""" NAT gateway creation module
"""

import awsops
import parsing
import config

def main():
    """ Create a NAT gateway.
    """
    parser = parsing.Parsing()
    args = parser.args_parser()
    aws = awsops.AwsOperations(args)
    allocate_id = aws.allocate_address()
    subnet_id = aws.get_subnet_id(config.PUBLIC_TAG)
    nat_gateway_id = aws.create_nat_gateway(subnet_id, allocate_id)
    aws.wait_for_nat_gateway(nat_gateway_id)
    print(nat_gateway_id)


if __name__ == '__main__':
    main()
