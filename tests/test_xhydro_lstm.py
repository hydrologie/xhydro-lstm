#!/usr/bin/env python
"""Tests for `xhydro_lstm` package."""

from __future__ import annotations

import pathlib
from importlib.util import find_spec

# import pytest


# @pytest.fixture
# def response():
#     """Sample pytest fixture.
#
#     See more at: https://doc.pytest.org/en/latest/explanation/fixtures.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_package_metadata():
    """Test the package metadata."""
    project = find_spec("xhydro_lstm")

    assert project is not None
    assert project.submodule_search_locations is not None
    location = project.submodule_search_locations[0]

    metadata = pathlib.Path(location).resolve().joinpath("__init__.py")

    with metadata.open() as f:
        contents = f.read()
        assert """Richard Arsenault""" in contents
        assert '__email__ = "Richard.Arsenault@etsmtl.ca"' in contents
        assert '__version__ = "0.1.1"' in contents
