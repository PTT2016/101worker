	
from antlr4 import *

class countNonTerminals(ANTLRv4ParserVisitor)
	def int defaultResult()
		return 1
		
	def int aggregateResult(int aggregate, int nextResult)
		return (aggregate + nextResult)
				
	def int countNonTerminals(visitGrammarSpec, ctx):
		if self.getChildCount > 0:
			return (self.visitChildren(ctx))
		return 0