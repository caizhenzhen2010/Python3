#!/usr/bin/env python3
# copyright(c) 2008 Q	trac Ltd.All rights reversed
"""This module provieds a few string manipulation functions"""
import string

def simplify(text,whitespace=string.whitespace,delete=""):
	"""Return the text with multipulte spaces reduced to single spaces"""
	result = []
	word = ""
	for char in text:
		if char in delete:
			continue
		elif char in whitespace:
			if word:
				result.append(word)
				word=""
		else:
			word+=char
	if word:
		result.append(word)
	return " ".join(result)

def is_balanced(text,brackets="()[]{}<>"):

	counts={}
	left_for_right={}
	for left,right in zip(brackets[::2],brackets[1::2]):
		assert left!=right,"the bracket characters must differ"
		counts[left]=0
		left_for_right[right]=left
	for c in text:
		if c in counts:
			counts[c]+=1
		elif c in left_for_right:
			left=left_for_right[c]
			if counts[left]==0:
				return False
			counts[left]-=1
	return not any(counts.values())
if _name_=="_main_":
	import doctest
	doctest.testmod()
