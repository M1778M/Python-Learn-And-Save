import argparse

paser = argparse.ArgumentParser()
#required if not have raise error
paser.add_argument('--echo', default="Hello::")
paser.add_argument('--format',choices=["py",'exe','js'])
paser.add_argument("-c",default="compile",type=str)
paser.add_argument('--ID',type=str)



argmts = paser.parse_args()


print("{}, {}     not = {}|".format(argmts.echo, argmts.format,argmts.c))