
"""MyFeature: basic example feature module.

Provides a simple Feature class with a greeting and utility methods.
"""

from typing import Iterable


class MyFeature:
	"""Simple feature demonstrating a few methods."""

	def __init__(self, name: str = "User") -> None:
		self.name = name

	def greet(self) -> str:
		"""Return a greeting for the configured name."""
		return f"Hello, {self.name}!"

	@staticmethod
	def sum_numbers(nums: Iterable[float]) -> float:
		"""Return the sum of an iterable of numbers."""
		return sum(nums)


def main() -> None:
	"""Basic CLI demonstration when run as a script."""
	feature = MyFeature("Developer")
	print(feature.greet())
	print("Sum of 1..5:", MyFeature.sum_numbers(range(1, 6)))


if __name__ == "__main__":
	main()
