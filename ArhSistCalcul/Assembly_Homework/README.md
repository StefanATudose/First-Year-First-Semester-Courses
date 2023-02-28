Teme assembly, sintaxa AT&T x86 (a se folosi un terminal de linux, dar cred ca merge cu orice unix).

ex1 este cerinta 1 de la tema 1
ex2 este cerinta 1 de la tema 2

Scripturile de python sunt pentru evaluator


Comenzi compilare:
$ as --32 ex1.asm -o ex1.o
$ gcc -m32 ex1.o -o ex1

La fel si cu ex2

Comenzi pentru pentru scripturi:
sudo apt install python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
sudo python2 get-pip.py
pip2 install pwn
pip2 install pathlib2

Rulare script
python2 script1.py
python2 script2.py
