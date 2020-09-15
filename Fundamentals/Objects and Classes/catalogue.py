class Catalogue:

    def __init__(self, name_):
        self.name = name_
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        self.return_list = []
        for p in self.products:
            if p[0] == first_letter:
                self.return_list.append(p)
        return self.return_list

    def __repr__(self):
        self.list = ('\n').join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{self.list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)