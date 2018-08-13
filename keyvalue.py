class Group:
	def __init__(self, name):
		self.name = name
		self.pairs = {}
	def add_pairs(self, key, value):
		pair = {key:value}
		self.pairs.update(pair)