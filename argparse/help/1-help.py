import argparse

paser = argparse.ArgumentParser()

paser.add_argument('--echo')

argmts = paser.parse_args()

print(argmts)