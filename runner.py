import os.path

pythonFiles = []


# Utility function to check if we should run this file for tests
def shouldRun(file):
    return file.endswith(".py") and 'runner.py' not in file


for dirPath, dirNames, fileNames in os.walk("."):
    for fileName in [f for f in fileNames if shouldRun(f)]:
        pythonFiles.append(os.path.join(dirPath, fileName))

# Execute all our files
# Will throw an exception if any tests fail
for pyFile in pythonFiles:
    exec(open(pyFile).read())
