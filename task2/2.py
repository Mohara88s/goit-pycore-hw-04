from pathlib import Path
current_dir = Path(__file__).parent

def get_cats_info(path:str)->list[dict]:
    list_of_cats=[]
    path_to_file = Path(path)
    if not path_to_file.is_absolute():
        path_to_file = current_dir / path_to_file
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            cats = [el.strip() for el in file.readlines()]
            for cat in cats:
                cat = cat.split(',')
                list_of_cats.append({
                    "id":cat[0],
                    "name":cat[1],
                    "age":cat[2],
                })
    except FileNotFoundError:
        print("Can't gat file with cats.")
    return list_of_cats






if __name__ == "__main__":
    cats_info = get_cats_info("path/to/cats_file.txt")
    print(cats_info)
    cats_info = get_cats_info("cats/cats_file.txt")
    print(cats_info)
    cats_info = get_cats_info("D:/Mohara/GitHub/goit-pycore-hw-04/task2/cats/cats_file.txt")
    print(cats_info)