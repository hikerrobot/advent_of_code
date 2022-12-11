import logging

def get_file_contents(filename):
    #  TODO get logger working. too tired... yawn
    logging.info("reading file {}".format(filename))
    with open(filename) as f:
        lines = f.read().splitlines()

    return tuple(lines)