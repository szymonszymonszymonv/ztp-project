from Storage import Storage


class Mediator:
    storage: Storage
    def __init__(self, storage):
        self.storage = storage

    def remove_from_storage(self, products):
        print(f'stan przed usunieciem:\n{self.storage.get_products()}')
        self.storage.delete_products(products)
        print(f'stan po usunieciu:\n{self.storage.get_products()}')
        
    def add_to_storage(self, products):
        print(f'stan przed dodaniem:\n{self.storage.get_products()}')
        self.storage.add_products(products)
        print(f'stan po dodaniu:\n{self.storage.get_products()}')


