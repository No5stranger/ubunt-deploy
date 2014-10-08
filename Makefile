echo-start:
	@echo "*-----You have start makefile----*"

deploy:
	ansible-playbook deploy.yml -f 10
