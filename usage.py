from pathlib import Path

from RDR import rdr, evaluate

file = Path("./input/rdr_input.txt")
dump = file.read_text(encoding="utf-8-sig")

rdr(str(file), "train")

to_tag = "./input/rdr_input.txt.RAW"
model = "./input/rdr_input.txt.RDR"
lexicon = "./input/rdr_input.txt.DICT"
rdr(to_tag, model=model, lexicon=lexicon, mode="tag")

expected_dump = Path("./input/rdr_input.txt").read_text(encoding="utf-8-sig")
actual_dump = Path("./input/rdr_input.txt.RAW.TAGGED").read_text(encoding="utf-8-sig")

ev = evaluate(file, "./input/rdr_input.txt.RAW.TAGGED")
print()
