import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re
import os

@t.test(0)
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "spiraal")
	test.description = lambda : "definieert de functie `spiraal()`"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(1)
def containsRequiredFunctionCalls(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "draw", "pause")
	test.description = lambda : "vertoont een of andere vorm van animatie"
