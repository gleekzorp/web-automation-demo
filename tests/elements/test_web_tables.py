import pytest


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/webtables')