import sys
from pyknow import *

class Animals(KnowledgeEngine):
    @Rule(OR(
           AND(Fact('sharp teeth'),Fact('claws'),Fact('forward looking eyes')),
           Fact('eats meat')))
    def cornivor(self):
        self.declare(Fact('carnivor'))
        
    @Rule(OR(Fact('hair'),Fact('gives milk')))
    def mammal(self):
        self.declare(Fact('mammal'))

    @Rule(Fact('mammal'),
          OR(Fact('has hooves'),Fact('chews cud')))
    def hooves(self):
        self.declare('ungulate')
        
    @Rule(OR(Fact('feathers'),AND(Fact('flies'),Fact('lays eggs'))))
    def bird(self):
        self.declare('bird')
        
    @Rule(Fact('mammal'),Fact('carnivor'),
          Fact(color='red-brown'),
          Fact(pattern='dark spots'))
    def monkey(self):
        self.declare(Fact(animal='monkey'))

    @Rule(Fact('mammal'),Fact('carnivor'),
          Fact(color='red-brown'),
          Fact(pattern='dark stripes'))
    def tiger(self):
        self.declare(Fact(animal='tiger'))

    @Rule(Fact('ungulate'),
          Fact('long neck'),
          Fact('long legs'),
          Fact(pattern='dark spots'))
    def giraffe(self):
        self.declare(Fact(animal='giraffe'))

    @Rule(Fact('ungulate'),
          Fact(pattern='dark stripes'))
    def zebra(self):
        self.declare(Fact(animal='zebra'))

    @Rule(Fact('bird'),
          Fact('long neck'),
          Fact('cannot fly'),
          Fact(color='black and white'))
    def straus(self):
        self.declare(Fact(animal='ostrich'))

    @Rule(Fact('bird'),
          Fact('swims'),
          Fact('cannot fly'),
          Fact(color='black and white'))
    def pinguin(self):
        self.declare(Fact(animal='pinguin'))

    @Rule(Fact('bird'),
          Fact('flies well'))
    def albatros(self):
        self.declare(Fact(animal='albatross'))
        
    @Rule(Fact(animal=MATCH.a))
    def print_result(self,a):
          print('Animal is {}'.format(a))
                    
    def factz(self,l):
        for x in l:
            self.declare(x)

class Ask():
    def __init__(self,choices=['y','n']):
        self.choices = choices
    def ask(self):
        if max([len(x) for x in self.choices])>1:
            for i,x in enumerate(self.choices):
                print("{0}. {1}".format(i,x),flush=True)
            x = int(input())
            return self.choices[x]
        else:
            print("/".join(self.choices),flush=True)
            return input()

class Content():
    def __init__(self,x):
        self.x=x
        
class If(Content):
    pass

class AND(Content):
    pass

class OR(Content):
    pass

class KnowledgeBase():
    def __init__(self,rules):
        self.rules = rules
        self.memory = {}
        
    def get(self,name):
        if ':' in name:
            k,v = name.split(':')
            vv = self.get(k)
            return 'y' if v==vv else 'n'
        if name in self.memory.keys():
            return self.memory[name]
        for fld in self.rules.keys():
            if fld==name or fld.startswith(name+":"):
                # print(" + proving {}".format(fld))
                value = 'y' if fld==name else fld.split(':')[1]
                res = self.eval(self.rules[fld],field=name)
                if res!='y' and res!='n' and value=='y':
                    self.memory[name] = res
                    return res
                if res=='y':
                    self.memory[name] = value
                    return value
        # field is not found, using default
        res = self.eval(self.rules['default'],field=name)
        self.memory[name]=res
        return res
                
    def eval(self,expr,field=None):
        # print(" + eval {}".format(expr))
        if isinstance(expr,Ask):
            print(field)
            return expr.ask()
        elif isinstance(expr,If):
            return self.eval(expr.x)
        elif isinstance(expr,AND) or isinstance(expr,list):
            expr = expr.x if isinstance(expr,AND) else expr
            for x in expr:
                if self.eval(x)=='n':
                    return 'n'
            return 'y'
        elif isinstance(expr,OR):
            for x in expr.x:
                if self.eval(x)=='y':
                    return 'y'
            return 'n'
        elif isinstance(expr,str):
            return self.get(expr)
        else:
            print("Unknown expr: {}".format(expr))