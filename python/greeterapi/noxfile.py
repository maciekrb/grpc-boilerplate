import os
import nox

# You would normally want test this against the latest version
# of your API protos
LOCAL_DEPS = [os.path.join("..", "proto-build")]


def default(session):
    """Default unit test session.
    This is intended to be run **without** an interpreter set, so
    that the current ``python`` (on the ``PATH``) or the version of
    Python corresponding to the ``nox`` binary the ``PATH`` can
    run the tests.
    """

    # Install all test dependencies
    session.install("pytest", "pytest", "pytest-cov")

    # Instal local deps first
    for local_dep in LOCAL_DEPS:
        session.install("-e", local_dep)

    session.install("-e", ".")

    # Run py.test against the unit tests.
    session.run(
        "py.test",
        "--quiet",
        "--cov=greeterapi",
        "--cov=tests.unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",  # No output just yet
        "tests/unit",
        *session.posargs
    )


@nox.session(python=["3.6", "3.7"])
def unit(session):
    default(session)


@nox.session(python=["3.6"])
def system(session):
    """Run the system test suite."""

    # Sanity check: Only run tests if the environment variable is set.
    if not all([os.environ.get("SOME_ENV_VAR")]):
        session.skip("SOME_ENV_VAR must be set via environment variable")

    system_test_folder_path = os.path.join("tests", "system")
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    # Sanity check: only run tests if found.
    if not system_test_folder_exists:
        session.skip("System tests were not found")

    # Install all test dependencies, then install this package into the
    # virtualenv's dist-packages.
    session.install("pytest", "mock")
    for local_dep in LOCAL_DEPS:
        session.install("-e", local_dep)
    session.install("-e", ".")

    # Run py.test against the system tests.
    if system_test_folder_exists:
        session.run("py.test", "--quiet", system_test_folder_path, *session.posargs)


@nox.session(python="3.6")
def cover(session):
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=70")
    session.run("coverage", "erase")


@nox.session(python="3.6")
def lint(session):
    """Run linters.
    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """
    session.install("flake8", *LOCAL_DEPS)
    session.install(".")
    session.run("flake8", "greeterapi", "tests")


@nox.session(python="3.6")
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("docutils", "Pygments")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


@nox.session(python="3.6")
def blacken(session):
    """ Run black.  Format code to uniform standard
    https://github.com/psf/black
    """
    session.install("black")
    session.run("black", "greeterapi", "tests")
