from Objects.varObject import VariableObject

class Parser(object):
	
	def __init__(self, tokens):
		
		self.tokens = tokens
		self.token_index = 0
		self.transpiled_code = ""
	def parse(self):
		
		while self.token_index < len(self.tokens):
		
			token_type = self.tokens[self.token_index][0]
			token_value = self.tokens[self.token_index][1]
			
			
			if token_type == "VAR_DECLARATION" and token_value == "v":
				self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
			elif token_type == "FUNCTION":
				self.parse_function(self.tokens[self.token_index:len(self.tokens)])
			self.token_index += 1
		print(self.transpiled_code)
		
	
	def parse_variable_declaration(self, token_stream):
	
		tokens_checked = 0
		
		name = ""
		operator = ""
		value = ""
		
		for token in range(0, len(token_stream)):
		
			token_type = token_stream[tokens_checked][0]
			token_value = token_stream[tokens_checked][1]
			print(token_value)
			if token_type == "STATEMENT_END":
				break
			elif token == 1 and token_type == "IDENTIFIER":
				name = token_value
				
			elif token == 1 and token_type != "IDENTIFIER":
				print("Nyaaa! Invalid identifier name somewhere! The token " + str(token) + " doesn't match up with the token type " + token_type + "! Please fix it so I can run smoothly!")
				quit()
				
			elif token == 2 and token_type == "OPERATOR":
				operator = token_value
			elif token == 2 and token_type != "OPERATOR":
				print("Nyaaa! Invalid operator somewhere! The token " + str(token) + " doesn't match up with the token type " + token_type + "! Please fix it so I can run smoothly!")
				quit()
				
			elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
				value = token_value
				print("Valid " + token_type + " received!")
			elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
				print("Nyaaa! " + token_type + " isn't a valid string, integer, or identifier!")
				quit()
				
			tokens_checked += 1
		varObj = VariableObject()
		self.transpiled_code += varObj.transpile(name, operator, value)
			
		self.token_index += tokens_checked

	def parse_function(self, token_stream):
		
		tokens_checked = 0
		
		for token in range(0, len(token_stream)):
			print()
			token_type = token_stream[tokens_checked][0]
			token_value = token_stream[tokens_checked][1]
			if token_type == "STATEMENT_END":
				break
			elif token == 0 and token_type == "FUNCTION":
				print(token_value)
				
			
		tokens_checked += 1
	