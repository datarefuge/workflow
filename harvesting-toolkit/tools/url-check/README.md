# Check whether a URL has already been archived by the Internet Archive

The python script in this directory takes a list of UR's as pinput (one per line) and checks against the Internet Archive's API to see if the page has already been archived. 

An optional second argument will write a list of **unarchived** URL's to a file.

An optional third argument will write a list of **archived** URL's, with the archiving timestamp prepended in the form `timestam, url` (one per line). If the archive date is more than say 3 months old it is probably still worth archiving again, for completeness.

If you can incorporate this check into your workflow, it's probably worth doing, as we are finding a lot of our goal uRL''s have already been archived (yay!). 

## Example

```sh
python3 ./checkia.py urls.txt unarchived.txt archived.csv
```

