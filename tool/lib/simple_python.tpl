{%- extends 'null.tpl' -%}

{%- block input %}
{{ cell.source | ipython2python }}
{%- endblock input %}

{% block output -%}
{{ output.data['text/plain'] | comment_lines }}
{% endblock output -%}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}