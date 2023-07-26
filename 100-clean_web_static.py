#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ["100.26.9.188", "100.26.227.244"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    cleans
    """

    number = int(number)

    if number < 0:
        return
    elif number == 0 or number == 1:
        numbers = 1
    else:
        numbers = number + 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(numbers))
    path = '/data/web_static/releases'
    with cd(path):
        sudo('cd {} ; ls -t | head -n +{} | xargs rm -rf'.format(path, numbers))
