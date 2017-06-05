class SMBus(object):

	def __init__(self, bus=None):
		print("BUS: " + str(bus))

	def read_i2c_block_data(self, a, b, c):
		print(a)
		return "test"

	def write_i2c_block_data(self, a, b, c):
		print(a)
		return "test"

