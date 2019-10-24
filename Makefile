all: build

.PHONY: build

build:
	python setup.py sdist bdist_wheel
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

clean:
	rm -rf build dist pyfps.egg-info
