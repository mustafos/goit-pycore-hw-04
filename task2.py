
def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age,
                }

                cats_info.append(cat)

        return cats_info

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

    except (ValueError, OSError) as error:
        print(f"Error reading cats file: {error}")
        return []


if __name__ == "__main__":
    cats = get_cats_info("cats_file.txt")
    print(cats)
