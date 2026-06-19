"""new_Branch.py

Simple demo feature: a small CLI to greet and do basic math.
"""

def greet(name: str) -> str:
	"""Return a greeting for the given name."""
	return f"Hello, {name}!"


def add(a: float, b: float) -> float:
	"""Return the sum of two numbers."""
	return a + b


def multiply(a: float, b: float) -> float:
	"""Return the product of two numbers."""
	return a * b


class SimpleFeature:
	"""Encapsulates the basic feature operations."""

	def __init__(self, name: str = "User"):
		self.name = name

	def greet(self) -> str:
		return greet(self.name)

	def add(self, a: float, b: float) -> float:
		return add(a, b)

	def multiply(self, a: float, b: float) -> float:
		return multiply(a, b)


if __name__ == "__main__":
	# minimal CLI demonstration
	import sys

	args = sys.argv[1:]
	if not args:
		print(greet("World"))
	elif args[0] == "greet":
		name = args[1] if len(args) > 1 else "World"
		print(greet(name))
	elif args[0] == "add" and len(args) >= 3:
		print(add(float(args[1]), float(args[2])))
	elif args[0] == "mul" and len(args) >= 3:
		print(multiply(float(args[1]), float(args[2])))
	else:
		print("Usage: greet [name] | add a b | mul a b")
