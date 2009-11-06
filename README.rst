Django Lingo
======

`Lingo`_ is a reusable django app which provides extensible, pure-python fulltext indexing for Django models using the `Lingo`_ information-retrieval library. 

The django-lingo project lives at http://github.com/ryates/django-lingo/.

.. _Lingo: http://github.com/ryates/django-lingo/


What is Lingo?
-------------
Django-lingo is a simple Django app that allows you to customize the labels of ModelForm-based forms.  The initial version ties customizations to the contrib.auth User objects, but future revisions will support allowing developers implementing Lingo to provide customizations based on whatever seems appropriate (e.g. Sites, Business Unit, etc.).  

Lingo is not strings localization.  Strings localization is typically locale-based and relies on translations that are built once and generally don't change.  Lingo is designed for having a single model that needs to display labels differently based on varying terms or lingo used.

This app was created based on system that we built where clients wanted the ability to change the fields to represent terminology that they use in their own business.  

Usage
-----
For now, see the tests for details on how to use it.  

License
-------
Lingo is yours to use, modify, and redistribute according to the terms of the BSD license, the full text of which is in a file named ``LICENSE.txt``, which should be in the same directory as this readme.

Contributors
------------
* Rob Yates <rob AT robyates.org>

