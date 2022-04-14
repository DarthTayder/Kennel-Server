CUSTOMERS= [
    {
        "id": 1,
        "name": "Customer 1"
    },
    {
        "id": 2,
        "name": "Customer 2"
    },
    {
        "id": 3,
        "name": "Customer 3"
    },
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer