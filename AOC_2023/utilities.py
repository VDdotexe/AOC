def parsing_multi(file_):
    with open(file_, 'r') as f:
        content = f.readlines()
    content = [i.replace("\n", "") for i in content]
    return content