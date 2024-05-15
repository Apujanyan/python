from abc import ABC, abstractmethod


"""
Dependency Inversion Principle

High-level classes shouldn’t depend on low-level classes.
Both should depend on abstractions. Abstractions
shouldn’t depend on details. Details should depend on
abstractions.
"""


# Bad practice
# A high-level class depends on a low-level class.

# High-level class
class BudgetReport:
    def __init__(self, database: MySQL) -> None:
        self.database = database

    def open(self) -> None:
        ...

    def save(self) -> None:
        ...


# Low-level class
class MySQL:
    def insert(self) -> None:
        ...

    def update(self) -> None:
        ...

    def delete(self) -> None:
        ...


# Good practice
# Low-level classes depend on a high-level abstraction

# High-level classes
class BudgetReport:
    def __init__(self, database: Database) -> None:
        self.database = database

    def open(self) -> None:
        ...

    def save(self) -> None:
        ...


class Database(ABC):
    @abstractmethod
    def insert(self) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def delete(self) -> None:
        ...


# Low-level classes
class Oracle(Database):
    ...


class PostgreSQL(Database):
    ...