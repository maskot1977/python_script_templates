import argparse
import os
import sys
from logging import DEBUG, basicConfig, getLogger


def function(args):
    logger.debug(args)


def main(argv=[]):
    environment_key = os.environ.get("ENVIRONMENT_KEY", None)
    logger.info(environment_key)

    parser = argparse.ArgumentParser(
        description="Please describe what you intend here."
    )

    parser.add_argument("dragon", type=str, help="This is a positional argument.")
    parser.add_argument("--freeza", type=int, help="fuga", default=530000)

    parser.add_argument("-o", "--out", type=str, help="output")

    args = parser.parse_args(argv)

    function(args)


if __name__ == "__main__":
    basicConfig(
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    main(sys.argv[1:])
    logger.info("DONE")
