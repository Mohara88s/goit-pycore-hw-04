from pathlib import Path
current_dir = Path(__file__).parent

def total_salary(path:str)->tuple:
    total_sal = 0
    average_sal = 0
    path_to_file = Path(path)
    if not path_to_file.is_absolute():
        path_to_file = current_dir / path_to_file
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            devs = file.readlines()  
            for dev in devs:
                total_sal = total_sal + float(dev.split(',')[1])
            average_sal = total_sal / len(devs)
    except FileNotFoundError:
        print("Can't gat file with salaries.")
    return (int(total_sal), int(average_sal))
    

if __name__ == "__main__":
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    total, average = total_salary("salary/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    total, average = total_salary("D:/Mohara/GitHub/goit-pycore-hw-04/task1/salary/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
