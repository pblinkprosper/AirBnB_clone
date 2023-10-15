#!/usr/bin/python3
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
    output = f.getvalue()
