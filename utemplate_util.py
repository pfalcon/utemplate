import sys
import os
import os.path
try:
    import uio as io
except ImportError:
    import io
import utemplate.source
import utemplate.compiled


if len(sys.argv) < 3:
    print("Usage: %s <cmd> <template> [<template arg>...]" % sys.argv[0])
    sys.exit(1)

cmd = sys.argv[1]
package = None

if cmd == "rawcompile":
    out_name = sys.argv[2].replace(".", "_") + ".py"
    with open(sys.argv[2]) as f_in, open(out_name, "w") as f_out:
        c = utemplate.source.Compiler(f_in, f_out)
        c.compile()

if cmd == "compileall":
    sys.path.insert(0, ".")
    loader = utemplate.source.Loader(package, ".")
    for cur_path, dirs, files in os.walk(sys.argv[2]):
        for f in files:
            if f.endswith(".py"):
                continue
            fname = cur_path + "/" + f
            print(fname)
            loader.load(fname)

elif cmd == "compile":
    loader = utemplate.source.Loader(package, ".")
    try:
        os.unlink(loader.compiled_path(sys.argv[2]))
    except:
        pass
    # Compiled file created from the current dir, but imported from
    # sys.path, so make sure current dir is in sys.path.
    sys.path.insert(0, ".")
    render = loader.load(sys.argv[2])

elif cmd == "render":
    loader = utemplate.compiled.Loader(package, ".")
    render = loader.load(sys.argv[2])
    for x in render(*sys.argv[3:]):
        sys.stdout.write(x)

elif cmd == "run":
    f_out = io.StringIO()
    with open(sys.argv[2]) as f_in:
        c = utemplate.source.Compiler(f_in, f_out,
            loader=utemplate.source.Loader(None, os.path.dirname(sys.argv[2]) or "."))
        c.compile()
    ns = {}
    exec(f_out.getvalue(), ns)
    for x in ns["render"](*sys.argv[3:]):
        sys.stdout.write(x)

else:
    print("Unknown command:", cmd)
