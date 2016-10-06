import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

def before():
	lib.neutralizeFunctionFromImport(lib.module(_fileName), "show", "matplotlib.pyplot")

@t.test(0)
def containsRequiredFunctions(test):
	def testMethod():
		source = lib.source(_fileName)
		funcIn = lambda src, fName : assertlib.match(src, re.compile(".*{}\(.*".format(fName), re.DOTALL))
		for fName in ["fit"]:
			if not funcIn(source, fName):
				return False
		return True

	test.test = testMethod
	test.description = lambda : "definieert de functie `fit()`"

@t.passed(containsRequiredFunctions)
@t.test(1)
def correctC(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName).split("\n")[0], "60.")
	test.description = lambda : "print de beste waarde van c"

@t.passed(containsRequiredFunctions)
@t.test(2)
def correctUncertainy(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName).split("\n")[1], "1.5")
	test.description = lambda : "print de onzekerheid bij c"
