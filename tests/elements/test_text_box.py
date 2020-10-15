

def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get('#userName').type('Daniel Floyd')
    py.get("#userEmail").type('test@test.com')
    py.get('#currentAddress').type('123 street address')
    py.get('#permanentAddress').type(py.fake.address())
    py.get('#submit').click()
    assert py.get('p[id="name"]').should().contain_text('Daniel Floyd')


# Refactor Code
def test_submit_form_refactored(py):
    pass
