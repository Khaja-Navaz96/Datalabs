.PHONY: run test pylint db help clean  # Use .PHONY to mark targets that don’t correspond to files.

HOST=127.0.0.1
TEST_PATH=./

run:
	python app.py runserver --host $(HOST) --port $(PORT)

test:
    py.test --verbose --color=yes $(TEST_PATH)

#pylint:


#db:


help:
	@echo "\n"
	@echo "Hello, Welcome to Help ! Below are the list of commands you may use."
	@echo "\n"
	@echo "make run      -     Runs the application "app.py" on your local machine"
	@echo "make test     -     Runs all the test cases"
	@echo "make pylint   -     Runs Pylint"
	@echo "make db       -     Runs the Migration script, created using alembic "
	@echo "make clean    -     Deletes all the files of the type .o and .dat "
	@echo "\n"

clean:
	rm -f  *.o  *.dat

