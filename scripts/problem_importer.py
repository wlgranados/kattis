import getopt, sys
from requests import get


def import_problem_info(problem_url: str):
    """
    :return:
    """
    pass


def usage() -> str:
    """
    Provide usage guideline for script
    :return: Usage string
    """
    return """Usage: 
                    problem_importer.py --url=<input_url> --dir=<output_directory>
                    or
                    problem_importer.py -u <input_url> -o <output_directory>
            """


def main():
    """
    Driver function to run script
    :param argv: Command line arguments passed into script
    """
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "hud", ['help', 'url=', 'target_dir='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    problem_url = None
    output_dir = None
    for opt, arg in optlist:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-u", "--url"):
            problem_url = arg
        elif opt in ("-d", "--dir"):
            output_dir = arg
        else:
            assert False, "unhandled option"



if __name__ == "__main__":
    main()
