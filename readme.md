to try out:
- numba
- pypy
- codon

# Setup virtualenv

```
python3 -m venv venv
pip install numba numpy
. venv/bin/activate
```


# Numba
instructions

```
python3 numba_basic.py
```


# Pypy
setup instructions

```
curl -LO third_party/pypy.tar.bz2 https://downloads.python.org/pypy/pypy3.10-v7.3.16-linux64.tar.bz2
(cd third_party && tar -xjvf pypy.tar.bz2)
virtualenv -p third_party/pypy/bin/pypy venv_pypy
python3 pypy_basic.py
```


# Codon
setup instructions
```
/bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
~/.codon/bin/codon build codon_basic.py -o codon_out
./codon_out
```
