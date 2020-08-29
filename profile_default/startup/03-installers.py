"""Initialize the profile installers."""


def fmind_install(*packages: list, as_user: bool = False):
    """Install a list of python packages using pip."""
    for package in packages:
        FMIND_LOGGER.info("Installing pip package: '%s'", package)
        ipython.magic(f"pip install {'--user' if as_user else ''} {package}")


def fmind_uninstall(*packages: list, as_user: bool = False):
    """Uninstall a list of python packages using pip."""
    for package in packages:
        FMIND_LOGGER.info("Installing pip package: '%s'", package)
        ipython.magic(f"pip uninstall {'--user' if as_user else ''} {package}")
