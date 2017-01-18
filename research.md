# RESEARCH 

First pick a url/dataset to evaluage. 

**Claim/check out your link so there are no
duplicate researching efforts.**

Keep in mind two things when looking at the spreadsheet: 



### Is the data actually actually crawlable?

Again, see [here](https://docs.google.com/document/d/1PeWefW2toThs-Pbw0CMv2us7wxQI0gRrP1LGuwMp_UQ/edit)
and
[here](https://docs.google.com/document/d/1qpuNCmBmu4KcsS_hE2srewcCiP4f9P5cCyDfHmsSAVU/edit)
for a mostly non-techincal introduction to the crawler. Some additional
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
  - Fill out that you seeded 
  - Fill out that link is done 
- NO: If it is confirmed not crawlable:
  - Search agency websites and data.gov for dataset entry points for your dataset collection   
  - Add harvastable data url to spreadsheet (Column ), REALLY IMPORTANT! 
  - Learn what actual datasets look like in terms of format  (SQL, FTP, ZIP, PDF Collections, etc.), size,  what you found, etc. (Column )
- YES AND NO: for example, FTP address, mixed content, big data sets:
  - Nominate it anyway, but folow the steps for uncrawlable content above.
  - *While we understand that this may mean duplicate sets of data in the ckan, that is not a concern. We are ensuring that the data is fully preserved and accessible.*

Try to understand what data sets are underlying the web pages. Look for related
entries in the spreadsheet, and ensure that you aren't harvesting a subdirectory
if you can harvest the entire directory. Often, data underlying dozens of pages
or multiple "access portal" apps is also available as one structured data file.
