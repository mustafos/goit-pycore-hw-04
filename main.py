
def total_salary(path):
    total = 0
    developers_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary)
                developers_count += 1

        if developers_count == 0:
            return 0, 0

        average = total / developers_count
        return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0

    except (ValueError, OSError) as error:
        print(f"Error reading salary file: {error}")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Total salary: {total}")
    print(f"Average salary: {average}")
