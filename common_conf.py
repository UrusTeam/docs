# -*- coding: utf-8 -*-
#
# This contains common configuration information for the urus wikis. 
# This information is imported by the conf.py files in each of the sub wikis
#

#Set False to re-enable warnings for non-local images.
disable_non_local_image_warnings=True


wiki_base_url='https://urusteam.github.io/docs/'
intersphinx_base_url=wiki_base_url+'%s/'


# Where to point the base of the build for the main site menu
html_context= {'target':'/'}
# This needs to change to the actual URL root once the theme updated.

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
                       'urus': (intersphinx_base_url % 'urus',
                                  None),
                       'urussystem': (intersphinx_base_url % 'urussystem',
                                  None),
                       'protocol': (intersphinx_base_url % 'protocol',
                                  None),
                       'urusstudio': (intersphinx_base_url % 'urusstudio',
                                  None),
                       'hardware': (intersphinx_base_url % 'hardware',
                                  None),
                       'software': (intersphinx_base_url % 'software',
                                  None),
                       'kernel': (intersphinx_base_url % 'kernel',
                                  None),
                       'developer': (intersphinx_base_url % 'developer',
                                  None),
                                  }

############ PATCH REMOVE NON-LOCAL IMAGE WARNINGS
### From:
##  http://stackoverflow.com/questions/12772927/specifying-an-online-image-in-sphinx-restructuredtext-format
##  And https://github.com/sphinx-doc/sphinx/issues/2429

#Set False to re-enable warnings for non-local images.
disable_non_local_image_warnings=True

if disable_non_local_image_warnings:
    import sphinx.environment
    from docutils.utils import get_source_line

    def _warn_node(self, msg, node, **kwargs):
        if not msg.startswith('nonlocal image URI found:'):
            self._warnfunc(msg, '%s:%s' % get_source_line(node),**kwargs)

    sphinx.environment.BuildEnvironment.warn_node = _warn_node
############ ENDPATH