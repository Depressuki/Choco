import lexer
import parserscript

def main():
	content = ""
	with open('test.choc', 'r') as file:
		content = file.read()
		
	#Lexer
	
	lex = lexer.Lexer(content)
	
	tokens = lex.tokenize()
	
	p = parserscript.Parser(tokens)
	p.parse()
main()