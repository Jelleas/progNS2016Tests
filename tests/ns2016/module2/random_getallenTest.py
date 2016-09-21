import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import sys

@t.test(0)
def correctMijn_random(test):
	def testMethod():
		mijn_random = lib.getFunction("mijn_random", _fileName)
		if not assertlib.containsOnly([mijn_random(1,1) for i in range(100)], [1]):
			return False, "Huh? a random number between 1 and 1 gives something unexpected"
		if not assertlib.containsOnly([mijn_random(0,1) for i in range(100)], [0,1]):
			return False, "Huh? a random number between 0 and 1 can become something other than 0 or 1?!"
		return True, ""
	test.test = testMethod
	
	test.description = lambda : "mijn_random functions correctly"
	test.fail = lambda info : str(info)


@t.passed(correctMijn_random)
@t.test(1)
def correctVierkant(test):
	test.test = lambda : assertlib.between(lib.getFunction("Vierkant", _fileName)(), 0.45, 0.55)
	test.description = lambda : "correct distance calculated by Vierkant"