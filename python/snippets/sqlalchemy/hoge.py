#!/Users/tell_k/.virtualenvs/sphinx/bin/python

# $Id: rst2html.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_string, default_description, publish_parts


description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

#{'attribution': 'dash', 'footnote_backlinks': 1, 'record_dependencies':
#        DependencyList(None, []), 'rfc_base_url': 'http:
#        //www.faqs.org/rfcs/', 'traceback': None, 'pep_references': None,
#        //'strip_comments': None, 'toc_backlinks': 'entry', 'lan
#        guage_code': 'en', 'datestamp': None, 'report_level': 2, 'table_style':
#        '', 'pep_base_url': 'http://www.python.org/dev/p
#        eps/', '_destination': None, 'halt_level': 4, 'strip_classes': None,
#        'compact_field_lists': 1, 'error_encoding_error_han
#        dler': 'backslashreplace', 'debug': None, 'embed_stylesheet': 1,
#        'output_encoding_error_handler': 'xmlcharrefreplace', '
#        stylesheet_path':
#        '/Users/tell_k/.virtualenvs/sphinx/lib/python2.7/site-packages/docutils/writers/html4css1/html4css1.cs
#        s', 'sectnum_xform': 1, 'dump_transforms': None, 'stylesheet': None,
#        'docinfo_xform': 1, 'warning_stream': None, 'field_
#        name_limit': 14, 'initial_header_level': '1', 'exit_status_level': 5,
#        'config': None, 'rfc_references': None, 'cloak_ema
#        il_addresses': None, 'trim_footnote_reference_space': None,
#        'compact_lists': 1, 'pep_file_url_template': 'pep-%04d', 'du
#        mp_pseudo_xml': None, 'expose_internals': None, 'sectsubtitle_xform': 0,
#        'source_link': None, 'strict_visitor': None, 'o
#        utput_encoding': 'utf-8', 'template':
#        '../../../../../.virtualenvs/sphinx/lib/python2.7/site-packages/docutils/writers/h
#        tml4css1/template.txt', 'source_url': None, 'input_encoding': None,
#        '_disable_config': None, 'id_prefix': '', 'option_li
#        mit': 14, 'xml_declaration': 1, 'tab_width': 8, 'error_encoding':
#        'UTF-8', '_source': u'hoge.rst', 'raw_enabled': 1, 'ge
#        nerator': None, 'dump_internals': None, 'title': None,
#        'footnote_references': 'brackets', 'input_encoding_error_handler'
#        : 'strict', 'auto_id_prefix': 'id', 'doctitle_xform': 1,
#        'strip_elements_with_classes': None, '_config_files': [], 'file
#        _insertion_enabled': 1, 'math_output': 'MathML', 'dump_settings': None}

#template
#stylesheet_path
#warning_stream
#settings_overrides={'warning_stream': '/dev/null'}

f = open('hoge.rst')
hoge = f.read()
f.close()
print publish_parts(source=hoge, writer_name='html', settings_overrides={'warning_stream': '/dev/null'})['body']
