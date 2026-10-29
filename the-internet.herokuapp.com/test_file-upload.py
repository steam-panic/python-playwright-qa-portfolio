from pathlib import Path

def test_file_upload(homepage):
    # Navigate to the file upload page
    homepage.locator("a[href='/upload']").click()

    # Upload a file
    file_input = homepage.locator("#file-upload")
    file_path = Path(__file__).parent.parent / "the-internet.herokuapp.com" / "test-data" / "test_file.txt"
    file_input.set_input_files(str(file_path))

    # Submit the form
    homepage.locator("input[type='submit']").click()

    # Verify that the file was uploaded successfully
    assert homepage.locator("#uploaded-files").text_content().strip() == "test_file.txt"