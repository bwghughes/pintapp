ci:
	sniffer . -x --with-growl -x --with-coverage -x --cover-package=roomyapp.models,roomyapp.app -x --cover-html

deploy:
	dotcloud push roomyapp

test:
	nosetests --with-coverage -x --cover-package=roomyapp.models,roomyapp.app -x --cover-html

doc:
	echo "Docs"
