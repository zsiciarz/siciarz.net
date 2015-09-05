.PHONY: test

test:
	coverage run manage.py test --keepdb
