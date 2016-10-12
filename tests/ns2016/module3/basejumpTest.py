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
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "basejump")
	test.description = lambda : "definieert de functie `basejump()`"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(1)
def correctTimeTillParachute(test):
	test.test = lambda : assertlib.numberOnLine(12.18, lib.outputOf(_fileName).split("\n")[0], deviation = 0.1)
	test.description = lambda : "print de tijd die verstrijkt tot de parachute open moet (zonder luchtweerstand)"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(2)
def correctExtraTime(test):
	test.test = lambda : assertlib.numberOnLine(5.06, lib.outputOf(_fileName).split("\n")[1], deviation = 0.01)
	test.description = lambda : "print de tijd die er bij komt door de luchtweerstand"
