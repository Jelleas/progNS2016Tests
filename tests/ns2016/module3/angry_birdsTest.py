import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

def before():
	lib.neutralizeFunctionFromImport(lib.module(_fileName), "show", "matplotlib.pyplot")

def after():
	import matplotlib.pyplot
	reload(matplotlib.pyplot)

@t.test(0)
def hasBeweging(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "beweging")
	test.description = lambda : "definieert de functie `beweging()`"

@t.passed(hasBeweging)
@t.test(1)
def correctBalBeweging0(test):
	test.test = lambda : assertlib.exact(lib.getFunction("beweging", _fileName)(16, 79, False), False)
	test.description = lambda : "`beweging` werkt met snelheid = 16, hoek = 79, geen animatie"

@t.passed(hasBeweging)
@t.test(2)
def correctBalBeweging1(test):
	test.test = lambda : assertlib.exact(lib.getFunction("beweging", _fileName)(3, 30, False), False)
	test.description = lambda : "`beweging` werkt met snelheid = 3, hoek = 30, geen animatie"

@t.passed(hasBeweging)
@t.test(3)
def correctBalBeweging2(test):
	test.test = lambda : assertlib.exact(lib.getFunction("beweging", _fileName)(11.5, 45, False), True)
	test.description = lambda : "`beweging` werkt met snelheid = 11.5, hoek = 45, geen animatie"

@t.passed(hasBeweging)
@t.test(4)
def correctOutput(test):
	def testMethod():
		answers = [-88, -87, -86, -84, -81, -69, -68, -67, -66, -65, 15, 16, 17, 74, 75, 81, 87]
		for line in lib.outputOf(_fileName).split("\n"):
			if not line.strip():
				continue

			for i, answer in enumerate(answers):
				if assertlib.contains(line, str(answer)):
					del answers[i]
					break
			else:
				return False, "{} is niet correct".format(line)
		return len(answers) == 0

	test.test = testMethod
	test.description = lambda : "print de hoeken waarbij de vogel de sensor raakt"
