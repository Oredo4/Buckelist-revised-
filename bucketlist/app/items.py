class Items(object):
    allitems = []

    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = None

    def create_item(self):
        name = input("enter name: ")
        item = Item(name)
        self.allitems.append(item)

    def edit_item(self, name=None):
        new_name = input("enter new bucketlist name: ")
        for i in self.allitems:
            if i.name == name:
                i.name = new_name

    def delete_item(self):
        name = input("enter bucketlist name: ")
        for i in self.allitems:
            if i.name == name:
                self.allitems.remove(i)

    def print_details(self):
        for i in self.allitems:
            print(i.name)