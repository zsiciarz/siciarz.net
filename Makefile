.PHONY: test watch

WEBPACK = ./node_modules/.bin/webpack
WEBPACK_ARGS = --colors --progress

test:
	coverage run manage.py test --keepdb

production_assets: node_modules
	$(WEBPACK) $(WEBPACK_ARGS)

watch: node_modules
	$(WEBPACK) $(WEBPACK_ARGS) --watch

node_modules: package.json
	@npm install
