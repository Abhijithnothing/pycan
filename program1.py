def emp(name, empid, department, salary):
    return (
        f"employee name:{name}\n"
        f"employee id:{empid}\n"
        f"department:{department}\n"
        f"salary:{salary}\n"
    )

if __name__ == "__main__":
    print(emp("Alice", "FE041", "Engineering", 500000))
