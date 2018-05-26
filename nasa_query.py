import argparse



def args_check():

    parser = argparse.ArgumentParser(description="NASA Image & Video Query")
    parser.add_argument("--pname", type=str, default="ilan ramon", help="Search Person Query")
    parser.add_argument("--msize", type=int, default=1000, help="Minimum File Size")

    return parser.parse_args()
if __name__ == "__main__":
    args = args_check()