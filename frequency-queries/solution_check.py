import os
import filecmp
import difflib

solution_file = 'output07.txt'

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    file1_path = os.path.join(scr_dir, './output/output.txt')
    file2_path = os.path.join(scr_dir, './output/' + solution_file)
    print(filecmp.cmp(file1_path, file2_path))

    '''lines1 = open(file1_path).readlines()
    lines2 = open(file2_path).readlines()
    for line in difflib.unified_diff(lines1, lines2, fromfile='file1', tofile='file2', lineterm=''):
        print(line)'''