from invoke import task

@task
def start(ctx):
    ctx.run("PYTHONPATH=src python3 src/index.py", pty=True)

@task
def build(ctx):
    ctx.run("PYTHONPATH=src python3 src/build.py", pty=True)

@task
def test(ctx):
    ctx.run("PYTHONPATH=src pytest src", pty=True)

@task
def lint(ctx):
    ctx.run("PYTHONPATH=src pylint src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def coverage(ctx):
    ctx.run("PYTHONPATH=src coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

