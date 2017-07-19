#!/usr/bin/env python
"""
sidewinder service params

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def sidewinder():
    import params

    params.data_dir = params.data_dir.replace('"','')
    data_path = params.data_dir.replace(' ','').split(',')
    data_path[:]=[x.replace('"','') for x in data_path]

    directories = [params.log_dir, params.pid_dir, params.conf_dir, params.index_dir]
    directories = directories+data_path;

    Directory(directories,
              owner=params.sidewinder_user,
              group=params.sidewinder_user,
              recursive=True
          )

    File(format("{conf_dir}/sidewinder-env.sh"),
          owner=params.sidewinder_user,
          content=InlineTemplate(params.sidewinder_env_sh_template)
     )

    props = mutable_config_dict(config['configurations']['sidewinder-props'])
    props = add_configs(config['configurations']['sidewinder-advanced-props'])

    PropertiesFile("sidewinder.properties",
                      dir=params.conf_dir,
                      properties=props,
                      owner=params.sidewinder_user,
                      group=params.sidewinder_user,
    )

    yaml = config['configurations']['sidewinder-yaml']

    File(format("{conf_dir}/sidewinder.yaml"),
       content=Template(
                        "sidewinder.yaml.j2", yaml),
       owner=params.sidewinder_user,
       group=params.sidewinder_user
    )

def add_configs(server_config, sidewinder_config):
    for key, value in sidewinder_config.iteritems():
        server_config[key] = value
    return server_config

def mutable_config_dict(sidewinder_config):
    server_config = {}
    for key, value in sidewinder_config.iteritems():
        server_config[key] = value
    return server_config
