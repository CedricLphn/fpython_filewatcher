from src.load_yaml import load_config

import argparse, os
"""Parser of arguments from cli

"""
parser = argparse.ArgumentParser(description="Intro à remplir")
## set exclusive
group = parser.add_mutually_exclusive_group()
## set all arguments possibilities
group.add_argument("-d", "--directory", action="store_true", help="directory name")
group.add_argument("-i", "--interval", type=int, help="number of seconds")
group.add_argument("-c", "--config", type=str, help="filename config [interval, directory]")
group.add_argument("-l", "--logging", type=str, help="config filename")

## get args
args = parser.parse_args()

## if directory given
if args.directory:
    ## change the directory by the argument passed for --directory
    os.chdir(args.directory)
    print(os.getcwd())

## if interval given
if args.interval:
    ## get the interval duration
    _interval = args.interval

## if file config given
if args.config:
    ## load YAML config file
    config_yaml = load_config('')



