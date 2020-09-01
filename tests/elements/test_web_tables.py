import pytest


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/webtables')


def test_add_user(py, demo_qa):
    py.get('#addNewRecordButton').click()
    py.get('#firstName').type('Daniel')
    py.get('#lastName').type('Floyd')
    py.get('#userEmail').type(py.fake.email())
    py.get('#age').type('20')
    py.get('#salary').type('100000')
    py.get('#department').type(py.fake.job())
    py.get('#submit').click()
    assert py.get('.rt-tbody').should().contain_text('Daniel')


# py.wait(use_py=True).sleep(5)
