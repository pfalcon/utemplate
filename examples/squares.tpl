{% args n=5 %}
{% for i in range(n) %}
| {{i}} | {{"%2d" % i ** 2}} |
{% endfor %}
