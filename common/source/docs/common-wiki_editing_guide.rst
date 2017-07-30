.. _common-editor-information-resource:
.. _common_wiki_editing_guide:

==================
Wiki Editing Guide
==================

All members of the community are welcome to join and contribute to this
wiki! Any help you can offer is appreciated — from creating new articles
and re-validating older articles, through to fixing broken links and
spelling/grammatical errors.

We've made that very easy - all you need for access is a 
`Github account <https://github.com/join>`__. 

This provides everything you need to help the wiki grow!


Making a quick edit
===================

Once you've got your `Github account <https://github.com/join>`__ you can edit
project source pages directly on Github. 

For small changes (e.g. fixing typographic errors) just click the **Edit on GitHub**
link at the top of the wiki page to be taken to it's source. 

Then select the **Edit** icon and follow Github's simple prompts to fork the repository, make
the changes, and open a pull request. 

.. figure:: ../../../images/github_edit_icon.jpg

    Select the **Edit** icon to start making your changes. 

For more information see the Github Help topic: 
`Editing files in another user's repository <https://help.github.com/articles/editing-files-in-another-user-s-repository/>`__

.. note::

    Wiki home pages (named "index.html") do not have the **Edit on GitHub** link. You can still edit them
    by manually navigating to the desired page on Github.

.. _common_wiki_editing_guide_big_edit:

Making a big edit
=================

  
Creating a new wiki page
========================


How to get changes approved
===========================


Building/testing docs locally
=============================


RST rendering on Windows
------------------------

A combination of two Windows tools can help you previewing your modifications:
  	
* `Notepad++ plugin for RST files <https://github.com/steenhulthin/reStructuredText_NPP>`__
* `restview (on-the-fly renderer for RST files) <https://mg.pov.lt/restview/>`__

The Notepad++ plugin helps you with code completion and syntax highlighting during modification.
Restview renders RST files on-the-fly, i.e. each modification on the RST file can be immediately
visualized in your web browser. 

The installation of the Notepad++ plugin is clearly explained on the plugin's website (see above).

Restview can be installed with:

.. code-block:: bat
	
	python -m pip install restview
		
The restview executable will be installed in the **Scripts** folder of the Python main folder.
Restview will start the on-the-fly HTML rendering and open a tab page in your preferred web browser.

Example:

If you are in the root folder of your local Wiki repository:

.. code-block:: bat
	
	start \python-folder\Scripts\restview common\source\docs\common-wiki_editing_guide.rst	
	
RST rendering on Linux
----------------------

`ReText <https://github.com/retext-project/retext>`__ is a Linux tool that provides
syntax highlighting and basic on-the-fly rendering in a single application.

.. note:: 

    Although the tool is Python based, don't try it on Windows as it very prone to crashes (this is 
    also stated by the website).

Wiki Infrastructure
===================


Working with common pages
=========================

General Editing/Style Guide
===========================

This section explains some specific parts of syntax used by the wiki along with general
style guidelines to promote. consistency of appearance and
maintainability of wiki content. The general rule is to keep things
simple, using as little styling as possible.

For more information check out the 
`Sphinx reStructured Text Primer <http://www.sphinx-doc.org/en/stable/rest.html>`__.



Titles
------

Choose a concise and specific title. It should be informative enough that a reader can determine
if the content is likely to be relevant and yet differentiate it from other (similar) topics.

Use first-letter capitalization for all words in the title (except connecting words: "and","the", "with" etc.)

The title syntax is as shown below. Note that we use an "anchor reference" immediately before the title (and named 
using the page filename). This allows us to link to the file from other wikis and from documents even if 
they move within the file structure.

.. code-block:: rst

    .. _your_file_name:

    ==========
    Page Title
    ==========
    

Abstract
--------

Start the topic (after the title) with an abstract rather than a heading or an image.

Ideally this should be a single sentence or short paragraph describing the content and scope of the topic.


Headings
--------

Headings are created by (fully) underlining the heading text with a single character. 
We use the following levels:

.. code-block:: rst

    Heading 1
    =========
    
    Heading 2
    ---------
    
    Heading 3
    +++++++++
    
    Heading 4
    ^^^^^^^^^
    
    Heading 5
    ~~~~~~~~~



Emphasis
--------

Emphasis should be used *sparingly*. A page with too much bold
or italic is hard to read, and the effect of emphasis as a tool
for identifying important information is reduced.

Use emphasis to mark up *types* of information:

- ``code`` for code and variables
- **bold** for "button to press" and filenames
- *italic* for names of dialogs and tools.

The markup for each case is listed below.

.. code-block:: rst

    ``Inline code``
    **Bold**
    *Italic*

Lists
-----

Numbered lists can be generated by starting a line with ``#.`` followed by a space. 
Unordered lists can be generated by starting a line with "*" or "-". Nested lists
are created using further indentation:

.. code-block:: rst

    #Ordered listed
    
    #. Item one
    #. Item 2
       Multiline
    #. Item 3
       
       - Nested item
       #. Nested item ordered

    #Unordered list
    
    - Item 1
    - Item 2
    
      - Nested item


Information notes and warnings
------------------------------

You can add notes, tips and warnings in the text using the "tip", "note"
and "warning" shortcodes, respectively. These render the text in an
information box:

.. code-block:: rst

    .. note::

       This is a note

.. note::

   This is a note



.. code-block:: rst

    .. tip::

       This is a tip
   
   
.. tip::

   This is a tip
   
   
.. code-block:: rst

    .. warning::

       This is a warning

.. warning::

   This is a warning

   
Code
====

Use the "code-block" directive to declare code blocks. You can specify the type of code too and it will be 
syntax marked:

.. code-block:: rst

    .. code-block:: python
    
        This is format for a code block (in python)
    
        Some code

Alternatively you can just have a double colon "::" at the end of a line, a blank line,
and then indent the code block text:

.. code-block:: rst

    This is format for a code block. ::
    
        Some code



.. _common-editor-information-resource_how_to_link_to_other_topics:

Internal links
--------------


External links
--------------

To link to off-wiki topics, use the following format:

.. code-block:: rst

    `Link text <http://the-target-link-url>`__

This same format can be used for internal links, but without the benefit of being able to track when
internal links are broken by title changes etc.
 

How to put the page into the sidebar menu
-----------------------------------------


How to put links in the top menu
--------------------------------

Using images in your wiki pages
-------------------------------


Archiving topics
================


Deleting wiki pages
===================

Wiki pages can be deleted by removing them from git and any menu in which they appear.

.. warning::

    Before deleting a wiki page it is important to ensure that it is not the 
    parent of other menu items (e.g. it does not contain a "toctree")
    

Legal information
=================

All content on this wiki is licensed under the terms of the `Creative Commons Attribution-ShareAlike 3.0 Unported <http://creativecommons.org/licenses/by-sa/3.0/>`__.

.. warning::

   Only post content that you have the legal right to make
   available under the `CC BY-SA 3.0 <http://creativecommons.org/licenses/by-sa/3.0/>`__ license. If you
   do use images or content that belongs to others, seek permission for
   re-use and clearly state their origin and terms for re-use.
   


Translating wiki pages
======================

Translation is currently not supported.


FAQ
===

Why are my changes not published?
---------------------------------

The wiki is moderated to help reduce the chance of misleading or
incorrect information being posted. All articles and changes are
reviewed before they are published.


[copywiki destination="urus"]
