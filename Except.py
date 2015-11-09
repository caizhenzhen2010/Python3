d="ssssss"
try:
	x=d[5]
except LookupError:
	print("LookupError error occurred")
except IndexError:
	print("IndexError userd")
else:
	print("else")
finally:
	print("finally")