def myGrep(filename, target):
      '''prints every line of file filename containing str target'''
      infile = open(filename)
      for line in infile:
            if target in line:
                  print(line, end='')

myGrep('testfile.txt', 'Ann')