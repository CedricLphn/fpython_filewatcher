from src.models.cli_parser import cli_parser

import logging

def main():
    """

    """
    _run = False
    _with_logs = False
    ## parse arguments
    get_list = cli_parser()
    if get_list is not None:

        if len(get_list) > 1:
            ## do thing with monitoring
            _run = True
            if len(get_list) == 3:
                _with_logs = True

    if _run is True:
        ## continue
        condition = _with_logs == True
        msg = ", logs writing" if condition else ", logs off"
        print("lets go", msg)




if __name__ == '__main__':
    main()