import argparse

from src.models.load_yaml import load_config


def cli_parser():
    """Parser of arguments from cli

    """
    parser = argparse.ArgumentParser(description="Monotoring of directory contents")

    ## set all arguments possibilities
    root_group = parser.add_mutually_exclusive_group()
    parser.add_argument("-d", "--directory", type=str, help="directory name")
    parser.add_argument("-i", "--interval", type=int, help="number of seconds")
    parser.add_argument("-l", "--logging", type=str, help="logging config filename")

    group_list_config = root_group.add_mutually_exclusive_group()
    group_list_config.add_argument("-c", "--config", type=str, help="[interval int in seconds, directory path] config yaml filename")

    ## get args
    args = parser.parse_args()

    ## if logging file config given
    if args.logging:
        _logging = args.logging
        if _logging != "true":
            print("Logging error : must be set on '-l true' to handle debugs, infos, warnings")


    ## if yaml file config given
    if args.config:
        ## load YAML config file
        _config_yaml = load_config(args.config)
        _interval = _config_yaml['interval']
        _directory = _config_yaml['directory']
        print("new path to monitor : ", _directory)
        print("interval : ", _interval)
        exit()

    ## if directory given
    if args.directory:
        ## change the directory by the argument passed for --directory
        _directory = args.directory
        print("new path to monitor : ", _directory)

    ## if interval given
    if args.interval:
        ## get the interval duration
        _interval = args.interval
        print("interval : ", _interval)
