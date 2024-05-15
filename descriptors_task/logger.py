import os
import datetime


"""Logger module for logging. """


class Logger:
    """Logger class for logging. """

    __logs: dict = {}
    __date = datetime.date.today()
    # __time = datetime.datetime.now()
    __current_time = datetime.datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def logs() -> dict:
        """logs method for retrieving all logs. """

        return Logger.__logs

    @staticmethod
    def success(text: str) -> None:
        """success method for successful operation logging. """

        try:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"].append(
                f"SUCCESS | {text}"
            )
        except KeyError:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"] = [
                f"SUCCESS | {text}"
            ]

        print(f"{Logger.__date} {Logger.__current_time} | SUCCESS | {text}")

    @staticmethod
    def info(text: str) -> None:
        """info method for giving information. """

        try:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"].append(
                f"INFO | {text}"
                f""
            )
        except KeyError:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"] = [
                f"INFO | {text}"
            ]

        print(f"{Logger.__date} {Logger.__current_time} | INFO | {text}")

    @staticmethod
    def error(text: str) -> None:
        """error method for failed operation logging. """

        try:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"].append(
                f"ERROR | {text}"
            )
        except KeyError:
            Logger.__logs[f"{Logger.__date} {Logger.__current_time}"] = [f"ERROR | {text}"]

        print(f"{Logger.__date} {Logger.__current_time} | ERROR | {text}")

    @staticmethod
    def _create_log_directory() -> None:
        """Creates new directory for logs if not exists. """

        path = os.getcwd() + "/logs"
        if not os.path.isdir(path):
            os.makedirs(path)

    @staticmethod
    def add(filename=f"{__date}_{__current_time}") -> None:
        """add method for creating log file with .log extension. """

        Logger._create_log_directory()
        f = open(f"./logs/{filename}.log", 'a')
        for key in Logger.__logs.keys():
            for log in Logger.__logs[key]:
                f.write(f"{key} | {log}\n")
        f.close()
