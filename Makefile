all: init

init:
	pip install -r requirements.txt

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

clean:
	rm -rf build dist pyfps.egg-info

.PHONY: init build upload clean
