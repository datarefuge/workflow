check-ia
========

`check-ia` check if given URLs have been archived in the [Internet Archive](https://archive.org).  It uses the Wayback Machine's [network API](https://archive.org/help/wayback_api.php) to perform the checks.

----
*Author*:       [Michael Hucka](http://www.cds.caltech.edu/~mhucka)

*Repository*:   [https://github.com/mhucka/rsmirror](https://github.com/mhucka/rsmirror)


Usage
-----

`check-ia` can take a file containing a list of URLs, or it can check URLs given as arguments on the command line.  The simplest usage is

```csh
check-ia URL 
```

Alternatively, it can take any of several command line arguments:

```csh
check-ia [-h] [-f file] [-o file] [-m file] [-q]
```

* `-h` or `--help`: print a help message
* `-f` or `--file`: an input file from which to read URLs to check
* `-o` or `--okay`: an output file where to write URLs that are found to exist in the Internet Archive's Wayback Machine
* `-m` or `--miss`: an output file where to write URLs that are found missing from  the Internet Archive's Wayback Machine
* `-q` or `--quiet`: make the program run more quietly.

The file format for the output file for *found* URLs (i.e., the file written by the argument `-o`) is a comma-separated value file with two columns: a timestamp and a URL:

```
timestamp,URL
```

The file format for the output of *missing* URLs is simply a list of URLs, one per line, since no sensible default timestamp value can be assigned in those cases.


Additional comments relevant to data rescue efforts
---------------------------------------------------

If the archive date for a given URL is more than, say, 3 months old, it is probably still worth archiving again, for completeness.

If you can incorporate this check into your workflow, it's probably worth doing, as we are finding a lot of our goal URL's have already been archived (yay!).
