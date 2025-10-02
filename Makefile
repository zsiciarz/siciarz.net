.PHONY: test deploy

test:
	uv run coverage run manage.py test --keepdb

deploy:
	ansible-playbook -i hosts playbook.yml
