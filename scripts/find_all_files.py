import argparse
import os
import argparse
import os
import sys
from logging import DEBUG, basicConfig, getLogger


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


def main(argv=[]):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory", type=str, help="directory that you hope to look into."
    )
    parser.add_argument(
        "-e", "--extension", type=str, help="specify files with extension"
    )
    parser.add_argument("-c", "--cat", help="cat the file", action="store_true")
    parser.add_argument("-w", "--wc", help="wc the file", action="store_true")
    args = parser.parse_args()

    for file in find_all_files(args.directory):
        if args.extension:
            extension = file.split(".")[-1]
            if extension != args.extension:
                continue

        if args.wc:
            os.system("wc " + file)
        else:
            print(file)

        if args.cat:
            print("##### HEAD OF THE FILE #####\n\n")
            for line in open(file):
                print(line, end="")
            print("##### END OF THE FILE #####\n\n")


if __name__ == "__main__":
    basicConfig(
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    main(sys.argv[1:])
    logger.info("DONE")
