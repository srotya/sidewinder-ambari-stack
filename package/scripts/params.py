#!/usr/bin/env python
"""
Sidewinder Params configurations
"""

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import status_params

# server configurations
config = Script.get_config()

sidewinder_home = '/usr/sidewinder'
sidewinder_bin = '/usr/sidewinder/bin/'
sidewinder_user = 'sidewinder'
conf_dir = "/etc/sidewinder"
pid_dir = '/var/run/sidewinder'
pid_file = '/var/run/sidewinder/sidewinder.pid'

# Environment properties
log_dir = config['configurations']['sidewinder-env']['log_dir']
hostname = config['hostname']
java64_home = config['hostLevelParams']['java_home']
sidewinder_env_sh_template = config['configurations']['sidewinder-env']['content']

# Basic properties
data_dir = config['configurations']['sidewinder-props']['data.dir']
index_dir = config['configurations']['sidewinder-props']['index.dir']
max_open_files = config['configurations']['sidewinder-props']['max_open_files']
