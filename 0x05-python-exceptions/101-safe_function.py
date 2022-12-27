#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        retu = fct(*args)
        return retu
    except Exception as e:
        print("EXception: {}".format(e), file=sys.stderr)
        return None
