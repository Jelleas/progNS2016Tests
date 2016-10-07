import checkpy.test as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re
import os

@t.test(0)
def containsRequiredFunction(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "student")
	test.description = lambda : "definieert de functie `student()`"

@t.passed(containsRequiredFunction)
@t.test(1)
def containsRequiredFunctionCalls(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "student", "draw", "pause", "clf")
	test.description = lambda : "vertoont een of andere vorm van animatie"
