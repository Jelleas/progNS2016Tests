import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

@t.test(0)
def fileExists(test):
	test.test = lambda : assertlib.fileExists(_fileName)
	test.description = lambda : "file {} exists".format(_fileName)

@t.passed(fileExists)
@t.test(1)
def containsRequiredFunctions(test):
	def testMethod():
		source = lib.source(_fileName)
		funcIn = lambda src, fName : assertlib.match(src, re.compile(".*{}\(.*".format(fName), re.DOTALL))
		for fName in ["draw", "pause", "clf"]:
			if not funcIn(source, fName):
				return False, "could not find a call to {}() in source code".format(fName)
		return True

	test.test = testMethod
	test.description = lambda : "code seems to perform an animation of some sort"