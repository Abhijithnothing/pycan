import pytest
def emp(name,empid,department,salary):
    result=(
        f"employee name:{name}"
        f"employee id:{empid}" 
        f"department:{department}"
        f"salary:{salary}"
    )
    return result
if __name__ =="__main__":
    name="Alice"
    empid="FE041"
    department="Engineering"
    salary=500000
    print(emp(name,empid,department,salary))
