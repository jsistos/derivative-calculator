import dyex.functions.function as func
import dyex.functions.elementary as elem
import dyex.functions.operator as op
import dyex.tools.tools as tools

class Parser():
    def __init__(self, expression):
        self.expression = self.format(expression)
        self.blocks = self.find_parenthesis()

        return None

    def format(self, expression):
        return expression.replace(' ', '').lower()

    def find_parenthesis(self):
        lefts = ('(', '[', '{')
        rights = (')', ']', '}')

        blocks = {(0, len(self.expression)-1, self.expression): 0}
        leftLimits = []
        layer = 0

        #Go through the entire string and find parenthesis via parenthesis tree
        for i in range(len(self.expression)):
            if self.expression[i] in lefts:
                #Add the position where the left parenthesis was found
                leftLimits.append(i)

                #Go one layer deeper in the parenthesis tree
                layer += 1

            elif self.expression[i] in rights:
                lLim, rLim = leftLimits[-1], i

                #Add full expression to blocks
                blocks[(lLim, rLim, self.expression[lLim+1:rLim:])] = layer

                #Get rid of the last left parenthesis (now paired with a right parenthesis)
                ## Add try catch for error handling here
                leftLimits.pop(-1)

                #Go one layer above in the parenthesis tree
                layer -= 1
        
        return blocks

    def parenthesis_by_layer(self, layer):
        return {(k[0], k[1]):k[2] for k,v in self.blocks.items() if v == layer}

    def reduce_expression(self):
        arrExpression = tools.string_to_array(self.expression)
        layer1 = self.parenthesis_by_layer(1)

        for parenthesis in layer1.keys():
            arrExpression[parenthesis[0]] = '#'
            del arrExpression[parenthesis[0] + 1:parenthesis[1]:]

        reducedExpression = tools.array_to_string(arrExpression)
        return reducedExpression


    def find_exponents(self):
        return None

    def find_products(self):
        return None

    def find_sums(self):
        if '+' in self.expression:
            return op.Sum(self.expression.split('+'))
        return None

    def parse(self):
        reducedExpression = self.hide_first_layer()
        firstLayerParentheses = self.parenthesis_by_layer(1)

        for subFuncStr in firstLayerParentheses:
            if firstLayerParentheses == 'x':
                return elem.Ex()
            elif isinstance(firstLayerParentheses, (int, float)):
                return elem.Const(firstLayerParentheses)

            return self.parse(subFuncStr)