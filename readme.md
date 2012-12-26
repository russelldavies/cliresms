cliresms
======
cliresms - A python script to send webtexts from the command line for Irish carriers.

Description
-----------
This is Python clone (sort of) of [o2sms](http://o2sms.sourceforge.net)

What's wrong with o2sms? Nothing really, it's great and kudos to Mackers for writing it. But being written in Perl and requiring a few esoteric Perl modules makes portability a problem (for me, at least). Since Python is installed wherever I go I thought I'd make my own portable version in Python.

Like o2sms, it's command line driven and requires you have a valid webtext account with an Irish mobile provider. As I'm used to o2sms, it has similar command line parameters and uses the same configuration file format (with the addition of a `carrier` statement).

Meteor, Three, and O2 are currently supported. Help add more.

Requires Python >= 2.6 and works on Python 3. For Python versions < 2.7, the argparse module is required. No extra modules are necessary to be as portable as possible.

Synopsis
--------
    cliresms [options] <number|alias|group> [<number|alias|group> ...]

The message will be read from standard input; either pipe some text or type
the message, ending with CTRL-d or the '.' character on a line by itself
(just like most unix tools).

Options
-------
    -u --username=STRING
    	Use this username (defaults to unix username)
    
    -p, --password=STRING
    	Use this password (if omitted, will prompt for password)
    
    -c, --config-file=FILE
    	Use this configuration file (defaults to ~/.cliresms.conf)
    
    -s, --split-messages
    	Allow message to be split into multiple SMSs (the default)
    
    -C, --carrier=NAME
    	Force the carrier to be this (``meteor'', ``o2'',``vodafone'', ``three'', ``emobile'', or ``tesco'')
    
    -m, --message=STRING
    	Don't wait for STDIN, send this message
    
    -h, --help
    	Prints this help message and exits
    
    --version
    	Print version and exit

Configuration File
------------------
Configuration is in the file *~/.cliresms.conf* or can be overwritten with the `-c` / `--config-file` command line option.

Values in this file are stored as one per line and take the same name and format as their command line equivalents.

The one exception to this is the `alias` setting, which defines a named alias for one number (a straight alias) or more than one number (a group).

Configuration file example:

    username russell
    password horsebattery
    carrier meteor
    nosplit
    alias sean 0865551234
    alias beerpeople +353865550000 +353865550001 +353865550002
    # a comment

Author
------
Russell Davies \<russell@zeroflux.net\>

Acknowledgements
----------------
Thanks to David McNamara \<me.at.mackers.dot.com\> for o2sms.

Copyright
---------
Copyright 2012 Russell Davies

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
