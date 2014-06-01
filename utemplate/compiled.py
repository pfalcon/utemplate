def load(name):
    # Load from explicit filename
    f = open(name)
    code = f.read()
    f.close()
    ns = {}
    exec(code, ns)
    return ns["render"]


class Loader:

    def __init__(self, dir):
        self.dir = dir

    def load(self, name):
        # Load by template name from standard location
        return load(self.dir + "/compiled/" + name + ".py")
