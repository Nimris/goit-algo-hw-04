def get_cats_info(path: str) -> list:
    result = []
    try:
        with open(path, 'r', encoding = 'UTF-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    result.append({"id": id, "name": name, "age": int(age)})
                except ValueError:
                    print(f"Skipping invalid line: {line}")
            
            print(result)
            return result
        
    except FileNotFoundError:
        print("Error 404")
        return []
        
get_cats_info("cats.txt")