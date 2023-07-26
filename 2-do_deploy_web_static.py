#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = ["100.26.9.188", "100.26.227.244"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if exists(archive_path):
        put(archive_path, '/tmp/')

        filename = basename(archive_path)
        file_ext = splitext(filename)[0]

        sudo(f'mkdir -p /data/web_static/releases/{file_ext}')
        sudo(f'tar -xzf /tmp/{filename} -C /data/web_static/releases/{file_ext}')
        sudo('rm -rf /tmp/{filename}')
        sudo('rm -rf /data/web_static/current')
        sudo(f'ln -s /data/web_static/releases/{file_ext} /data/web_static/current')
        return True
    return False