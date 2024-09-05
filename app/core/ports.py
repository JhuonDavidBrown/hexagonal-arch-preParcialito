from abc import ABC, abstractmethod
from typing import List

from app.core import models


class DocumentRepositoryPort(ABC):
    @abstractmethod
    def save_document(self, document: models.Document) -> None:
        pass

    @abstractmethod
    def get_documents(self, query: str, n_results: int | None = None) -> List[models.Document]:
        pass


class LlmPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, retrieval_context: str) -> str:
        pass


class DatabasePort(ABC):
    @abstractmethod
    def save_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user(self, username: str) -> models.User:
        pass

    @abstractmethod
    def save_document(self, document: models.Document) -> None:
        pass
