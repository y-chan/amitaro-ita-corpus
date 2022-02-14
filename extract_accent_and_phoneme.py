with open("accent_and_phoneme.csv") as f:
    labels = f.read().split("\n")

phonemes = []
accents = []

is_accent = False

for label in labels:
    if is_accent:
        label = label.replace(", ", ",").replace("   ", " ").replace("  ", " ")
        accents.append(label)
    else:
        phonemes.append(label)
    is_accent = not is_accent

with open("phoneme.csv", mode="w") as f:
    f.write("\n".join(phonemes))

with open("accent.csv", mode="w") as f:
    f.write("\n".join(accents))
