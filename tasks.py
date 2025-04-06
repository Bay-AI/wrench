from invoke import task


@task
def install(ctx):
    """
    Installs dependencies using Poetry.
    """
    # Executes 'poetry install'
    ctx.run("poetry install --with dev", pty=True)


@task
def fix(ctx):
    """
    Formats and lints the code using ruff with autofix enabled.
    """
    # The command applies ruff autofix to all files in the current directory.
    ctx.run("poetry run ruff check wrench tests --fix", pty=True)


@task
def format(ctx):
    """
    Formats and lints the code using ruff with autofix enabled.
    """
    # The command formats
    ctx.run("poetry run ruff format wrench tests", pty=True)


@task
def test(ctx):
    """
    Runs tests using pytest via Poetry.
    """
    # Executes 'pytest' within the Poetry environment.
    ctx.run("poetry run pytest -rP tests/", pty=True)
