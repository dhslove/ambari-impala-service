import os
from resource_management import *


class ImpalaBase(Script):
    #Call setup.sh to install the service
    def installImpala(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)

        cmd = 'yum-config-manager --add-repo  ' \
              'http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo'

        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)


        cmd = 'yum -y install  impala-server impala-catalog impala-state-store impala-shell'
        Execute('echo "Running ' + cmd + '"')
        Execute(cmd)

