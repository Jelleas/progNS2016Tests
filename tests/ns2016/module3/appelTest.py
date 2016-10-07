import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

def before():
	lib.neutralizeFunctionFromImport(lib.module(_fileName), "show", "matplotlib.pyplot")

@t.test(0)
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "appel")
	test.description = lambda : "definieert de functie `appel()`"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(1)
def correctTime(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[0], ".*4\.5[1-3].*")
	test.description = lambda : "print het tijdstip waarop de appel de grond raakt"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(2)
def correctSpeed(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[1], ".*159\.[4-6].*")
	test.description = lambda : "print de snelheid waarmee de appel de grond raakt"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(3)
def correctSecondsToHit100(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName).split("\n")[2], ".*2\.8[2-4].*")
	test.description = lambda : "print het tijdstip waarop een snelheid van 100km/u wordt bereikt"
