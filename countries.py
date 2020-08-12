# we assume that file with countries contains at least one entry
# and all existing entries are valid


def create_dict(file_name):
    my_dict = dict()
    for line in file_name:
        key, value = line.split()
        my_dict[key] = int(value)
    return my_dict


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(key, value)


def add_new(file_name, my_dict, values):
    try:
        my_file = open(file_name, "a")
    except FileNotFoundError:
        print("Impossible to update data")
        quit()
    except IOError:
        print("Fails for an I/O-related reason, try again later")
        quit()

    my_dict[values[0]] = int(values[1])
    my_file.write(' '.join(values))
    my_file.write('\n')
    my_file.close()


def find_biggest(my_dict):
    biggest = None
    res = None
    for key, value in my_dict.items():
        if biggest is None or value > biggest:
            biggest = value
            res = (key, value)
    return res


def find_country_population(name, my_dict):
    return my_dict.get(name, None)


if __name__ == "__main__":
    try:
        file_name = input("Enter file: ")
        if len(file_name) < 1:
            file_name = "countries.txt"
        try:
            file = open(file_name)
        except FileNotFoundError:
            print("No such file or directory")
            quit()

        populations = create_dict(file)

        print_dict(populations)

        new_country = tuple(input("Enter new country name and population: ").split())
        try:
            add_new(file_name, populations, new_country)
        except ValueError:
            print("Population should be a number, entry is not saved")
        except IndexError:
            print("Required data: country name and number of population")

        print_dict(populations)

        biggest_res = find_biggest(populations)
        print("The biggest is %s with population %d" % biggest_res) if biggest_res is not None \
            else print("List of countries is empty")

        country_name = input("Find population by country name: ")
        res = find_country_population(country_name, populations)
        print(res) if res is not None else print("No results")
    except KeyboardInterrupt:
        print("\nProgram interrupted, try again")
        quit()