import argparse

paser = argparse.ArgumentParser(description="For test and Help",epilog="GoodBye",
                                prefix_chars='-')


paser.add_argument('--echo',help="show your message")
paser.add_argument('--number','-n',help="number target")
paser.add_argument('-v','--verbose',action='store_true')


argmts = paser.parse_args()


print(argmts.echo)
if argmts.verbose:
    print("JOINED")