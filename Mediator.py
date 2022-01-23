from Storage import Storage


class Mediator:
    storage: Storage
    def __init__(self, storage):
        self.storage = storage

    def remove_from_storage(self, products):
        self.storage.delete_products(products)
        
    def add_to_storage(self, products):
        self.storage.add_products(products)


