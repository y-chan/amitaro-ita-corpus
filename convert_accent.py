import numpy
import os

accent_symbols = [
    "[",  # pitch up
    "]",  # pitch down
    "#",  # accent boundary
    "?",  # accent boundary(question)
    "_",  # not changing accent
]

accent_to_id = {s: i for i, s in enumerate(accent_symbols)}
id_to_accent = {i: s for i, s in enumerate(accent_symbols)}


with open("accent.csv") as f:
    accents = f.read().split("\n")
    basenames = [text.split(",")[0] for text in accents]
    accents = [text.split(",")[1] for text in accents]

for i, accent in enumerate(accents):
    basename = basenames[i]
    accent_seq = numpy.array([accent_to_id[a] for a in accent.split(" ")])
    accent_filename = f"{basename}.npy"
    numpy.save(os.path.join("accent", accent_filename), accent_seq)
