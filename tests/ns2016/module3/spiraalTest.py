import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re
import os

@t.test(0)
def fileExists(test):
	test.test = lambda : assertlib.fileExists(_fileName)
	test.description = lambda : "bestand {} is aanwezig".format(os.path.basename(_fileName))

@t.passed(fileExists)
@t.test(1)
def containsRequiredFunctions(test):
	def testMethod():
		source = lib.source(_fileName)
		funcIn = lambda src, fName : assertlib.match(src, re.compile(".*{}\(.*".format(fName), re.DOTALL))
		for fName in ["draw", "pause", "clf"]:
			if not funcIn(source, fName):
				return False
		return True

	test.test = testMethod
	test.description = lambda : "vertoont een of andere vorm van animatie"
