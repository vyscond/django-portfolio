env=env
python=$(env)/bin/python
pip=$(env)/bin/pip

test:
	@clear
	@$(python) manage.py test portfolio.tests

run:
	@$(python) manage.py runserver

shell:
	$(python)

install:
	@python setup.py install

requirements:
	$(pip) freeze > requirements.txt

dist:
	python setup.py dist
