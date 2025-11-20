class Product:
    def __init__(self,title, price, year):
        self.title = title
        self.price = int(price)
        self.year = int(year)



class Phone(Product):
    def __init__(self,title, price, year, memory, camera):
        super().__init__(title, price, year)
        self.memory = memory
        self.camera = camera
        self.type = 'phone'


class Tv(Product):
    def __init__(self,title, price, year, size, tv_type):
        super().__init__(title, price, year)
        self.size = size
        self.types = tv_type
        self.type = 'tv'


class PC(Product):
    def __init__(self,title, price, year, cpu, ram):
        super().__init__(title, price, year)
        self.cpu = cpu
        self.ram = ram
        self.type = 'pc'


class Store:
    def __init__(self, name):
        self.base = []
        self.name = name

    def add_items(self):
        while True:
            print('\nWhat do you want to add?\n1. Phone\n2. TV\n3. PC\n4. Return')
            code = input('> ')

            if code == '1':
                p = Phone(
                    input('title: '),
                    input('price: '),
                    input('year: '),
                    input('memory: '),
                    input('camera: ')
                )
                self.base.append(p)
                print("Phone added!\n")

            elif code == '2':
                p = Tv(
                    input('title: '),
                    input('price: '),
                    input('year: '),
                    input('size: '),
                    input('type: ')
                )
                self.base.append(p)
                print("TV added!\n")

            elif code == '3':
                p = PC(
                    input('title: '),
                    input('price: '),
                    input('year: '),
                    input('cpu: '),
                    input('ram: ')
                )
                self.base.append(p)
                print("PC added!\n")

            else:
                break

    def view_items(self):
        while True:
            print('\nView items:\n1. Phone\n2. TV\n3. PC\n4. Return')
            code = input('> ')

            if code == '1':
                for i in self.base:
                    if i.type == 'phone':
                        print(f"{i.title} | {i.price}$ | {i.year} | {i.memory}GB | {i.camera}MP")

            elif code == '2':
                for i in self.base:
                    if i.type == 'tv':
                        print(f"{i.title} | {i.price}$ | {i.year} | {i.size}\" | {i.types}")

            elif code == '3':
                for i in self.base:
                    if i.type == 'pc':
                        print(f"{i.title} | {i.price}$ | {i.year} | {i.cpu} | {i.ram}GB")

            else:
                break

    def delete_items(self):
        title = input('Enter title to delete: ')
        removed = False

        for item in self.base[:]:
            if item.title == title:
                self.base.remove(item)
                removed = True

        print("Deleted!" if removed else "Item not found!")

    def manager_store(self):
        while True:
            print('\n*** Manager Store ***')
            print('1. Add items\n2. View items\n3. Delete items\n4. Exit')

            code = input('> ')
            if code == '1':
                self.add_items()
            elif code == '2':
                self.view_items()
            elif code == '3':
                self.delete_items()
            else:
                print('Goodbye!')
                break
if __name__ == '__main__':
    store = Store('AX7 store')
    store.manager_store()