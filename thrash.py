# Author : Ali Snedden
# Date   : 07-feb-2024
# License: GPL-3.0
#
# Questions
#
# Thoughts :
#
# Note :
"""Takes ngb and niter and creates niter files and reads from them niter times
"""
import os
import sys
import time
import argparse
import warnings
import numpy as np


def main():
    """

    Args:

    Returns:

    Raises:
    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--niter', metavar='niter',
                         type=int, help='Number of loop iterations')
    parser.add_argument('--ngb', metavar='ngb',
                         type=float, help='Approximate size of files to write in'
                                           'GB, is float')
    parser.add_argument('--path', metavar='path',
                         type=str, help='Path/Name of output file to '
                                          'read/write/rewrite')
    print("Started : {}".format(time.strftime("%D:%H:%M:%S")))
    start = time.time()
    args = parser.parse_args()
    niter = args.niter
    ngb = args.ngb
    path = args.path
    for n in range(niter):
        print("iter = {}".format(n))
        # Make 4 byte floats
        size = int(np.sqrt(ngb * 10**9 / 4))
        m = np.zeros([size,size], dtype=np.float32)
        # write
        np.save(path, m, allow_pickle=True)
        # read
        mread = np.load(path)


    print("Ended : {}".format(time.strftime("%D:%H:%M:%S")))
    print("Run Time : {:.4f} s".format((time.time() - start)))
    sys.exit(0)


if __name__ == "__main__":
    main()
