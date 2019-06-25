### Summary
This is an example that shows rebuilds on targets do not depend on the CSIG of the target itself.

## How to run
To see this run `python run.py` in this directory. This will run a set of commands to show the behavior. The sample itself will print out the csig value of the target to help show this behavior.

The script will:
1) run a build
2) run it again to show everything is up-to-date
3) modify the output target (out.txt in this case)
4) run the build again
   1) This will show the rebuild failed and how we now have bad state on disk
5) delete the out.txt to show it is the only modifiation we can make to the target which will cause it to rebuild
   1) This is not about changes to sources, but to the target itself


## What is expected

Step 4) from the above should have rebuilt the target and put the tree in a good known state