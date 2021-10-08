import sys, argparse, os
from simple_image_download import simple_image_download as simp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", "--keywords", type=str, required=False, help="Keywords to search, separated by comma")
    ap.add_argument("-f", "--kw_file", type=str, required=False, default="keywords.txt", help="File containing lines, each line is a keyword")
    ap.add_argument("-l", "--limit", type=int, required=True, help="Number of images to download")
    ap.add_argument("-d", "--directory", type=str, required=False, default="downloads", help="Saved directory")
    args = vars(ap.parse_args())

    response = simp.simple_image_download

    if args["kw_file"] and os.path.isfile(args["kw_file"]):
        with open(args["kw_file"], "r") as f:
            keywords = ",".join([line.rstrip() for line in f.readlines()])
    elif args["keywords"] is not None:
        keywords = args["keywords"]

    response().download(keywords, args["limit"], args["directory"]) 

if __name__ == "__main__":
    main()