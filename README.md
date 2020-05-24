# Kattis

Open Kattis solutions to problems in various languages

## Instructions

To use the `problem_importer.py` script there are 2 command line arguments:

1. `url=<PROBLEM_URL>` : (required) used to specify the problem url.
2. `--dir <DIR_PATH>` : (optional) used to specify directory to store files.

If no directory is provided then by default, the script assumes you have a similar folder structure as this repo, and creates
a folder for the problem within `/src/<problem_name>` and adds the information pertaining within.

#### Run Command:

```bash
python problem_importer.py url="PROBLEM_URL" --dir "PATH_TO_DIRECTORY"
```
