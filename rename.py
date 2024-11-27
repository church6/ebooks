#!/usr/bin/python3
"""
# @filename    :  rename.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-11-27T16:21:53+08:00
# @require     :  Python 3.12.3
# @function    :
"""

import os
import time


def work():
    """
    Function :
    """
    for entry in os.scandir("/data/books/pdfs"):
        if entry.is_file():
            if entry.name.endswith("pdf"):
                name = (
                    entry.path.replace(" ", "_")
                    .replace("（", "(")
                    .replace("）", ")")
                    .replace("-", "_")
                    .replace("【", "[")
                    .replace("】", "]")
                    .replace("：", "_")
                    .replace("？", "_")
                    .replace("，", "_")
                    .replace("、", "_")
                    .replace("《", "_")
                    .replace("》", "_")
                    .replace("•", "_")
                    .replace("！", "_")
                    .replace('"', "_")
                )
                name = name.replace("_", "").replace(":", "")
                print(name)
                os.rename(entry.path, name)
        else:
            print(f"FIXME={entry.path}")


def measurer(func):
    """
    Function : measurer
    """

    def wrapper(*args, **kwargs):
        """
        Function : wrapper
        """
        start = time.time()
        func(*args, **kwargs)
        print(f"# elapsed time:{time.time() - start}")

    return wrapper


# @measurer
def main():
    """
    Function : main
    """
    work()


if __name__ == "__main__":
    main()
