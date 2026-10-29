
def test_homepage_title(homepage):
#header text on the homepage
    assert homepage.title() == "The Internet"


def test_homepage_subtitles(homepage):
#subheader text on the homepage
    assert homepage.locator("h1").text_content() == "Welcome to the-internet"
    assert homepage.locator("h2").text_content() == "Available Examples"

def test_homepage_links(homepage):
#list of links on the homepage
    assert homepage.locator("a[href='/abtest']").text_content() == "A/B Testing"
    assert homepage.locator("a[href='/add_remove_elements/']").text_content() == "Add/Remove Elements"
    assert homepage.locator("a[href='/basic_auth']").text_content() == "Basic Auth"
    assert homepage.locator("a[href='/broken_images']").text_content() == "Broken Images"
    assert homepage.locator("a[href='/challenging_dom']").text_content() == "Challenging DOM"
    assert homepage.locator("a[href='/checkboxes']").text_content() == "Checkboxes"
    assert homepage.locator("a[href='/context_menu']").text_content() == "Context Menu"
    assert homepage.locator("a[href='/digest_auth']").text_content() == "Digest Authentication"
    assert homepage.locator("a[href='/disappearing_elements']").text_content() == "Disappearing Elements"
    assert homepage.locator("a[href='/drag_and_drop']").text_content() == "Drag and Drop"
    assert homepage.locator("a[href='/dropdown']").text_content() == "Dropdown"
    assert homepage.locator("a[href='/dynamic_content']").text_content() == "Dynamic Content"
    assert homepage.locator("a[href='/dynamic_controls']").text_content() == "Dynamic Controls"
    assert homepage.locator("a[href='/dynamic_loading']").text_content() == "Dynamic Loading"
    assert homepage.locator("a[href='/entry_ad']").text_content() == "Entry Ad"
    assert homepage.locator("a[href='/exit_intent']").text_content() == "Exit Intent"
    assert homepage.locator("a[href='/download']").text_content() == "File Download"
    assert homepage.locator("a[href='/upload']").text_content() == "File Upload"
    assert homepage.locator("a[href='/floating_menu']").text_content() == "Floating Menu"
    assert homepage.locator("a[href='/forgot_password']").text_content() == "Forgot Password"
    assert homepage.locator("a[href='/login']").text_content() == "Form Authentication"
    assert homepage.locator("a[href='/frames']").text_content() == "Frames"
    assert homepage.locator("a[href='/geolocation']").text_content() == "Geolocation"
    assert homepage.locator("a[href='/horizontal_slider']").text_content() == "Horizontal Slider"
    assert homepage.locator("a[href='/hovers']").text_content() == "Hovers"
    assert homepage.locator("a[href='/infinite_scroll']").text_content() == "Infinite Scroll"
    assert homepage.locator("a[href='/inputs']").text_content() == "Inputs"
    assert homepage.locator("a[href='/jqueryui/menu']").text_content() == "JQuery UI Menus"
    assert homepage.locator("a[href='/javascript_alerts']").text_content() == "JavaScript Alerts"
    assert homepage.locator("a[href='/javascript_error']").text_content() == "JavaScript onload event error"
    assert homepage.locator("a[href='/key_presses']").text_content() == "Key Presses"
    assert homepage.locator("a[href='/large']").text_content() == "Large & Deep DOM"
    assert homepage.locator("a[href='/windows']").text_content() == "Multiple Windows"
    assert homepage.locator("a[href='/nested_frames']").text_content() == "Nested Frames"
    assert homepage.locator("a[href='/notification_message']").text_content() == "Notification Messages"
    assert homepage.locator("a[href='/redirector']").text_content() == "Redirect Link"
    assert homepage.locator("a[href='/download_secure']").text_content() == "Secure File Download"
    assert homepage.locator("a[href='/shadowdom']").text_content() == "Shadow DOM"
    assert homepage.locator("a[href='/shifting_content']").text_content() == "Shifting Content"
    assert homepage.locator("a[href='/slow']").text_content() == "Slow Resources"
    assert homepage.locator("a[href='/tables']").text_content() == "Sortable Data Tables"
    assert homepage.locator("a[href='/status_codes']").text_content() == "Status Codes"
    assert homepage.locator("a[href='/typos']").text_content() == "Typos"
    assert homepage.locator("a[href='/subdirectories']").text_content() == "Subdirectories"
    assert homepage.locator("a[href='/two_factor']").text_content() == "Two-Factor Login"
    assert homepage.locator("a[href='/tinymce']").text_content() == "WYSIWYG Editor"

def test_homepage_links_count(homepage):
    assert homepage.locator("li a[href]").count() == 51

def test_homepage_footer_text(homepage):
    assert homepage.locator("#page-footer").inner_text().strip() == "Powered by Elemental Selenium and Sauce Labs"

def test_homepage_footer_links(homepage):
    assert homepage.locator("#page-footer a[href='http://elementalselenium.com/']").text_content() == "Elemental Selenium"
    assert homepage.locator("#page-footer a[href='https://saucelabs.com/']").text_content() == "Sauce Labs"