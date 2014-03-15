<p>
  All the variables that are defined in the <code>config.py</code> can be also
  used in the in the Jinja2 templates as well. For example if you want to refer
  to the brand name or a current version you could use it like:
  <code>&#123;&#123;config.CONFIG_DB.brand_name&#125;&#125;</code> or
  <code>&#123;&#123;config.CURRENT_VERSION_ID&#125;&#125;</code>
  respectively.
</p>
