import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re
import os

@t.test(0)
def containsRequiredFunction(test):
	def testMethod():
		source = lib.source(_fileName)
		funcIn = lambda src, fName : assertlib.match(src, re.compile(".*{}\(.*".format(fName), re.DOTALL))
		for fName in ["student"]:
			if not funcIn(source, fName):
				return False
		return True

	test.test = testMethod
	test.description = lambda : "definieert de functie `student()`"

@t.passed(containsRequiredFunction)
@t.test(2)
def containsRequiredFunctions(test):
	def testMethod():
		source = lib.source(_fileName)
		funcIn = lambda src, fName : assertlib.match(src, re.compile(".*{}\(.*".format(fName), re.DOTALL))
		for fName in ["student", "draw", "pause", "clf"]:
			if not funcIn(source, fName):
				return False
		return True

	test.test = testMethod
	test.description = lambda : "vertoont een of andere vorm van animatie"
