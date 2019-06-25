
bin/buildout:
	virtualenv-2.7 .
	./bin/pip install -r requirements.txt

bin/instance_iadelib: bin/buildout
	./bin/buildout -Nvt 5

iadelib-up: bin/instance_iadelib
	./bin/instance_iadelib fg

urban-up: bin/instance_iadelib
	./bin/instance_urban fg

middleware-up:
	docker-compose up
