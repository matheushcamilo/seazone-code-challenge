import sys
import os
from invoke import task

PROJECT_NAME = "seazone"


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


@task
def prepare_environment(ctx):
    """Prepare environment for tests"""
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} kill")
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} build")
    run_command(ctx, f"docker-compose --project-name {PROJECT_NAME} up -d")


@task
def prepare_db_for_tests(ctx):
    """Prepare the database for tests"""
    run_command(ctx, "python manage.py reset_db --noinput")
    run_command(ctx, "python manage.py migrate")
    load_data(ctx)
    run_command(ctx, "python manage.py create_admin_user")


@task
def run_tests(ctx):
    """Run tests"""
    run_command(ctx, "python manage.py test")
