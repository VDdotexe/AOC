def parsing_multi(file_):
    with open(file_, 'r') as f:
        content = f.readlines()
    content = [i.replace("\n", "") for i in content]
    return content


def parsing_multi_ravi(file_):
    with open(file_, 'r') as f:
        content = f.read()
    content = content.split('\n')
    return content






