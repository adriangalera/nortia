# nortia
Time tracking software to be run in a Raspberry Pi and use buttons as input.

The name comes from https://en.wikipedia.org/wiki/Nortia

How to run it:

```bash
PYTHONPATH=. python3 nortia/main.py /tmp/test.csv
```
To edit the file, use https://filebrowser.org/installation:

```bash
filebrowser -a 0.0.0.0 -r nortia/
```
