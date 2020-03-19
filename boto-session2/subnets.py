#!/usr/bin/env python
""" Subnet creation module
"""

import awsops
import parsing
import config


def main():
    """ Create a private and public subnet.
    """
    parser = parsing.Parsing()
    args = parser.args_parser()
    aws = awsops.AwsOperations(args)
    public_cidr = config.MAPPING[config.PUBLIC_TAG]
    public_subnet_id = aws.create_subnet(public_cidr)
    aws.create_tags(public_subnet_id, config.PUBLIC_TAG)
    private_cidr = config.MAPPING[config.PRIVATE_TAG]
    private_subnet_id = aws.create_subnet(private_cidr)
    aws.create_tags(private_subnet_id, config.PRIVATE_TAG)


if __name__ == '__main__':
    main()
