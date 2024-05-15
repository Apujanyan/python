from abc import ABC, abstractmethod
from typing import Iterable, Union


"""
Strategy

Strategy is a behavioral design pattern that lets you define a
family of algorithms, put each of them into a separate class,
and make their objects interchangeable.
"""


class Sort(ABC):
    @abstractmethod
    def sort(
            self,
            data: Iterable[Union[int, float]]
    ) -> Iterable[Union[int, float]]:
        ...


class QuickSort(Sort):
    def sort(
            self,
            data: Iterable[Union[int, float]]
    ) -> Iterable[Union[int, float]]:
        print('Sorting with Quick sort algorithm.')
        return sorted(data)


class BubbleSort(Sort):
    def sort(
           self,
           data: Iterable[Union[int, float]]
    ) -> Iterable[Union[int, float]]:
        print('Sorting with Bubble sort algorithm.')
        return sorted(data)


class Sorter:
    def __init__(self, sort: Sort) -> None:
        self.sort = sort

    def set_sort(self, sort: Sort) -> None:
        self.sort = sort

    def sort_data(
            self,
            data: Iterable[Union[int, float]]
    ) -> Iterable[Union[int, float]]:
        return self.sort.sort(data)


def main() -> None:
    data = [1, 5, -56, 0, 34]

    bubble_sorter = Sorter(BubbleSort())
    sorted_data = bubble_sorter.sort_data(data)
    print(f'Sorted data: {sorted_data}')

    quick_sorter = Sorter(QuickSort())
    sorted_data = quick_sorter.sort_data(data)
    print(f'Sorted data: {sorted_data}')


if __name__ == '__main__':
    main()
