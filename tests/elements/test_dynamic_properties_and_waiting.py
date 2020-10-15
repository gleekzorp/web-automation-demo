import pytest


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/dynamic-properties')


def test_element_with_dynamic_id_has_text(py, demo_qa):
    demo_qa()
    py.get('div').contains('This text has random Id')


def test_element_with_dynamic_id_has_text_part_two(py, demo_qa):
    assert py.contains('This text has random Id')


def test_element_is_visible_after_5_seconds(py, demo_qa):
    assert py.get('#visibleAfter').should().be_visible()


def test_element_enabled_after_5_seconds(py, demo_qa):
    button = py.get('#enableAfter')
    assert button.should().not_have_attr('disabled')


def test_element_enabled_after_5_seconds_option_two(py, demo_qa):
    assert py.get('#enableAfter').should().not_have_attr('disabled')


def test_element_enabled_after_5_seconds_option_three(py, demo_qa):
    button = py.get('#enableAfter')
    assert py.wait().until(lambda _: button.is_enabled())


def test_color_change_lambda(py, demo_qa):
    button = py.get('#colorChange')
    assert py.wait().until(lambda _: 'danger' in button.get_attribute('class'))


def test_color_change(py, demo_qa):
    button = py.get('#colorChange')
    py.wait(use_py=True).sleep(5)
    assert 'text-danger' in button.get_attribute('class')

