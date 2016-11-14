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
def hasNulpunten(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "nulpunten")
	test.description = lambda : "definieert de functie nulpunten()"

@t.passed(hasNulpunten)
@t.test(1)
def correct(test):
	test.test = lambda : sorted(int(p * 10) for p in lib.getFunction("nulpunten", _fileName)(1,2,-10)) == [-43, 23]
	test.description = lambda : "nulpunten werkt correct voor invoer a=1, b=2, c=-10"

@t.passed(hasNulpunten)
@t.test(2)
def returnTypeIsList(test):
	test.test = lambda : assertlib.sameType(lib.getFunction("nulpunten", _fileName)(1,2,-10), [])
	test.description = lambda : "nulpunten geeft een lijst terug"