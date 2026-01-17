from program1 import emp
def test_emp():
    expected_output=(
        "employee name:Alice\n"
        "employee id:FE041\n"
        "department:Engineering\n"
        "salary:500000\n"
    )
    assert emp("Alice","FE041","Engineering",500000) == expected_output
