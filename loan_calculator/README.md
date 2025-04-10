# Loan Calculator
This is a Django-based loan calculator app

## Project Set

### Prerequsites
- Python 3.11 
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Import the project:**    
    - Unzip project loan_calculator.zip file.
    - cd loan_calculator   

2. **Install the required packages:**    
    - pip3 install -r requirements.txt

3. **Apply database migrations:**
    *(Required in case tables are missing. The data and tables might be already part of the package)* 
    - python3 manage.py migrate

4. **Run the development server:**    
    - python3 manage.py runserver

5. **Run tests:**    
    - python3 manage.py test 


### API Endpoints

- **Create Loan Scenario:** `POST /api/loan_scenarios/`
- **List Loan Scenarios:** `GET /api/loan_scenarios/`
- **Retrieve Loan Scenario:** `GET /api/loan_scenarios/<id>/`
- **Update Loan Scenario:** `PUT /api/loan_scenarios/<id>/`
- **Delete Loan Scenario:** `DELETE /api/loan_scenarios/<id>/`    


