# Web Automation Demo

- Carlos Kidman invited his students at Autobots to create a portfolio with various web automation examples based on a post from Angie Jones
  - [10-portfolio-projects](https://techbeacon.com/app-dev-testing/10-portfolio-projects-aspiring-automation-engineers)
  - [QAP/Autobots Website](https://www.qap.dev/autobots)
  - [QAP/Autobots Slack](https://join.slack.com/t/qautah/shared_invite/zt-4cbb6q78-J8opsCMlPqOKdef42x9kUw)
  - [Carlos Kidmans Twitch](https://www.twitch.tv/carloskidman)

> The challenges are completed in class as a group, solo, and homework

# Setup Your Own Project

- Download Python at https://www.python.org/downloads/
  > Don't forget to check add python to PATH while installing
- Download Pycharm at https://www.jetbrains.com/pycharm/

### Create a new project via Pycharm

- Open `Pycharm`
- Click `Create New Project`
- Click `Project Interpreter: New Virtualenv Environment`
  - Make sure `radio button for New environment using` is checked and is using `Virtualenv`
- Click `Create`

### Setup folder for testing with Pytest and Pyleniumio

- Open the `Terminal` at the bottom of the screen
  > make sure it says (venv)
- Install pyleniumio
  - `(venv)$ pipenv install pyleniumio`
  - `(venv)$ pylenium init`
    - If this worked correctly you should have three new files `conftest.py`, `pylenium.json`, `pytest.ini`
- Setup the project to use pytest
  - Click `PyCharm` from the toolbar at the top left
  - Click `Preferences..` on `MAC` or `Settings` on `PC`
  - Click `Tools`
  - Click `Python Integrated Tools`
  - Change `Default Test Runner` to `pytest`
  - Click `OK`

### Setup a test folder
- `Right Click` on your web-automation-demo folder on the top left of the screen
- Click on `new`
- Click on `Directory`
- Name that new Directory `tests`
- `Right Click` on the newly created `tests` folder
- Click on `new`
- Click on `Directory`
- Name that new Directory `elements`

### Setup a test file
- `Right Click` on your `tests` folder
- Click on `new`
- Click on `File`
- Name that new File `test_text_boxes.py`
- Add the following code and click the green Play button
```python

def test_google(py):
    py.visit('https://www.google.com')
    assert 'Google' in py.title()

```
- Your test should have passed and your all setup to start doing the challenges

If you have any questions or this didn't work please reach out to anyone on the QAP/Autobots slack channel.

[Join QAP/Autobots Slack](https://join.slack.com/t/qautah/shared_invite/zt-4cbb6q78-J8opsCMlPqOKdef42x9kUw)


# Current Challenges
> website we tested against: https://demoqa.com
- **Elements**
  - [001 Text Boxes](#001-text-boxes)
  - [002 Radio Buttons](#002-radio-buttons)
  - [003 Check Boxes](#003-check-boxes)
  - [004 Dynamic Properties](#004-dynamic-properties)
  - [005 Upload and Download](#005-upload-and-download)
  - [006 Web Tables](#006-web-tables)



# Challenge Description Images

## 001 Text Boxes
[![001-text-boxes](challenges/elements/001-text-box.png "001 Challenge Text Boxes")](challenges/elements/001-text-box.png)
## 002 Radio Buttons
[![002-radio-buttons](challenges/elements/002-radio-buttons.png "002 Challenge Radio Buttons")](challenges/elements/002-radio-buttons.png)
## 003 Check Boxes
[![003-check-boxes](challenges/elements/003-check-boxes.png "003 Challenge Check Boxes")](challenges/elements/003-check-boxes.png)
## 004 Dynamic Properties
[![004-dynamic-properties](challenges/elements/004-dynamic-properties.png "004 Challenge Dynamic Properties")](challenges/elements/004-dynamic-properties.png)
## 005 Upload and Download
[![005-upload-and-download](challenges/elements/005-upload-and-download.png "005 Upload and Download")](challenges/elements/005-upload-and-download.png)
## 006 Web Tables
[![006-web-tables](challenges/elements/006-web-tables.png "006 Web Tables")](challenges/elements/006-web-tables.png)
