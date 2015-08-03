from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def sync():
    env.hosts = ['www.co-pylit.org']
    localdir = 'output/'
    remotedir = 'html/blog'
    local('rsync -arvuz %s %s@%s:%s' %(localdir,env.user,env.hosts[0],remotedir))
    with cd('html/blog/images'):
        local('chmod 755 *')

def newsync():
    env.hosts = ['166.78.143.79']
    localdir = 'output/'
    remotedir = 'html/blog'
    local('rsync -arvuz %s %s@%s:%s' % (localdir, env.user, env.hosts[0], remotedir))
    with cd('html/blog/images'):
        local('chmod 755 *')
