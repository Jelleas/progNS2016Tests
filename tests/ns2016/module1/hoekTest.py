import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def correct(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), "4.7")
	test.description = lambda : "correct angle calculated"