
class ParentList(object):

	def __init__(self, items):
		self._items = list(items)

	def add(self, item):
		self._items.append(item)

	def __getitem__(self, index):
		return self._items[index]

	def sort(self):
		self._items.sort()

	def __repr__(self):
		return "{}({!r})".format(self.__class__.__name__, self._items)

	def __len__(self):
		return len(self._items)

class ChildList(ParentList):

	def __init__(self, items=()):
		super().__init__(items)
		self.sort()
		self.__repr__()

	def add(self, item):
		super().add(item)
		self.sort()

inst1 = ChildList((1,3,7,2,8,5,9,2,5,8,4))
print(inst1)


