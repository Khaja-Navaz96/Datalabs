.PHONY: run test pylint db help clean coverage  # Use .PHONY to mark targets that don’t correspond to files.

HOST=127.0.0.1
TEST_PATH=/
$(PYTHON):
	$(VIRTUALENV) $(VIRTUAL_ENV)

run:
	python3 app.py runserver --host $(HOST) --port $(PORT)


test: 
	pytest pytest-test.py 

coverage:
	coverage report

pylint:
	pylint app.py
	

db:
	python3 migrate.py

help:

	
	@echo "\n"
	@echo "make run      -     Runs the application "app.py" on your local machine"
	@echo "make test     -     Runs all the test cases"
	@echo "make pylint   -     Runs Pylint"
	@echo "make db       -     Runs the Migration script, created using alembic "
	@echo "make clean    -     Deletes all the files of the type .o and .dat "
	@echo "\n"

clean:
	rm -f  *.o  *.dat

