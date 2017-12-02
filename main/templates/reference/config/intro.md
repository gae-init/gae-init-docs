{% raw %}

All the variables that are defined in the `config.py` can be also used in the in the Jinja2 templates as well. For example if you want to refer to the brand name or a current version you could use it like: `{{config.CONFIG_DB.brand_name}}` or `{{config.CURRENT_VERSION_ID}}` respectively.

{% endraw%}
