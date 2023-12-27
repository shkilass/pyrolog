.. _index:

.. rst-class:: center

    .. image:: banner.png


.. code-block:: python

    import pyrolog

    logger = pyrolog.Logger(
        name='Example',
        handlers=[
            pyrolog.StdoutHandler(
                log_level='info',
                formatter=pyrolog.ColoredFormatter()
            )
        ]
    )


.. admonition:: About the **Pyrolog**
    :class: important

    **Pyrolog** - is a modern, simple in use and fast logging library.
    It helps you to log any event in your projects and easily detect the bugs.

    Key features
    ------------

    * **Fast:** Developed specially without heavy algorithms but saving its power.
    * **Easy:** Library is simple and intuitive. Install library and start use it right away.
    * **Powerful:** Many features that helps you to do elegant logging ecosystem in your projects.
    * **Type-hinted:** All classes, methods are type-hinted, that helps you in development.

Installing
----------

.. code-block:: shell

    $ pip install pyrolog


.. toctree::
    :hidden:
    :caption: Quick Guide

    quickguide/firststeps
    quickguide/parent_groups

.. toctree::
    :hidden:
    :caption: Features reference

    features/example

.. toctree::
    :hidden:
    :caption: Reference

    reference/pyrolog_module
