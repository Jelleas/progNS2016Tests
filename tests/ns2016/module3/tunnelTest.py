import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

def before():
	lib.neutralizeFunctionFromImport(lib.module(_fileName), "show", "matplotlib.pyplot")

@t.test(0)
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "tunnel")
	test.description = lambda : "definieert de functie `tunnel()`"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(1)
def correctMaxSpeed(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[0], ".*28[0-9][0-9][0-9].*")
	test.description = lambda : "print de maximale snelheid van de appel"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(2)
def correctTimeTillReturn(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[1], ".*50[0-9][0-9].*")
	test.description = lambda : "print het tijdstip van terugkeer na loslaten"
