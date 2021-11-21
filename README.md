# Test things
- - -
This is a sample of basic Django app to test some codes, and functionalities in basic way.
- - -
### Index
1. [Install](#install)
    1. [OS Requirements installation](#os-requirements-installation)
        + [Ubuntu and derivatives](#ubuntu-and-derivatives)
        + [Windows](#windows)
    2. [Clone the Repository](#clone-the-repository)
    3. [Create and Activate a virtualenv](#create-and-activate-a-virtualenv)
    4. [PiP Requeriments installation](#pip-requeriments-installation)
    5. [Run development Django server](#run-dev-django-server)
2. [Things to test](#things-to-test)
    1. [Get data from another api and expose in endpoint activating basic CORS headers](#get-data-from-another-api-and-expose-in-endpoint-activating-basic-cors-headers)

- - -
### Install

##### OS Requirements installation
* ###### Ubuntu and derivatives
```bash
$ sudo apt install build-essential python3 python3-dev python3-pip python3-wheel python3-setuptools python3-virtualenv python3-virtualenvwrapper git
```
* ###### Windows 
  
Install [Python3 64bit](https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe)
or [Python3 32bit](https://www.python.org/ftp/python/3.8.7/python-3.8.7.exe) then 
configure so that [python appears in the Windows PATH](https://datatofish.com/add-python-to-windows-path/)

##### Clone the Repository
```bash
$ git clone https://github.com/ReynaldoCC/teststhings.git
```

#### Create and Activate a virtualenv
```bash
$ virtualenv testenv -p python3
$ source testenv/bin/activate
```
#### PiP Requeriments installation
```bash
$ pip3 install -r <path/to/project/folder>/requeriments.txt
```

#### Run dev Django server
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```


### Things to test

#### Get data from another api and expose in endpoint activating basic CORS headers

This is a test to get data from de url "https://newsapi.org/v2/top-headlines?country=cu&language=es&apiKey=33b6de14b85345a8b0142a85128ffe59" and expose it in this server but activating CORS headers, the data is fetched with requests library and is exposed in "/data/" endpoint.
With default configuration must get data requesting http://127.0.0.1:8000/data/


