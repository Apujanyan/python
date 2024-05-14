"""
Single Responsibility Principle

A class should have just one reason to change.
"""


# Bad practice
class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def print_time_sheet_report(self) -> None:
        print(f'Time sheet report of {self}. ')


# Good practice
class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class TimeSheetReport:
    @staticmethod
    def print_time_sheet_report(employee: Employee) -> None:
        print(f'Time sheet report of {employee}. ')

