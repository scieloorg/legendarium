===============================
legendarium
===============================


.. image:: https://img.shields.io/pypi/v/legendarium.svg
        :target: https://pypi.python.org/pypi/legendarium

.. image:: https://img.shields.io/travis/jamilatta/legendarium.svg
        :target: https://travis-ci.org/jamilatta/legendarium

.. image:: https://readthedocs.org/projects/legendarium/badge/?version=latest
        :target: https://legendarium.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jamilatta/legendarium/shield.svg
     :target: https://pyup.io/repos/github/jamilatta/legendarium/
     :alt: Updates


Python library to handle SciELO`s bibliographic legend


* Free software: BSD license
* Documentation: https://legendarium.readthedocs.io.



Develop API Usage
---------

<pre>
<code>
>>>from legendarium import Legendarium
>>>leg_dict = {'acron_title': 'Rev.Mal-Estar Subj', 'year_pub': '2011', 'volume': '67', 'number': '9', 'fpage': '154', 'lpage':'200', 'article_id':'e00120416'}
>>>leg = Legendarium(**leg_dict)
>>>leg.stamp
>>>Rev.Mal-Estar Subj 2011;67(9):154-200
</code>
</pre>


For develop version
====================

-e git+git@github.com:scieloorg/legendarium#egg=legendarium


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

