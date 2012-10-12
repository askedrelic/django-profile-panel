Django Debug Profile Toolbar
============================

Add a Profile panel to the Django Debug Tool. Disabled by default, requires
a querystring paramater to enable.

This is mainly a re-packaging of dmishe's commits from here:
https://github.com/dmishe/django-debug-toolbar

To Install
-------

* Install and configure Django Debug Toolbar.
* pip install django-profile-panel
* Add panel_panel app to your INSTALLED_APPS.
* Add profile_panel.panel.ProfileDebugPanel to DEBUG_TOOLBAR_PANELS.
* Make any request with ?profile


