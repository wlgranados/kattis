import argparse
import os
import sys
from bs4 import BeautifulSoup, element
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
        soup_logic(soup)

        if dir_path is None:
            dir_path = os.getcwd()
    except exceptions.HTTPError as err:
        print(str(err))


def soup_logic(soup):
    """
    Logic handler to parse problems
    :param soup: Soup object from BS4
    :return:
    """
    # holds over-all problem info
    problem_info = """"""
    problem_sidebar_info_raw = soup.findAll("div", {"class": "sidebar-info"})[2]

    # grab sidebar-info
    for ele in problem_sidebar_info_raw.find_all("p")[:-1]:
        problem_info += ele.text + "\n"

    # grab main div content
    problem_main_info_raw = soup.findAll("div", {"class": "problem-wrapper"})
    for ele in problem_main_info_raw:
        title = ele.find("div", {"class": "headline-wrapper"}).text
        problem_info += "\nProblem: " + title + "\n"
        body = ele.find("div", {"class": "problembody"})
        for tag in body:
            if tag.name != "table":
                print(tag.get_text())

    # print(problem_info)


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
