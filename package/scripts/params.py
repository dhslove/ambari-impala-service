#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob ,socket

# server configurations
config = Script.get_config()

impala_user = config['configurations']['impala-env']['impala_user']
impala_group = config['configurations']['impala-env']['impala_group']
impala_log_dir = config['configurations']['impala-env']['impala_log_dir']
impala_log_file = os.path.join(impala_log_dir,'impala-setup.log')
impala_catalog_host = config['clusterHostInfo']['impala_catalog_service_hosts'][0]
impala_state_store_host = config['clusterHostInfo']['impala_state_store_hosts'][0]

service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
current_host_name = socket.gethostname()

security_enabled = config['configurations']['cluster-env']['security_enabled']