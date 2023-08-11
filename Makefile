LOCALDIR    = output/
REMOTEDIR   = ../www.co-pylit.org/www/blog/
SSH_PORT   = 5224

.PHONY: build
build:
	pelican content

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: init
init:
	pip install -U pip
	pip install pip-tools

.PHONY: reqs
reqs:
	pip-compile
	pip install -r requirements.txt

.PHONY: sync
sync:
	rsync -avz -e "ssh -p $(SSH_PORT)" $(LOCALDIR) rblack@www.co-pylit.org:$(REMOTEDIR)

