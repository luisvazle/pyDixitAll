import xml.etree.ElementTree as ET
import os


class DataManager:
    def __init__(self, file_path):
        self.tree = None
        self.root = None
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            root = ET.Element("terms")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)

        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

    def add_term(self, term, definition):
        term_element = ET.Element("term", name=term)
        term_element.text = definition
        self.root.append(term_element)
        self.tree.write(self.file_path)

    def modify_term(self, term, definition):
        for term_element in self.root.findall("term"):
            if term_element.get("name") == term:
                term_element.text = definition
                self.tree.write(self.file_path)
                return True
        return False

    def delete_term(self, term):
        for term_element in self.root.findall("term"):
            if term_element.get("name") == term:
                self.root.remove(term_element)
                self.tree.write(self.file_path)
                return True
        return False

    def get_definition(self, term):
        for term_element in self.root.findall("term"):
            if term_element.get("name") == term:
                return term_element.text
        return None

    def get_all_terms(self):
        return [term_element.get("name") for term_element in self.root.findall("term")]
