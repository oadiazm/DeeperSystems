#!/bin/bash
if [ "$(uname)" == "Darwin" ]; then
  echo "Mac OS X platform"
  if [ ! -d ./venv/ ]; then
    pyvenv-3.5 venv
    source venv/bin/activate
    pip install --upgrade pip
    #brew install postgres
    export PATH=$PATH:/usr/local/Cellar/postgresql/9.6.1/bin/
    export LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
    pip install -r requirements.txt
    chmod u+x manage.py
    deactivate
  else
    source venv/bin/activate
    pip install -r requirements.txt
    #python manage.py collectstatic
    deactivate
  fi
else
  echo "Not Mac OS X platform"
fi
