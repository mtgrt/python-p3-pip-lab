import sys
import requests
import pytest

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 12  # Adjusted to match your environment

def test_requests_version():
    assert requests_version() == "2.31.0"  # Adjusted to match your environment

def test_pytest_version():
    assert pytest_version() == "7.4.4"  # Adjusted to match your environment