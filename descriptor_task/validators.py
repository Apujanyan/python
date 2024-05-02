"""Validators module for validation User class attributes"""
import re


class AgeValue:
    """AgeValue descriptor for age validation"""
    def __set_name__(self, owner, property_name) -> None:
        self.property_name = property_name

    def __get__(self, instance, owner) -> int:
        if instance is None:
            return self
        return getattr(instance, f'__{self.property_name}', None)

    def __set__(self, instance, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(
                f"The {self.property_name} must be an integer type!"
                )
        if value <= 0:
            raise ValueError(
                f"The {self.property_name} cannot be negative!"
                )
        setattr(instance, f'__{self.property_name}', value)


class NameValue:
    """NameValue descriptor for first and last name validation"""
    def __set_name__(self, owner, property_name) -> None:
        self.property_name = property_name

    def __get__(self, instance, owner) -> str:
        if instance is None:
            return self
        return getattr(instance, f'__{self.property_name}', None)
    
    def __set__(self, instance, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"The {self.property_name} must be a string type!")
        if not value.isalpha():
            raise ValueError(
                f"The {self.property_name} cannot be empty or contain spaces!"
                )
        setattr(instance, f'__{self.property_name}', value)


class EmailValue:
    """EmailValue descriptor for email validation"""
    def __set_name__(self, owner, property_name) -> None:
        self.property_name = property_name

    def __get__(self, instance, owner) -> str:
        if instance is None:
            return self
        return getattr(instance, f'__{self.property_name}', None)
    
    def __set__(self, instance, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"The {self.property_name} must be a string type!"
            )
        email_re = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(email_re, value):
            raise ValueError("Invalid email address!")
        setattr(instance, f'__{self.property_name}', value)


class PasswordValue:
    """PasswordValue descriptor for password validation"""
    def __set_name__(self, owner, property_name) -> None:
        self.property_name = property_name

    def __get__(self, instance, owner) -> str:
        if instance is None:
            return self
        return getattr(instance, f'__{self.property_name}', None)

    def __set__(self, instance, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"The {self.property_name} must be a string type!"
            )
        if (
            len(value) <= 8 or
            not re.search("[a-z]", value) or
            not re.search("[A-Z]", value) or
            not re.search("[0-9]", value) or
            not re.search("[_@$]", value)
        ):
            raise ValueError("Weak password!")
        setattr(instance, f'__{self.property_name}', hash(value))
