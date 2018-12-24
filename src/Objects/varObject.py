

class VariableObject(object):
	def __init__(self):
		self.exec_string = ""
		
	def transpile(self, name, operator, value):
		try: self.exec_string += name + " " + operator + " " + value + "\n"
		except: pass
		
		try: self.exec_string += str(val['value'])
		except: pass

		return self.exec_string
		