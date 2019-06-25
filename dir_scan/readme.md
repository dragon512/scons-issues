### Summary
This is a simple example that shows builders do not process scanners on directory nodes that are part of the target list

## How to run
To see this run `scons` in this directory

you should see output such as this:

```
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
('Source scanner node=', <SCons.Node.FS.File object at 0x0000000003D559B0>, 'builder =', 'mybld')
write_file(["outdir"], ["some_source.txt"])
scons: done building targets.
```

This shows that the scanner only ran with the source, not the target

## What is expected
output such as this is expeceted
```
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
('Target scanner node=', <SCons.Node.FS.Dir object at 0x0000000003D559B0>, 'builder =', 'mybld')
('Source scanner node=', <SCons.Node.FS.File object at 0x0000000003D559B0>, 'builder =', 'mybld')
write_file(["outdir"], ["some_source.txt"])
scons: done building targets.
```


## Other side issues this shows as well

The command of `scons -c` does not clean the directory target of this builder.

This can be worked around by explictly calling `Clean()` on the target output of the builder

