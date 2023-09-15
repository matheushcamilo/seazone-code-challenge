import sys
import os
from invoke import task


def run_command(ctx, cmd, settings_module="seazone.settings"):
    print(f"Executing raw command: {cmd}")
    if sys.platform == "win32":
        return os.system(cmd)
    return ctx.run(
        f'export DJANGO_SETTINGS_MODULE={settings_module} && {cmd}', pty=True
    )


@task
def makemigrations(ctx):
    run_command(ctx, "python manage.py makemigrations")


@task
def migrate(ctx):
    run_command(ctx, "python manage.py migrate")


@task
def load_data(ctx):
    run_command(ctx, "python manage.py loaddata --format=yaml ./fixtures/initial_data.yaml")


@task
def dump_data(ctx):
    run_command(ctx, "python manage.py dumpdata --format=yaml > ./fixtures/initial_data.yaml")


@task
def runserver(ctx):
    run_command(ctx, "python manage.py runserver")
