#!/bin/bash

dmd -g -c -fPIC -ofdelfhook.o elfhook.d
perl Makefile.PL
make
LD_PRELOAD=$HOME/dmd2/linux/lib64/libphobos2.so perl hoge.pl
