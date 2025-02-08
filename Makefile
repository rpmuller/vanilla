all: build install

build: rpmuller.py template.mustache template.sidebar.mustache template.right.sidebar.mustache
	uv run rpmuller.py

install:
	scp rpmuller.right.sidebar.html root@mullermail.xyz:/home/user-data/www/rmuller.net/index.html
	scp profile.jpg root@mullermail.xyz:/home/user-data/www/rmuller.net/profile.jpg
