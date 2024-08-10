from abc import ABC, abstractmethod
from typing import List

from app.core import models


class DocumentRepositoryPort(ABC):
    @abstractmethod
    def save_document(self, document: models.Document) -> None:
        pass

    @abstractmethod
    def get_documents(self, query: str) -> List[models.Document]:
        pass


class OpenAIPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass