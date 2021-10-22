class Parser():
    def __init__(self, expression):
        self.expression = expression
        self.blocks = self.find_parenthesis()

        return None

    def find_parenthesis(self):
        lefts = ['(', '[', '{']
        rights = [')', ']', '}']

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

    def find_parenthesis_by_layer(self, layer):
        return {k for k,v in self.blocks.items() if v == layer}

#Make dedicated testing folder
exp = Parser('e^((x+1)^2)*(4x^2+5x+2)')
print(exp.blocks)
print("In layer 1: " + str(exp.find_parenthesis_by_layer(1)))