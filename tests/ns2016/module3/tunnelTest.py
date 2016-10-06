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
		for fName in ["tunnel"]:
			if not funcIn(source, fName):
				return False
		return True

	test.test = testMethod
	test.description = lambda : "definieert de functie `tunnel()`"

@t.passed(containsRequiredFunctions)
@t.test(1)
def correctMaxSpeed(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[0], ".*28[0-9][0-9][0-9].*")
	test.description = lambda : "print de maximale snelheid van de appel"

@t.passed(containsRequiredFunctions)
@t.test(2)
def correctTimeTillReturn(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[1], ".*50[0-9][0-9].*")
	test.description = lambda : "print het tijdstip van terugkeer na loslaten"
