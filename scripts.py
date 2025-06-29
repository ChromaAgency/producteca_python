import subprocess

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    return subprocess.run(
        ['python', '-m', 'unittest', 'discover',  '-p', 'test_*.py'],
    ).returncode


def get_coverage():
    """
    Get the coverage report of the project to know how much are we unit testing.
    We omit tests, odoo, and main, as they are tests, odoo connection files (which we dont test), and the main file,
    which is the entry point of the project and does not run any business logic code, just gives info to user.
    ``
    """
    subprocess.run(
        ['coverage', 'run', '-m', 'unittest', 'discover',  '-p', 'test_*.py'],
    )
    subprocess.run(
        ['coverage', 'xml', "--omit=test*.py,*/tests/*"],
    )
    
    with open("coverage.md", "w") as f:
        subprocess.run(
            ['coverage', 'report', "--format=markdown", "--omit=test*.py,*/tests/*"],
            stdout=f,
        )
    

def generate_html_coverage():
    """
    Get the coverage report of the project to know how much are we unit testing.
    We omit tests, odoo, and main, as they are tests, odoo connection files (which we dont test), and the main file,
    which is the entry point of the project and does not run any business logic code, just gives info to user.
    ``
    """
    subprocess.run(
            ['coverage', 'html', "--omit=test*.py,*/tests/*"],
        )
