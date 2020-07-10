

def test_random_id(py):
    py.visit('https://demoqa.com/dynamic-properties')
    py.get('div').contains('This text has random Id')
