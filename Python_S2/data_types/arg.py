import argparse
# basic uses
parser = argparse.ArgumentParser(usage="possible arguments will be listed here",description="this program explains how it works")
# add_argument(name of argument, **kwargs), **kwargs allow a flexible dictionary arguments 
parser.add_argument("hello", type=str, default="hello world", help="greeting")
parser.add_argument("--optional",nargs='+', help=" nargs allows the current argument expect one or more args using  '*,+,?' or N which is the number of args ")

args = parser.parse_args()
print(args.hello)

def key_args(**kwawrgs):
    for key, value in kwawrgs.items():
        print(f"{key}: {value}")
key_args(name="Alice", age=30, city="New York")