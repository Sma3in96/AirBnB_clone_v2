#!/usr/bin/python3
''' distribute the archive to the web servers '''
from fabric.api import put, run, env
import os

env.hosts = ['18.234.193.16', '100.25.183.7']


def do_deploy(archive_path):
    """ deploy the web static """
    if not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        ext_d = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f"sudo mkdir -p /data/web_static/releases/{ext_d}/")
        run(f"sudo tar -xzf /tmp/{file} -C /data/web_static/releases/{ext_d}/")
        run(f"sudo rm /tmp/{file}")
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, ext_d))
        run(f'sudo rm -rf {path}{ext_d}/web_static')
        run('sudo rm -rf /data/web_static/current')
        run(f"sudo ln -s {path}{ext_d}/ /data/web_static/current")
        return True
    except Exception as e:
        return False