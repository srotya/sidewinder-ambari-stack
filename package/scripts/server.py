"""
Sidewinder server file
"""

from resource_management import *
import signal
import sys
import os
from os.path import isfile

from sidewinder import sidewinder


class Sidewinder(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Sidewinder'
        stop_cmd = format("wget -O /tmp/sidewinder.rpm http://search.maven.org/remotecontent?filepath=com/srotya/sidewinder/sidewinder-core/0.0.22/sidewinder-core-0.0.22.rpm; rpm -ivf /tmp/sidewinder.rpm")
        Execute(stop_cmd)
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        sidewinder()
    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service sidewinder stop")
        Execute(stop_cmd)
        print 'Stop Sidewinder'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("service sidewinder start")
        Execute(start_cmd)
        print 'Start Sidewinder'
    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service sidewinder status")
        Execute(status_cmd)
        print 'Status of the Master'
if __name__ == "__main__":
    Sidewinder().execute()
