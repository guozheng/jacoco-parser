init:
	pip install -r requirements.txt

test:
	python -m unittest -v test_parser.TestParser

.PHONY: init test
