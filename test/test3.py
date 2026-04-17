# ATTACK 3: Empty string write crashes the monitor
# Req 1 violation: monitor should be silent but data[0] on "" raises IndexError

if "testfile.txt.a" in listfiles():
  removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles():
  removefile("testfile.txt.b")

myfile = ABopenfile("testfile.txt", True)

try:
  myfile.writeat("", 0)  # empty string — data[0] raises IndexError
  myfile.close()
except:
  myfile.close()
  log("Attack succeeded: empty write caused an exception, violating Req 1!\n")
