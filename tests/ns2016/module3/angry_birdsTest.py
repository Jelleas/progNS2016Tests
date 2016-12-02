import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)

@t.test(0)
def hasBeweging(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "beweging")
	test.description = lambda : "definieert de functie `beweging()`"

@t.passed(hasBeweging)
@t.test(1)
def correctOutput(test):
	def testMethod():
		answers = [-88, -87, -86, -84, -81, -69, -68, -67, -66, -65, 15, 16, 17, 74, 75, 81, 87]
		nAnswers = len(answers)
		nCorrect = 0
		for line in lib.outputOf(_fileName).split("\n"):
			for i, answer in enumerate(answers):
				if assertlib.contains(line, str(answer)):
					del answers[i]
					nCorrect += 1
					break
			else:
				nCorrect -= 1

		return nAnswers - nCorrect <= 5 

	test.test = testMethod
	test.description = lambda : "print de juiste hoeken waarbij de vogel de sensor raakt"
