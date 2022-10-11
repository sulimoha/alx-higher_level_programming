def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value), end="\n")
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
