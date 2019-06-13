import subprocess
import os

# cleanup of state
try:
    os.unlink("out.txt")
except:
    pass
try:
    os.unlink(".sconsign.dblite")
except:
    pass

print("Build the example, makes an out.txt file")
print()
subprocess.call("scons --debug=explain",shell=True)
print()
print("notice a rebuilt shows everything is up-to-date")
print()
subprocess.call("scons --debug=explain",shell=True)
print()
print("We modify the file with some random data to show the user changing the target file")
print()
with open("out.txt","w") as ofile:
    ofile.write("Some new data")

print("Try to build the again.. scons says everything is up-to-date")
print("This is currently correct behavior in scons, but the user may have expected")
print("the build system to rebuild the target as it was modified")
print()
subprocess.call("scons --debug=explain",shell=True)

print()
print("The only way to do this is to --clean or del/rm the target file")
print("(deleting file in this case)")
print()
os.unlink("out.txt")
subprocess.call("scons --debug=explain",shell=True)

