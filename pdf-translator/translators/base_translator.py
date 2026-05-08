from abc import ABC, abstractmethod
class BaseTranslator(ABC):
    @abstractmethod
    def translate(self,text:str)->str: ...
