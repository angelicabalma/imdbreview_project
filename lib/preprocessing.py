from pathlib import Path

import re

def combine_text_files(dirpath, out_filename):
    '''
    This function combines text files in `dirpath` and combines them into `out_filename`.
    `out_filename` is placed in the parent directory to dirpath.
    '''

    # convert filename to path
    outpath = dirpath.parent
    outpath = outpath.joinpath(out_filename)

    # read files
    counter = 0
    with open(outpath, "w") as new_file:
        for file in dirpath.glob("*.txt"):
            reader = open(file, "r")
            contents = reader.read()
            new_file.write(contents + "\n")
            reader.close()

            if (counter % 1000) == 0:
                print(f"Reading file #{counter}.")
            counter += 1

    print("Done!")
    

def normalize_reviews(text):
    '''
    This function normalizes string data to be lowercase, have no punctuation, and be only characters [a-z]
    
    With help from Angelica B.
    '''
    text = text.lower() 
    text = text.replace("<br />", " ")
    text = re.sub(r"[^a-z ]", " ", text)
    text = re.sub(r" +", " ", text)
    filtered = []
    for w in tokens:
        if w not in stopwords and w not in punctuation:
            filtered.append(w)
    return filtered