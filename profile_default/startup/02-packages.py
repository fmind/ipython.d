"""Initialize the profile packages."""

FMIND_DEV_PACKAGES = [
    'bandit',
    'black',
    'cookiecutter',
    'coverage',
    'invoke',
    'ipdb',
    'isort',
    'jedi',
    'metrics',
    'mypy',
    'pdoc',
    'profiling',
    'pyinstaller',
    'pylint',
    'pytest',
    'rope',
    'twine',
    'vulture',
    'wheel',
]

FMIND_DATA_PACKAGES = [
    'csvkit',
    'dask',
    'glom',
    'numpy',
    'pandas',
    'pint',
    'plotly',
    'sklearn',
    'statsmodels',
    'streamlit',
    'xgboost',
]

FMIND_ADMIN_PACKAGES = [
    'PyGithub',
    'ansible',
    'chardet',
    'glances',
    'howdoi',
    'litecli',
    'psutil',
    'ptrepl',
    'pyinfra',
    'ranger',
    'schedule',
    'sh',
    'supervisor'
    'tqdm',
    'watchdog',
]

FMIND_JUPYTER_PACKAGES = [
    'RISE',
    'ipywidgets',
    'jupyterlab',
    'jupytext',
    'nbconvert'
    'nbformat',
    'papermill',
    'voila',
]

FMIND_NETWORK_PACKAGES = [
    'httpie',
    'requests',
    'scapy',
    'scrapy',
    'youget',
]

FMIND_GRAPHIC_PACKAGES = [
    'diagrams',
    'manimlib',
]

FMIND_PARALLEL_PACKAGES = [
    'ipyparallel',
]

FMIND_AUTOMATION_PACKAGES = [
    'pyautogui',
    'splinter',
]

FMIND_EVERYTHING_PACKAGES = [
    package
    for packages in [
        FMIND_DEV_PACKAGES,
        FMIND_DATA_PACKAGES,
        FMIND_ADMIN_PACKAGES,
        FMIND_JUPYTER_PACKAGES,
        FMIND_NETWORK_PACKAGES,
        FMIND_GRAPHIC_PACKAGES,
        FMIND_PARALLEL_PACKAGES,
        FMIND_AUTOMATION_PACKAGES,
    ]
    for package in packages
]
