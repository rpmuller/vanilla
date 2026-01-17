all: build install

build: rpmuller.py template.timeline.html template.html
	uv run rpmuller.py

install:
	scp rpmuller.html root@mullermail.xyz:/home/user-data/www/rmuller.net/index.html

