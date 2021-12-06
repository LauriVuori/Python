import csv


class csv_class:
    """
    Class description:
    -----------------
    this is class

    Brief:
    -----------------
    This class does

    Attributes:
    -----------------
    this_is_list : list

    Methods:
    -----------------
    read
    write
    create
    find colum
    print csv user to see whats in it
    get data from colum
    """
    def __init__(self, filename="example.csv", delimeter=";"):
        self.filename = filename
        self.delimeter = delimeter
        self.__open_ifnot_create_csv()

    def set_filename(self, filename):
        self.filename = filename

    def get_filename(self):
        print("Current file name is: " + self.filename)
    
    def __open_ifnot_create_csv(self):
        try:
            new_file = open(self.filename, "r")
            print("File found", self.filename)
        except FileNotFoundError:
            new_file = open(self.filename, "wb")
            print("Created file: ", new_file.name)
        new_file.close()
        # with open(self.filename, "wb") as csvfile:
            
# with open('eggs.csv', newline='') as csvfile:
# ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# ...     for row in spamreader:
# ...         print(', '.join(row))

test = csv_class()


