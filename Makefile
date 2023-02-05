say_hello:
	echo "Yo yo yo"


install:
	pip install -r requirements.txt


# linters 
make format:
	black scr

make check:
	flake8 scr
