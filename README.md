# deafualt repo setup

This is simple app based on [Django tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

Functionality goals:
- it allows to give votes
- it tracks votes of users
    - user provides name
    - providing name that exists in db allows to overwrite previous vote


### python env setup
1. install pyenv
2. run `pyenv install 3.10.7`
3. set python 3.10.7 as local version with `pyenv local 3.10.7`

run:
```shell
python -m venv .venv
source .venv/bin/activate
```

### python libraries
`make install`


### Run main
`python main.py`
