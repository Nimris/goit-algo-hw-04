def total_salary(path: str) -> tuple:
    total = 0
    amount = 0
    
    try:
        with open(path, "r", encoding = "UTF-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                
                total += int(salary)
                amount += 1
                
            average = total/amount
               
            print(f"Total: {total}\nAverage: {average}")   
            return (total, average)
        
    except FileNotFoundError:
        print("File not Found")
        return (0, 0)

total_salary("salary.txt")