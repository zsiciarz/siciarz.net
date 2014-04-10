# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from contextlib import nested

from fabric.api import *


def prepare_project():
    """
    Enters the directory and sources environment configuration.

    I know ``nested`` is deprecated, but what a nice shortcut it is here ;)
    """
    return nested(
        cd(PROJECT_PATH),
        prefix("source ../../../.siciarznet/bin/activate"),
    )


PROJECT_PATH = "$HOME/v/siciarz.net/siciarz.net"

env.roledefs = {
    'web': ["siciarznet@siciarznet.megiteam.pl"],
}
env.color = True


@task
@roles("web")
def git_pull():
    with cd(PROJECT_PATH):
        run("git pull origin master")


@task
@roles("web")
def update_requirements():
    with prepare_project():
        run("pip install -r requirements.txt")


@task
@roles("web")
def migrate():
    with prepare_project():
        run("python manage.py syncdb")
        run("python manage.py migrate")


@task
@roles("web")
def collect_static():
    with prepare_project():
        run("python manage.py collectstatic --noinput")


@task
@roles("web")
def restart():
    run("appctl restart siciarznet")


@task
def open_browser():
    import webbrowser
    webbrowser.open("http://siciarz.net")


@task
@roles("web")
def deploy():
    git_pull()
    update_requirements()
    migrate()
    collect_static()
    restart()
