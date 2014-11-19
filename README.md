pyside-example
==============

Example on how to use PySide to create a Python GUI.

Dependencies
------------

You need to install PySide. The best way is with pip. For bonus points, use a virtualenv too.

(optional)
```sh
virtualenv fruit-example
. fruit-example/bin/activate
```

```sh
pip install PySide
```

If you are on OSX you will need to install Qt first.

```sh
brew install qt
```


Generate fruit_ui.py
--------------------

Run `pyside-uic` to convert the XML form designer file generated by QtCreator into a python PySide compatible class.

```sh
pyside-uic fruit.ui -o fruit_ui.py
```


Running the application
-----------------------

```sh
python fruit.py
```