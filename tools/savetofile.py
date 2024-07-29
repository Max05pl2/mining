def save_to_file(path, text):
    f = open(path, 'a', encoding="utf-8")
    f.write(text)
    f.close()