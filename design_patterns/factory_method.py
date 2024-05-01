"""Factory Method design pattern example"""

from abc import ABC, abstractmethod


class Package(ABC):
    @abstractmethod
    def run(self) -> None:
        ...


class DebianPackage(Package):
    def __init__(self, name: str) -> None:
        self.name = name
        self.extension = '.deb'
        self.full_name = name + self.extension

    def run(self) -> None:
        print(f'Running {self.full_name}...')


class RedHatPackage(Package):
    def __init__(self, name: str) -> None:
        self.name = name
        self.extension = '.rpm'
        self.full_name = name + self.extension

    def run(self) -> None:
        print(f'Running {self.full_name}...')


class PackageManager(ABC):
    @staticmethod
    @abstractmethod
    def download_package(package_name: str) -> Package:
        ...


class APT(PackageManager):
    @staticmethod
    def download_package(package_name: str) -> DebianPackage:
        if not package_name[-4::] == '.deb':
            raise ValueError('The package extension must be .deb!')
        print(f'The package {package_name} was successfully downloaded.')
        return DebianPackage(package_name)


class DNF(PackageManager):
    @staticmethod
    def download_package(package_name: str) -> RedHatPackage:
        if not package_name[-4::] == '.rpm':
            raise ValueError('The package extension must be .rpm!')
        print(f'The package {package_name} was successfully downloaded.')
        return RedHatPackage(package_name)


def main() -> None:
    deb_package = APT.download_package('deb_package.deb')
    rpm_package = DNF.download_package('rpm_package.rpm')
    deb_package.run()
    rpm_package.run()


if __name__ == '__main__':
    main()

