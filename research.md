# RESEARCH 

## Claiming a dataset to harvest

- You will work on datasets that were listed as uncrawlable by Seeders.
- Go to the Uncrawlable spreadsheet, and look for a dataset whose cell "Researcher status indicator" is empty. This means that no one is working on this dataset yet. Claim it by entering your slack handle with the status "Open" and today's date in the cell "Researcher status indicator" in Researcher section, for instance:
```
@khdelphine open 1/22/2017
```
- You will find the URL you are about to evaluate in the "Original URL" cell.


## Evaluating the data
Go to the URL, and start inspecting the content. 

## Is the data actually actually crawlable?

Again, see [here](https://docs.google.com/document/d/1PeWefW2toThs-Pbw0CMv2us7wxQI0gRrP1LGuwMp_UQ/edit)
and
[here](https://docs.google.com/document/d/1qpuNCmBmu4KcsS_hE2srewcCiP4f9P5cCyDfHmsSAVU/edit)
for a mostly non-technical introduction to the crawler. Some additional
technical notes for answering this:

- There is no specific file size cutoff on what is crawlable, but large files
  should be manually captured anyway.
- Files types like ZIP, PDF, Excel, etc. are crawlable if they are linked.
- The crawler can only follow HTTP links that appear directly in the DOM at load
  time. (That is, they should appear as `<a href ...>` tags in the page source.)
  If links are added by Javascript or require submitting a form, they are
  not crawlable.
- The crawler does not tolerate web frames (but it straightforward to inspect
  a page to obtain the content in the frame directly, and then nominate *that*).
- The crawler recently added the ability to crawl FTP, but we will not rely on
  this; we will treat resources served over FTP as uncrawlable.

What to do in each case:

- YES: If the URL is crawlable or you locate a crawlable URL that accesses the
  underlying dataset:
  - Nominate it: use our
    [Chrome extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok),
    and if that doesn't work then use the
    [bookmarklet](http://digital2.library.unt.edu/nomination/eth2016/about/)
  - Fill out the cell "Can it be crawled?" = "yes" in Researcher section of the spreadsheet
  - Fill out that you seeded (Cell "Seeded?" in Researcher section of the spreadsheet)
  - Fill out that link is done (Cell "Done" at the very end of the spreadsheet)
- NO: If it is confirmed not crawlable:
   - Fill out the cell "Can it be crawled?" = "no" in  Researcher section of the spreadsheet
  - Search agency websites and data.gov for dataset entry points for your dataset collection   
  - Add harvastable data url to spreadsheet (Column ), REALLY IMPORTANT! 
  - Learn what actual datasets look like in terms of format  (SQL, FTP, ZIP, PDF Collections, etc.), size,  what you found, etc. (Column )
- YES AND NO: for example, FTP address, mixed content, big data sets:
   - Fill out the cell "Can it be crawled?" = "yes & no" in Researcher section of the spreadsheet
  - Nominate it anyway, but follow the steps for uncrawlable content below.
  - *While we understand that this may mean duplicate sets of data in the ckan, that is not a concern. We are ensuring that the data is fully preserved and accessible.*

If you have found harvestable data then:

Try to understand what data sets are underlying the web pages. Look for related
entries in the spreadsheet, and ensure that you aren't harvesting a subdirectory
if you can harvest the entire directory. Often, data underlying dozens of pages
or multiple "access portal" apps is also available as one structured data file.

Add your suggested url for harvesting the data in the "Harvestable data" cell in the Researcher section of the spreadsheet. 
Also add other information in the spreadsheet that could help the Harvester, such as information about format (SQL, FTP, ZIP, PDF Collections, etc.), size, details about what you found, recommended approach, etc. 

Search for related URLS in the pipeline that might would be covered by the same approach so as not to duplicate work.

## Finishing up
- In the Uncrawlable spreadsheet, briefly describe the method used for harvesting in cell "Method Used" in Harvester section
- In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Researcher status indicator", for instance: 

  ```
  @khdelphine closed 1/22/2017
  ```
  - If ever a day or more passed since you originally claimed the item, update the date to today's date. 
  - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, someone else can claim it in your place and start working on it
    - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
- You're done! Move on to the next URL!


