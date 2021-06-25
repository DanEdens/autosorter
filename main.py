import os
sorter = os.environ.get('sorting')


def print_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))
            continue
        else:
            continue


if __name__ == '__main__':
    print_files(sorter)

