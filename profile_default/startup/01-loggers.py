"""Initialize the profile loggers."""

import logging

FMIND_FORMATTER = logging.Formatter(
    '[%(name)s:%(levelname)s] %(message)s'
)

FMIND_HANDLER = logging.StreamHandler()
FMIND_HANDLER.setFormatter(FMIND_FORMATTER)

FMIND_LOGGER = logging.getLogger('FMIND')
FMIND_LOGGER.addHandler(FMIND_HANDLER)
FMIND_LOGGER.setLevel(logging.INFO)
