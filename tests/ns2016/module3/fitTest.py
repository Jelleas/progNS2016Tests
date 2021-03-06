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
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "fit")
	test.description = lambda : "definieert de functie `fit()`"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(1)
def correctC(test):
	test.test = lambda : assertlib.numberOnLine(60.3, lib.getLine(lib.outputOf(_fileName), 0), deviation = 1)
	test.description = lambda : "print de beste waarde van c"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(2)
def correctUncertainy(test):
	test.test = lambda : assertlib.numberOnLine(1.5, lib.getLine(lib.outputOf(_fileName), 1), deviation = 0.1)
	test.description = lambda : "print de onzekerheid bij c"
