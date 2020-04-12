import os
import shutil


class Sort:
    def __init__(self, path):
        self.extensions = []
        self.path = path
        self.extension()
        self.create_folder()
        self.move()

    def list_of_items(self):
        for i in os.listdir(self.path):
            print(i)

    def extension(self):
        for i in os.listdir(self.path):
            if os.path.isfile(self.path + f"/{i}"):
                self.extensions.append(i.split('.')[-1])
        self.extensions = list(set(self.extensions))

    def create_folder(self):
        for i in self.extensions:
            if not os.path.exists(self.path + f"/{i}/"):
                os.mkdir(self.path + f"/{i}/")
                print("Directory ", i, " Created ")
            else:
                print("Directory ", i, " already exists")

    def move(self):
        for i in os.listdir(self.path):
            for j in self.extensions:
                if ('.' in i) and (j in i):
                    try:
                        shutil.move(self.path + f"/{i}", self.path + f"/{j}/{i}")
                    except FileNotFoundError:
                        pass


def main():
    name = input("Path: ")
    while not os.path.isdir(name):
        print("Please enter valid path: ")
        name = input("Path: ")
    x = Sort(name)


if __name__ == "__main__":
    main()



