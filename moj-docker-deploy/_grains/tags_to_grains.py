#!/usr/bin/env python

import json
import os
import sys
import boto.ec2
import boto.cloudformation
import urllib2

def get_cf_data():
    metadata_ip = '169.254.169.254'
    try:
        instance_id = urllib2.urlopen(
            'http://{0}/latest/meta-data/instance-id'.format(metadata_ip)).read().strip()
        region = urllib2.urlopen(
            'http://{0}/latest/meta-data/placement/availability-zone'.format(metadata_ip)).read().strip()[:-1]

        conn = boto.cloudformation.connect_to_region(region)
        tags = get_ec2_data()
        stack_name = "{0}-{1}".format(tags['Apps'], tags['Env'])
        stack_outputs = conn.describe_stacks(stack_name)[0].outputs
        out = {}
        [out.update({o.key:o.value}) for o in stack_outputs]
        return out

    except Exception as err:
        sys.stderr.write('tags_to_grains ERROR: %s\n' % str(err))
        sys.exit(2)

def get_ec2_data():
    """
    This retrieves ec2 data for the instance e.g
    Project: courtfinder
    Role: docker
    Apps: search,admin
    Env: dev

    To transform this data into salt grains run:
    ``salt '*' saltutil.sync_all``
    """

    metadata_ip = '169.254.169.254'

    try:

        instance_id = urllib2.urlopen(
            'http://{0}/latest/meta-data/instance-id'.format(metadata_ip)).read().strip()
        region = urllib2.urlopen(
            'http://{0}/latest/meta-data/placement/availability-zone'.format(metadata_ip)).read().strip()[:-1]

        conn = boto.ec2.connect_to_region(region)
        instance = conn.get_all_instances(
            instance_ids=[instance_id])[0].instances[0]
        return instance.tags

    except Exception as err:
        sys.stderr.write('tags_to_grains ERROR: %s\n' % str(err))
        sys.exit(2)

if __name__ == '__main__':
    print get_ec2_data()
    print get_cf_data()
