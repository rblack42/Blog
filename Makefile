LOCALDIR    = output/
REMOTEDIR   = www/blog/
SSH_PORT   = 5224

build:
	pelican content/ -s pelicanconf.py

sync:
	rsync -avz -e "ssh -p $(SSH_PORT)" $(LOCALDIR) rblack@www.co-pylit.org:$(REMOTEDIR)

