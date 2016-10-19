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
def correctMaxTemp(test):
	test.test = lambda : assertlib.match(lib.getLine(lib.outputOf(_fileName), 0), ".*36[,.]8.*")
	test.description = lambda : "print de maximale temperatuur"

@t.test(01)
def correctDayOfMaxTemp(test):
	def testMethod():
		line = lib.getLine(lib.outputOf(_fileName), 0)
		return assertlib.contains(line, "27") and assertlib.contains(line.lower(), "jun") and assertlib.contains(line, "1947")
	test.test = testMethod
	test.description = lambda : "print de dag van de maximale temperatuur"

@t.test(10)
def correctMinTemp(test):
	test.test = lambda : assertlib.match(lib.getLine(lib.outputOf(_fileName), 1), ".*24[,.]8.*")
	test.description = lambda : "print de minimale temperatuur"

@t.test(11)
def correctDayOfMinTemp(test):
	def testMethod():
		line = lib.getLine(lib.outputOf(_fileName), 1)
		return assertlib.contains(line, "27") and assertlib.contains(line.lower(), "jan") and assertlib.contains(line, "1942")
	test.test = testMethod
	test.description = lambda : "print de dag van de minimale temperatuur"

@t.test(20)
def correctLongestPeriod(test):
	test.test = lambda : assertlib.contains(lib.getLine(lib.outputOf(_fileName), 2), "21")
	test.description = lambda : "print de langste periode dat het aaneengesloten heeft gevroren"

@t.test(21)
def correctFinalDayOfLongestPeriod(test):
	def testMethod():
		line = lib.getLine(lib.outputOf(_fileName), 2)
		return assertlib.contains(line, "24") and assertlib.contains(line.lower(), "feb") and assertlib.contains(line, "1947")
	test.test = testMethod
	test.description = lambda : "print de laatste dag van de langste periode dat het aaneengesloten heeft gevroren"

@t.test(30)
def correctHeatwave(test):
	test.test = lambda : assertlib.contains(lib.getLine(lib.outputOf(_fileName), 3), "1911")
	test.description = lambda : "print het eerste jaartal waarin een hittegolf voorkwam"