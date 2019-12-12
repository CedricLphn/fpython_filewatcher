import src.sqlite as db
from src.checksum import *
from os import listdir
from os.path import isfile, join
import time
from src.models.cli_parser import cli_parser
import logging

def main():
    """Main module

    
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
    
    __EXAMPLE_FOLDER__ = "example/"
    db.init()

    print("Deamon ready")

    while True:
        files = [f for f in listdir(__EXAMPLE_FOLDER__) if isfile(join(__EXAMPLE_FOLDER__, f))]
        db_files = db.select_filename()
        print(">> FILES: ", files)
        print(">> SQL: ", db_files)
        for file in files:
            # TO DO : PENSER A FAIRE LES FICHIERS SUPPRIME
            # Delete all files existing in folder and database
            for db_file in db_files:
                if(db_file == file):
                    del db_files[db_files.index(file)]

            # File exist in db
            checksum = checksum_file(__EXAMPLE_FOLDER__ + file)
            if(db.count(file) > 0):
                if(db.select(file)[2] != checksum):
                    print("> File changed", file)
                    if(db.update_signature(file, checksum) == False):
                        print("(!) Error while updating database")
            else:
                print("> New file detected", file)
                db.write(file, __EXAMPLE_FOLDER__, checksum)
                
        print("new db file", db_files)

        # Detect file removed here
        for deleted in db_files:
            if(db.remove_filename(deleted)):
                print(">", deleted, "removed")
            else:
                print("(!) Error remove filename in database")

        time.sleep(3.5) # in sec

if __name__ == '__main__':
    main()