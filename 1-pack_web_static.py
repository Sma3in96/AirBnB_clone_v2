#/usr/bin/python
""" this scprit generate .tgz from content of wen static """

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ generate a .tgz """
    
    if not os.path.exists('versions'):
        local("mkdir -p versions")
    
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name = f"web_static_{time}.tgz"

    output = local(f"tar -cf versions/{name} web_static", capture=True)
    if output.failed:
        return None
    else:
        return os.path.join("versions", name)
