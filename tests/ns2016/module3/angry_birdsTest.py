import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

def before():
	import matplotlib.pyplot as plt
	lib.neutralizeFunction(plt.show)
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot
	reload(matplotlib.pyplot)

@t.test(0)
def hasBeweging(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "beweging")
	test.description = lambda : "definieert de functie `beweging()`"

@t.passed(hasBeweging)
@t.test(1)
def correctOutput(test):
	def testMethod():
		answers = [-88, -87, -86, -84, -81, -69, -68, -67, -66, -65, 15, 16, 17, 74, 75, 81, 87]
		for line in lib.outputOf(_fileName).split("\n"):
			for i, answer in enumerate(answers):
				if assertlib.contains(line, str(answer)):
					del answers[i]
					break

		return len(answers) <= 3

	test.test = testMethod
	test.description = lambda : "print de juiste hoeken waarbij de vogel de sensor raakt"
