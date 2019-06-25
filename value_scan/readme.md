### Summary
This is a simple example that shows builders do not process scanners, both source and target versions, on Value nodes in a builder.

## How to run
To see this run `scons` in this directory

you should see output such as this:

```
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
Source scanner node= some_source.txt builder = mybldf
Target scanner node= in.txt builder = mybldf
write_file(["in.txt"], ["some_source.txt"])
Write file builder ------
 Build - Source some_source.txt b'some data'
 Build - Target in.txt b''
Target scanner node= out.txt builder = mybldf
write_file(["out.txt"], ['out-value'])
Write file builder ------
 Build - Source out-value b'out-valuein-value'
 Build - Target out.txt b''
Target scanner node= out2.txt builder = mybldf
Source scanner node= in.txt builder = mybldv2
write_value2(['out-value2'], ["in.txt"])
Value builder two------
 Build - Source in.txt b'This is some data'
 Build - Target out-value2 b'out-value2This is some data'
 Build - Target result out-value2 b'out-value2This is some data'
Target scanner node= out2.txt builder = mybldf
write_file(["out2.txt"], ['out-value2'])
Write file builder ------
 Build - Source out-value2 b'out-value2This is some data'
 Build - Target out2.txt b''
scons: done building targets.
```

This example show four builders that the show the combinations of target/source of Value and File Nodes. Only the file nodes have the scanner applied to them. This example also show some behaviors with builders that try to build Values don't work as expected as well, however this sample is targeted at the moment for scanners.

## What is expected
Output should show scanner being called on the Value nodes themselves.

