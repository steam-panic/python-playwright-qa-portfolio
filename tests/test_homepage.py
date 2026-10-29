
def test_homepage_title(page):
    page.goto("https://the-internet.herokuapp.com/")

    assert page.title() == "The Internet"
