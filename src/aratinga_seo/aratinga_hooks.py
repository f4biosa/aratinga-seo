"""
Registers aratinga-seo icon in the admin dashboard.
"""

from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    """
    Add custom SVG icons to the Aratinga admin.
    """
    icons.append("aratinga_seo/icons/line-chart.svg")
    return icons
