#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    from markdown2 import Markdown
    import markdown2

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    if fdp.ConsumeBool():
        markdown2.markdown(fdp.ConsumeRemainingString())
    else:
        markdowner = Markdown()
        markdowner.convert(fdp.ConsumeRemainingString())
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
