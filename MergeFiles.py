import glob

read_files = glob.glob("./data/acteur/*.json")

with open("./data/liste_depute_histoirique.json", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())