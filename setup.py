import sys
from pathlib import Path

from setuptools import setup, find_namespace_packages

if sys.version_info[0:2] < (3, 6):
    raise RuntimeError("This package requires Python 3.6+.")

setup(
    name="moat-main",
    use_scm_version={"version_scheme": "guess-next-dev", "local_scheme": "dirty-tag"},
    packages=find_namespace_packages(include=['moat.*']),
    url="https://github.com/M-o-a-T/moat-main",
    license="MIT",
    author="Matthias Urlichs",
    author_email="<matthias@urlichs.de>",
    description="The MoaT command line",
    long_description=Path(__file__).with_name("README.rst").read_text(encoding="utf-8"),
    setup_requires=["setuptools_scm", "pytest-runner"],
    tests_require=["pytest-trio"],
    install_requires=[
        "anyio>=3.0",
        "moat-util",
        "asyncclick",
    ],
    extras_require={},
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Framework :: AnyIO",
        "Framework :: AsyncIO",
        "Framework :: Trio",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
    ],
    entry_points="""
    [console_scripts]
    moat = moat.main:cmd
    """,
)