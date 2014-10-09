#!/usr/bin/python2.7
# -*- conding: utf-8 -*-

from fabric.api import (
    local,
    run,
    task,
    sudo,
    env
)

env.hosts = ['localhost']
env.password = 'vagrant'

@task
def install_make():
    sudo("apt-get install gcc")
    sudo("apt-get install build-essential")
