from pathlib import Path

def combine_text_files(dirpath, out_filename):
    '''
    This function combines text files in `dirpath` and combines them into `out_filename`.
    `out_filename` is placed in the parent directory to dirpath.
    '''

    # convert filename to path
    outpath = dirpath.parent
    outpath = dirpath.joinpath(out_filename)

    # read files
    counter = 0
    with open(outpath, "w") as new_file:
        for file in dirpath.glob("*.txt"):
            reader = f.open(file, "r")
            contents = reader.read()
            new_file.write(contents + "\n")
            reader.close()

            if (counter % 1000) == 0:
                print(f"Reading file #{counter}.")
            counter += 1

    print("Done!")
