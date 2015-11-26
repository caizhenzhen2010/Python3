from fileinput import FileInput
def lines(file):
    for line in FileInput(file):yield line
    yield '\n'


def blocks(file):
    block=[]
    for line in lines(file):
        if str(line).strip():
            block.append(str(line))
        elif block:
            yield ''.join(block).strip()
            block=[]
