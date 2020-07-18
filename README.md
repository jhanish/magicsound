magicsound
=========
*Cross platform, single function module with no dependencies for playing sounds.*

Installation
------------
Install via pip:

    $ pip install magicsound

Done.

If you want to just work from the source,
just copy the magicsound.py file into the same folder as your project,
or into a library path.

The latest version of the source code can be found at:
https://github.com/jhanish/magicsound

Quick Start
-----------
Once you've installed, you can really quickly verify that it works with just this:

    >>> from magicsound import magicsound
    >>> magicsound('/path/to/a/sound/file/you/want/to/play.wav') 

Documentation
-------------
The magicsound module contains only one thing - the function (also named) magicsound.

It requires one argument - the path to the file with the sound you'd like to play. This may be a local file, or a URL.

There's an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously when possible, which is not always at this point.

On Windows, uses windll.winmm. WAVE and MP3 have been tested and are known to work. Other file formats may work as well.

On MacOS, we use the command line utility afplay so nothing else needs to be installed.

On Raspberry Pi, we use ffplay command line utility for the same reason.

On Linux, uses GStreamer. Known to work on Ubuntu 14.04 and ElementaryOS
Loki. Support for the ``block`` argument is currently not implemented.

Requirements
------------
Tested on Windows 10, MacOS 10.15.6 (Catalina), and Raspian on a 4 gig PI 4.
I've only tested with Python 3.8 on all 3 platforms.
The code is all simple enough that it's application should be able with a broad set
of software versions, but let me know, I'd like to fix any found problems
on modern systems, and add others as possible.  
If you need older systems to work, please check out
the playsound project that this project was forked from.

https://github.com/TaylorSMarks/playsound

Copyright
---------
This software is Copyright (c) 2020 Joe Hanish <joe.hanish@gmail.com>.

This is a derivitive work from Taylor Marks playsound library that you can find
here: https://github.com/TaylorSMarks/playsound. 

If you are using Python older than 3.6, I recommend you use his library.  Magicsound was made just to fix some problems on newer systems, eradicate the install requirement for OSX, and detect and work with Raspberry Pi directly.  This project is MIT licensed as is his. 

Taylor's original source copyright:
This software is Copyright (c) 2016 Taylor Marks <taylor@marksfam.com>.

See the bundled LICENSE file for more information.
