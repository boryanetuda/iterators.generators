nested_list = [
	['a', ['b'], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
				]


class FlatIterator:

	def __init__(self, nlist):

		self.nlist = nlist
		self.last_iter = len(self.nlist)
		self.coursor = -1
		self.ncoursor = 0
		self.new_list = []

	def __iter__(self):

		self.ncoursor = 0
		self.coursor += 1

		return self

	def __next__(self):

		while self.coursor - self.last_iter and self.ncoursor == len(self.nlist[self.coursor]):
			iter(self)
		if self.coursor == self.last_iter:
			raise StopIteration
		self.ncoursor += 1

		return self.nlist[self.coursor][self.ncoursor - 1]


def flat_generator(nlst):
	for i in nlst:
		if isinstance(i, list):
			for j in flat_generator(i):
				yield j
		else:
			yield i


def main():

	for item in FlatIterator(nested_list):
		print(item)

	flat = [item for item in FlatIterator(nested_list)]
	print(flat)

	for item in flat_generator(nested_list):
		print(item)


if __name__ == '__main__':
	main()
