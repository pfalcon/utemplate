import sys
import uos as os
import uio as io
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

if cmd == "compile":
    loader = utemplate.source.Loader(package, ".")
    try:
        os.unlink(loader.compiled_path(sys.argv[2]))
    except:
        pass
    render = loader.load(sys.argv[2])

elif cmd == "render":
    loader = utemplate.compiled.Loader(package, ".")
    render = loader.load(sys.argv[2])
    for x in render(*sys.argv[3:]):
        sys.stdout.write(x)

elif cmd == "run":
    f_out = io.StringIO()
    with open(sys.argv[2]) as f_in:
        c = utemplate.source.Compiler(f_in, f_out)
        c.compile()
    ns = {}
    exec(f_out.getvalue(), ns)
    for x in ns["render"](*sys.argv[3:]):
        sys.stdout.write(x)

else:
    print("Unknown command:", cmd)
