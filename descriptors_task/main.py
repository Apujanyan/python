from validators import *
from logger import Logger


class User:
    def __init__(
            self,
            *,
            first_name: str,
            last_name: str,
            email: str,
            age: int,
            password: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.password = password

    first_name = NameValue()
    last_name = NameValue()
    email = EmailValue()
    age = AgeValue()
    password = PasswordValue()


def main() -> None:
    bob = User(
        first_name="Bob",
        last_name="Smith",
        email="bob.smith@email.com",
        age=35,
        password='Bob_Smith35?@',
    )

    print(bob.age)
    Logger.success("Retrieving Bob's age")
    print(bob.password)
    Logger.info("Retrieving Bob's account password hash")
    print(Logger.logs())
    Logger.add()


if __name__ == '__main__':
    main()
