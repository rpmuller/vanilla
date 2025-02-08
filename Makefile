all: build install

build: rpmuller.py template.html template.sidebar.html template.right.sidebar.html
	uv run rpmuller.py

install:
	scp rpmuller.right.sidebar.html root@mullermail.xyz:/home/user-data/www/rmuller.net/index.html
	scp profile.jpg root@mullermail.xyz:/home/user-data/www/rmuller.net/profile.jpg
