import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def correctDistance(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[0], "35")
	test.description = lambda : "correct distance"

@t.test(1)
def correctBarriers(test):
	def testMethod():
		result = lib.outputOf(_fileName).split("\n")[1]
		testResult = assertlib.match(result, ".*9551.*9587.*") or assertlib.match(result, ".*9587.*9551.*")
		return testResult, result
	test.test = testMethod

	test.description = lambda : "correct bounding primes"
	test.fail = lambda info : "output \"%s\" does not contain the correct boundaries" %info