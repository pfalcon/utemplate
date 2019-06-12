utemplate
=========

`utemplate` is a lightweight and memory-efficient template engine for
Python, primarily intended for use with MicroPython
(https://github.com/micropython/micropython).

`utemplate` syntax is roughly based on Django/Jinja2 syntax (e.g.
`{% if %}`, `{{var}}`), but only the most needed features are offered
(for example, "filters" are syntactic sugar for function calls, and
so far are not planned to be implemented).

`utemplate` compiles templates to Python source code, specifically to
a generator function which, being iterated over, produces consecutive
parts (substrings) of a rendered template. This allows for minimal
memory usage during template substitution (with MicroPython, it starts
from mere hundreds of bytes). Generated Python code can be imported as
a module directly, or a simple loader class is provided for convenience.
There is also a loader class which will compile templates on the fly,
if not already compiled (currently not automatically recompiled if
changed, this is on TODO).

To test/manage templates, `utemplate_util.py` tool is provided. For
example, to quickly try a template (assuming you are already in
`examples/` dir):

    micropython ../utemplate_util.py run squares.tpl

or

    python3 ../utemplate_util.py run squares.tpl

Templates can take parameters (that's how dynamic content is generated).
Template parameters are passed as arguments to a generator function
produced from a template. They also can be passed on the `utemplate_util.py`
command line (arguments will be treated as strings in this case, but
can be of any types if called from your code):

    micropython ../utemplate_util.py run test1.tpl foo bar

Examples
--------

`examples/squares.tpl` as mentioned above has following content:

```
{% for i in range(5) %}
| {{i}} | {{"%2d" % i ** 2}} |
{% endfor %}
```

More examples are available in [examples/](examples/) directory.

If you want to see a complete example web application which uses utemplate,
refer to https://github.com/pfalcon/notes-pico .

License
-------

`utemplate` is written and maintained by Paul Sokolovsky. It's available
under the MIT license.
