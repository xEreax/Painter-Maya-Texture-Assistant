## Running Tests Locally
### Prerequisites
- python version >= 3.9
- Navigated to project in the terminal

### Create virtual environment
**In Windows terminal:**
 - Create virtual environment by running
`py -m venv venv`

- Activate environment by running
`venv\Scripts\activate`

- Install third party packages by running 
`python -m pip install -r tests/requirements.txt`

### Run tests
- Run python tests with maya version number of 
`python run_tests.py -m <maya_version_number>`

### Close virtual environment

run `deactivate`

### Delete virtual environment
run `rm -r venv `



