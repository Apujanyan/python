"""
Interface Segregation Principle

Clients shouldn’t be forced to depend on methods they
do not use.
"""

from abc import ABC, abstractmethod


# Bad practice
class CloudProvider(ABC):
    @abstractmethod
    def store_file(self, name: str) -> None:
        ...

    @abstractmethod
    def get_file(self, name: str) -> None:
        ...

    @abstractmethod
    def create_server(self, region: str) -> None:
        ...

    @abstractmethod
    def list_servers(self, region: str) -> list:
        ...

    @abstractmethod
    def get_cdn_address(self) -> str:
        ...


# Class Amazon can implement all methods in CloudProvider.
class Amazon(CloudProvider):
    ...


# Class Dropbox cannot implement all of them.
class Dropbox(CloudProvider):
    ...


# Good practice
class CloudHostingProvider(ABC):
    @abstractmethod
    def create_server(self, region: str) -> None:
        ...

    @abstractmethod
    def list_servers(self, region: str) -> list:
        ...


class CDNProvider(ABC):
    @abstractmethod
    def get_cdn_address(self) -> None:
        ...


class CloudStorageProvider(ABC):
    @abstractmethod
    def store_file(self, name: str) -> None:
        ...

    @abstractmethod
    def get_file(self, name: str) -> None:
        ...


class Amazon(CloudHostingProvider,
             CDNProvider,
             CloudStorageProvider):
    ...


class Dropbox(CloudStorageProvider):
    ...
