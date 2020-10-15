import pytest
import os
import base64


@pytest.fixture
def demo_qa(py):
    py.visit('https://demoqa.com/upload-download')


def test_file_upload(py, demo_qa):
    FILE = '/Users/gleek/Desktop/development/portfolio/image.png'
    choose_file_button = py.get('#uploadFile')
    choose_file_button.type(FILE)
    assert py.get('#uploadedFilePath').should().contain_text(FILE.split('/')[-1])


def test_file_download(py, demo_qa):
    DOWNLOAD_PATH = '/Users/gleek/Downloads'
    download_button = py.get('#downloadButton')
    file_name = download_button.get_attribute('download')
    download_button.click()

    py.wait(use_py=True).sleep(5)
    file = False
    for file in os.listdir(DOWNLOAD_PATH):
        if file_name in file:
            file = True

    assert file
    # assert os.path.isfile(f"{DOWNLOAD_PATH}/{file_name}")


def test_file_download_no_clicky(py, demo_qa):
    DOWNLOAD_PATH = '/Users/gleek/Downloads'
    download_button = py.get('#downloadButton')
    file_name = download_button.get_attribute('download')
    url = download_button.get_attribute('href')
    image_data = url.split(',')[-1].encode('UTF-8')

    with open(f'{DOWNLOAD_PATH}/{file_name}', "wb") as file:
        file.write(base64.decodebytes(image_data))

    py.wait(use_py=True).sleep(5)
    file = False
    for file in os.listdir(DOWNLOAD_PATH):
        if file_name in file:
            file = True

    assert file
    # assert os.path.isfile(f"{DOWNLOAD_PATH}/{file_name}")


# Websites that helped me
# https://stackoverflow.com/questions/2323128/convert-string-in-base64-to-image-and-save-on-filesystem-in-python
# https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal/6269785
# https://effbot.org/zone/python-with-statement.htm
# https://www.geeksforgeeks.org/with-statement-in-python/
