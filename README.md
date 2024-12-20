# About

Short POC on pants

# Installation

Use the following command to install:

    pip install elevait-pants-poc

# Python Version

The project is build and tested with python version 3.12.
# Docker

This project can be run in a docker container.
Docker compose is used to manage building and running the container.

## Build & Run

Before building the container the first time make sure that:
- The environment variable `PIP_INDEX_URL` is set to the internal [pypi server](https://start.1password.com/open/i?a=ZYEYIJWE2ZFEBMKC4U2M7BTXPY&v=6thpfxq7rrx5jsr7kiog6vxpgq&i=a6h2ni66kchppnh5affwcjtfqa&h=elevait.1password.com)
- The environment variable `PIP_DEFAULT_TIMEOUT` is set, if you don't want to use the default value `100`

Then you can build and run the image using:

    docker compose up --build

# Pre-commits

In order for the pre-commits to work you have to setup the `UV_INDEX_URL` environment variable to the same value as the `PIP_INDEX_URL` so the `pip-compile` step can work.
