import pytest
from pydantic import BaseModel
from pylenium import Pylenium
from selenium.webdriver.common.keys import Keys


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


def test_build_dictionary(py, demo_qa):
    grid_cells = py.findx('//*[@role="gridcell"]')
    headers = py.findx('//*[@class="rt-resizable-header-content"]')[:-1]
    user_array = []
    new_user = dict()
    n = 6
    user = 0
    y = 0
    for i in range(0, len(grid_cells)):
        if (i + 1) % (n + 1) == 0 and i != 0:
            y = 0
            user += 1
            user_array.append(new_user)
            new_user = dict()
            continue
        new_user[headers[y].text()] = grid_cells[i].text()
        y += 1

# py.wait(use_py=True).sleep(5)
# //*[@role="row"]

# //*[@role="gridcell"]
# 6 ... skip 7th


def test_filter_users_by_email(py, demo_qa):
    email = 'cierra@example.com'
    py.get('#searchBox').type(email, Keys.ENTER)

    rows = py.find("[role='rowgroup']")
    filtered_rows = [row for row in rows if email in row.text()]
    # filtered_rows = []
    # for row in rows:
    #     if email in row.text():
    #         filtered_rows.append(row)
    assert len(filtered_rows) == 1
    assert py.get('.rt-tbody').contains(email)


def test_emails_in_table_are_unique(py, demo_qa):
    email_cells = py.findx("//div[@role='rowgroup']/div//div[4]")
    non_empty_emails = [cell.text() for cell in email_cells if cell.text() != ' ']
    unique_emails = set(non_empty_emails)
    assert len(non_empty_emails) == len(unique_emails)


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str


class WebTable:
    def __init__(self, py: Pylenium):
        self.py = py


    def get_filtered_rows_by_email(self, rows, email):
        return [row for row in rows if email in row.text()]