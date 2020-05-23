import argparse
import os
import sys

from bs4 import BeautifulSoup
from requests import get, exceptions


def import_problem_info(problem_url: str, dir_path: str = ""):
    """
    Import problem
    :param problem_url: URL to kattis problem
    :param dir_path: Path to directory for output
    :return:
    """
    try:
        r = get(problem_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup.prettify())

        if dir_path is None:
            dir_path = os.getcwd()
            print(dir_path)
    except exceptions.HTTPError as err:
        print(str(err))


def main():
    """
    Driver function to run script
    """
    try:
        parser = argparse.ArgumentParser(description="Import Open Kattis problem information from given URL")
        parser.add_argument("url=", help="The url to your Open-Kattis problem", type=str)
        parser.add_argument("--dir", help="Directory where you want to store the output information",
                            type=str)
        args = vars(parser.parse_args())
        output_dir = args["dir"]
        problem_url = args["url="].split('=')[1]

        if problem_url is not None:
            import_problem_info(problem_url, output_dir)
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)


if __name__ == "__main__":
    main()
