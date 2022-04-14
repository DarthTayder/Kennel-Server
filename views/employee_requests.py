EMPLOYEES = [
    {
        "id": 1,
        "name": "Employee 1"
    },
    {
        "id": 2,
        "name": "Employee 2"
    },
    {
        "id": 3,
        "name": "Employee 3"
    },
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee