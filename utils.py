#!/usr/bin/python
# -*- coding: utf-8 -*- 

def write_md(fname, data, charset='utf-8'):
    tmp = fname + ".md"
    try:
        with open(tmp, 'wt') as f:
            f.write(data.encode(charset))
        
        print("write file: %s success" % tmp)
    except IOError:
        print("write file: %s error" % tmp)

def append_md(fname, data, charset='utf-8'):
    tmp = fname + ".md"
    try:
        with open(tmp, 'a') as f:
            f.write(data.encode(charset))
        
        print("append file: %s success" % tmp)
    except IOError:
        print("append file: %s error" % tmp)

def read_md(fname, charset='utf-8'):
    tmp = fname + ".md"
    try:
        with open(tmp, 'rt') as f:
            return f.read().decode(charset)
    except IOError:
        print("read file: %s error." % tmp)
    return None
    
