import sys
import io
import utemplate.source
import utemplate.compiled


cmd = sys.argv[1]
if cmd == "compile":
    out_name = sys.argv[2].replace(".", "_") + ".py"
    with open(sys.argv[2]) as f_in, open(out_name, "w") as f_out:
        c = utemplate.source.Compiler(f_in, f_out)
        c.compile()

elif cmd == "render":
    render = utemplate.compiled.load(sys.argv[2])
    for x in render():
        sys.stdout.write(x)

elif cmd == "run":
    f_out = io.StringIO()
    with open(sys.argv[2]) as f_in:
        c = utemplate.source.Compiler(f_in, f_out)
        c.compile()
    ns = {}
    exec(f_out.getvalue(), ns)
    for x in ns["render"]():
        sys.stdout.write(x)

else:
    print("Unknown command: ", cmd)
