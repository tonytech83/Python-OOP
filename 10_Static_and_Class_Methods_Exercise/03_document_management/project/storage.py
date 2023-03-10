from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.__find_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.__find_topic_by_id(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.__find_document_by_id(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category = self.__find_category_by_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = self.__find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = self.__find_document_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int) -> Document:
        return self.__find_document_by_id(document_id)

    def __find_category_by_id(self, category_id) -> Category:
        return [c for c in self.categories if c.id == category_id][0]

    def __find_topic_by_id(self, topic_id) -> Topic:
        return [t for t in self.topics if t.id == topic_id][0]

    def __find_document_by_id(self, document_id) -> Document:
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self) -> str:
        return '\n'.join(repr(d) for d in self.documents)
