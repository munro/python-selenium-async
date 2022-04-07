import os


def test():
    os.system("pytest -m 'not integration'")


def test_integration():
    os.system("pytest -m 'integration'")


def doc():
    os.system("sphinx-build source build")


def format():
    os.system("isort .")
    os.system("autoflake -i --remove-all-unused-imports **/*.py")
    os.system("black .")


def push_read_the_docs():
    os.system(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )


def doc_markdown():
    # @TODO this doesn't format correctly...
    os.system("sphinx-build -b markdown source build")
