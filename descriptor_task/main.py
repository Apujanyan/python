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
    Bob = User(
        first_name="Bob",
        last_name="Smith",
        email="bob.smith@email.com",
        age=35,
        password='Bob_Smith35?@',
    )

    print(Bob.age)

    Logger.success("fsd")
    Logger.success("666")
    Logger.error('error')
    Logger.add()
    print(Logger.logs())


if __name__ == '__main__':
    main()
