from data.data_manager import DataManager


class App:
    def __init__(self):
        self.data_manager = DataManager("src/data/data.xml")

    def add_term(self, term, definition):
        self.data_manager.add_term(term, definition)

    def modify_term(self, term, definition):
        self.data_manager.modify_term(term, definition)

    def delete_term(self, term):
        self.data_manager.delete_term(term)

    def get_definition(self, term):
        return self.data_manager.get_definition(term)

    def get_all_terms(self):
        return self.data_manager.get_all_terms()
