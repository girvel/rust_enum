build:
	py.exe -3.10 -m build && twine.exe upload dist/*
	rm -r dist