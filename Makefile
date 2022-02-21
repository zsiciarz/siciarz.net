.PHONY: test deploy

test:
	coverage run manage.py test --keepdb

deploy:
	ansible-playbook -i hosts playbook.yml
