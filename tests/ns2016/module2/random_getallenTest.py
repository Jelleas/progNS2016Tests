import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import sys

def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)

@t.test(00)
def hasRandomTussen(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "randomTussen")
	test.description = lambda : "definieert de functie randomTussen()"

@t.passed(hasRandomTussen)
@t.test(01)
def correctRandomTussen(test):
	def testMethod():
		randomTussen = lib.getFunction("randomTussen", _fileName)
		if not assertlib.containsOnly([int(randomTussen(1,1)) for i in range(100)], [1]):
			return False, "Huh? Een willekeurig getal tussen 1 en 1 wordt iets anders dan 1?!"
		if not assertlib.containsOnly([int(randomTussen(-5,5)) for i in range(100)], range(-5, 6)):
			return False, "Huh? Een willekeurig getal tussen -5 en 5 kan groter of kleiner worden dan -5 of 5?!"
		return True
	test.test = testMethod
	test.description = lambda : "randomTussen() werkt correct"

@t.test(10)
def hasVierkant(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "vierkant")
	test.description = lambda : "definieert de functie vierkant()"

@t.passed(hasVierkant)
@t.test(11)
def correctVierkant(test):
	test.test = lambda : assertlib.between(lib.getFunction("vierkant", _fileName)(), 0.51, 0.54)
	test.description = lambda : "vierkant geeft de goede afstand terug"