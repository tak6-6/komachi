# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです。
"""

class Komach:
    def __init__(self, valuelist, oplist):
        self.valuelist = valuelist
        self.oplist = oplist
        self.nFormulas = len(oplist) ** (len(valuelist)-1)
    
    def getNumberOfFormulas(self):
        return self.nFormulas
    
    def __getOpSet(self,formulaId):
        opSet = ''
        opSetLen = len(self.valuelist)-1
        for i in range(opSetLen):
            opIndex = int(formulaId / len(self.oplist) ** (opSetLen - 1 - i) % len(self.oplist))
            opSet = opSet + self.oplist[opIndex]
        return opSet

    def getFormula(self,formulaId):
        opSet = self.__getOpSet(formulaId)
        formula = str(self.valuelist[0])
        for i in range(len(opSet)):
            formula = formula + opSet[i] + str(valuelist[i+1])
        return formula

targetAns = 100
valuelist = list(range(1,10))
oplist = list('+- ')

nAns = 0
 
komachObj = Komach(valuelist,oplist)

for i in range(komachObj.getNumberOfFormulas()):
    formula = komachObj.getFormula(i)
    if eval(formula.replace(" ","")) == targetAns:
        print(f"{formula} = {targetAns}")
        nAns = nAns+1      
 
print(f"count = {nAns}")