import pytest

from pages import checkbox_page


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/checkbox')


def test_checkboxes(py, demo_qa):
    py.getx('//label[@for="tree-node-home"]/../button').click()
    py.getx('//label[@for="tree-node-desktop"]/../button').click()
    commands = py.get('#tree-node-commands')
    commands.click(force=True)

    # This says it isn't a checkbox or radio button
    # assert commands.is_checked()
    assert py.get('.text-success').should().have_text('commands')

    # Doesn't work since you need the whole class name
    # assert py.getx('//*[@for="tree-node-home"]/span[1]/*[name()="svg"]').should().have_class('rct-icon-half-check')
    # assert py.getx('//*[@for="tree-node-desktop"]/span[1]/*[name()="svg"]').should().have_class('rct-icon-half-check')
    assert py.getx('//label[@for="tree-node-home"]/span[1]/*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')
    assert py.getx('//label[@for="tree-node-desktop"]/span[1]/*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')


def test_checkboxes_refactor(py, demo_qa):
    checkbox_page.toggle(py, "home")
    checkbox_page.toggle(py, "desktop")
    checkbox_page.check_checkbox(py, "commands")

    assert py.get('.text-success').should().have_text('commands')
    assert py.getx('//label[@for="tree-node-home"]/span[1]/*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')
    assert py.getx('//label[@for="tree-node-desktop"]/span[1]/*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')


def test_checkboxes_expand_all(py, demo_qa):
    py.getx('//button[@title="Expand all"]').click()
    py.get('#tree-node-commands').click(force=True)

    assert py.get('.text-success').should().have_text('commands')
    assert py.getx('//label[@for="tree-node-home"]//*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')
    assert py.getx('//label[@for="tree-node-desktop"]//*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')


def test_checkboxes_expand_all_check_any_collapse_all_expand_all(py, demo_qa):
    py.getx('//button[@title="Expand all"]').click()
    py.get('#tree-node-react').click(force=True)
    checkbox_page.toggle(py, "home")
    checkbox_page.toggle(py, "home")

    assert py.get('.text-success').should().have_text('react')
    assert py.getx('//label[@for="tree-node-home"]//*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')
    assert "half-check" in py.getx('//label[@for="tree-node-documents"]//*[name()="svg"]').get_attribute('class')
    # OR
    assert py.getx('//label[@for="tree-node-workspace"]//*[name()="svg"]').should().have_class(
        'rct-icon rct-icon-half-check')


def test_check_random_elements(py, demo_qa):
    checkbox_list = ['notes', 'react', 'general']
    py.getx('//button[@title="Expand all"]').click()
    for item in checkbox_list:
        print(item)
        checkbox_page.check_checkbox(py, item)



# '//label[@for="tree-node-home"]/../button'
# '//span[@class="rct-text"]/button'
