from pylenium.driver import Pylenium


def check_checkbox(py: Pylenium, element: str):
    """
        Element should be Str
        element = "commands"
    """
    py.get(f"#tree-node-{element}").click(force=True)


def toggle(py: Pylenium, element: str):
    """
        Element should be Str and needs to already be visible on page
        Example:
            If Home is currently the only visible element I can't expand anything below Home until I expand Home
            > [] Home

        Example:
        element = "home"
    """
    py.getx(f'//label[@for="tree-node-{element}"]/../button').click()


# def you_have_selected(py: Pylenium, selected: str):
#     py.get('.text-success').should().have_text(selected)


class CheckboxFilters:
    pass
