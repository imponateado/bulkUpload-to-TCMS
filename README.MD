# Bulk Upload and Comment Script

This Python script automates the process of uploading image files to a TCMS (Test Case Management System) server and adds them as comments in test executions. It uses the `tcms_api` package to interact with the TCMS system.

## Features
- **Bulk Image Upload**: Scans a specified directory for image files (`.png`, `.jpg`, `.jpeg`, `.gif`) and uploads them to the TCMS.
- **Add Comments to Test Executions**: Adds the uploaded image as a comment in the specified test execution, embedding it using markdown.
- **Supports Authentication**: Connects to the TCMS using a username and password provided as arguments.

## Prerequisites
- **Python 3.x** installed on your machine.
- **`tcms_api` package**: Install it using:
  ```bash
  pip install tcms-api
  ```
- A valid TCMS server URL and user credentials.

## Usage
Run the script with the following arguments:

```bash
python bulkUpload.py <username> <password> <execution_run_id> <image_directory>
```

### Arguments:
- `<username>`: Your TCMS username.
- `<password>`: Your TCMS password.
- `<execution_run_id>`: The ID of the test execution run where the comments will be added.
- `<image_directory>`: The directory containing image files to be uploaded.

### Example:
```bash
python bulkUpload.py test_user test_password 1234 /path/to/images
```

## Script Workflow
1. **Authenticate with TCMS**: Logs in using the provided credentials.
2. **Upload Images**: Encodes each image file in Base64 and uploads it to the TCMS.
3. **Add Comments**: Generates a markdown-formatted comment with the uploaded image's URL and adds it to the specified test execution.

## Error Handling
The script handles errors during:
- File upload: Displays an error message if the upload fails.
- Comment addition: Logs an error if unable to add a comment to the test execution.

## Notes
- Ensure the `image_directory` contains only supported image formats.
- Modify the `url` variable in the script to match your TCMS server endpoint.

## Supported Methods
The script relies on the `tcms_api` package and supports several TCMS functionalities, including but not limited to:
- `User.add_attachment`
- `TestExecution.add_comment`

A full list of supported methods is included in the script comments for reference.

## Limitations
- This script is tailored for use with TCMS systems (e.g., Kiwi TCMS).
- Assumes a functional and accessible TCMS API endpoint.
