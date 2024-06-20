def total_salary(path: str) -> tuple:
    total = 0
    count = 0
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
                
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    
    average = total / count
    return (total, average)

result = total_salary("salary.txt")
print(f"Total salary: {result[0]}")
print(f"Average salary: {result[1]}")