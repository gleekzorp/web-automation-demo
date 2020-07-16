import pytest


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/radio-button')


def test_yes_radio_button_show_yes(py, demo_qa):
    py.get('#yesRadio').click(force=True)
    assert py.get('.text-success').should().have_text('Yes')


def test_impressive_radio_button_is_selected(py, demo_qa):
    checkbox = py.get('#impressiveRadio')
    checkbox.click(force=True)
    assert checkbox.is_selected()


def test_inject_javascript_to_enable_no_radio_button(py, demo_qa):
    no_no_square = py.get('#noRadio')
    py.execute_script('arguments[0].disabled = false', no_no_square.webelement)
    no_no_square.click(force=True)
    assert no_no_square.is_selected()
