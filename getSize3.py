import os

path = 'c:\\' # Set a path here
totalSize = 0

for filename in os.listdir(path):
    if not os.path.isfile(os.path.join(path, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(path, filename))

print(totalSize)
