## What do Researchers do?

Researchers review "uncrawlables" identified during [Seeding](seednsort.md), confirm the URL/dataset is indeed uncrawlable, and investigate how the dataset could be best harvested. Researchers need to have a good understanding of harvesting goals and have some familiarity with datasets.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you have a strong front end web experience and enjoy research. An understanding how federal data is organized (e.g. where "master" datasets are) would be valuable.
</div>



## Getting set up as a Researcher

- Event organizers (in-person or remote) will tell you how to volunteer for the Researcher role, either through slack or a form.
    - As a result, they will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
    - Click the invite link, and choose a user name and a password.
- Make sure you have an account on the DataRefuge slack (or other slack team recommended by your event organizers) This is where people share expertise and answer each other's questions.
    - Ask your event organizer to send you an invite
- If you need any assistance:
    - Talk to your DataRescue Guide if you are at an in-person event
    - Or post questions on Slack in the `#general` channel (or other channel recommended by your event organizers).

## Researchers and Harvesters

- Researchers and Harvesters should work very closely together as their work will feed from each other and much communication is needed between the two roles.
- For instance they could work in pairs or in small groups.
    - In some cases, a single person might be both a Researcher and a Harvester.
- As a Researcher, make sure to check out the [Harvesters documentation](harvesting.md) to familiarize yourself with their role.

## Claiming a dataset to Research

- Researchers work on datasets that were listed as uncrawlable by Seeders.
- Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `RESEARCH`: all the URLs listed are ready to be researched
    - Available URLs are the ones that have not been checked out by someone else, that is, that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Check out this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
- While you go through the research process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

## Note: URL vs UUID

The `URL` is the link to examine and harvest, and the `UUID` is a canonical ID we use to connect the url with the data in question. The UUID will have been generated earlier earlier in the process. UUID stands for Universal Unique Identifier.

## Evaluating the data

Go to the URL, and start inspecting the content.

## Is the data actually crawlable?

Again, see [here](https://docs.google.com/document/d/1PeWefW2toThs-Pbw0CMv2us7wxQI0gRrP1LGuwMp_UQ/edit)
and [here](https://docs.google.com/document/d/1qpuNCmBmu4KcsS_hE2srewcCiP4f9P5cCyDfHmsSAVU/edit)
for a mostly non-technical introduction to the crawler. Some additional
technical notes for answering this:

- There is no specific file size cutoff on what is crawlable, but large files should be manually captured anyway.
- Files types like ZIP, PDF, Excel, etc. are crawlable if they are linked.
- The crawler can only follow HTTP links that appear directly in the DOM at load time. (That is, they should appear as `<a href ...>` tags in the page source.)
If links are added by Javascript or require submitting a form, they are not crawlable.
- The crawler does not tolerate web frames (but it straightforward to inspect a page to obtain the content in the frame directly, and then nominate *that*).
- The crawler recently added the ability to crawl FTP, but we will not rely on this; we will treat resources served over FTP as uncrawlable.

What to do in each case:

### YES

If the URL is crawlable or you locate a crawlable URL that accesses the underlying dataset:

- Nominate it: use our
  [Chrome extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok),
  and if that doesn't work then use the
  [bookmarklet](http://digital2.library.unt.edu/nomination/eth2016/about/)
- Click checkbox `Do not harvest` in Archivers app.
<!-- why don't we ask that any more?  - Fill out cell "Seeded?" = "yes" and tell what URL you seeded. -->

### NO

If it is confirmed not crawlable:
<!-- Why don't we ask that any more? - Fill out the cell "Can it be crawled?" = "no" in Researcher section of the spreadsheet-->

- Search agency websites and data.gov for dataset entry points for your dataset collection  
    - Tips: Try to understand what data sets are underlying the web pages. Look for related entries in the Archivers app, and ensure that you aren't harvesting a subdirectory if you can harvest the entire directory. Often, data underlying dozens of pages or multiple "access portal" apps is also available as one structured data file.
    - Make note of any better entry point in the `Recommended Approach`field, along with any other recommendations on how to proceed with this harvest.
<!-- - Add your suggested url for harvesting the data to spreadsheet (in cell "Harvestable Data"), REALLY IMPORTANT!-->
- Add other information that could help the Harvester, such as the format (SQL, FTP, ZIP, PDF Collections, etc.), approximate size, details about what you found, etc.
- Search for related URLS that might already have been listed in the Archivers app that might be covered by the same approach, so as not to duplicate work. You can search for them in the `Link URL` field.

### YES AND NO

For example, FTP address, mixed content, big data sets:
<!--  - Fill out the cell "Can it be crawled?" = "yes & no" in Researcher section of the spreadsheet-->

- Nominate it anyway, but also follow the steps for uncrawlable content above.
- *While we understand that this may result in some dataset duplication, that is not a concern. We are ensuring that the data is fully preserved and accessible.*

## Finishing Up

- In the Archivers app, make sure to fill out as much information as possible to document your work.
- Check the Research checkbox (on the right-hand side) to mark that step as completed.
- Click `Save`.
- Click `Check in URL`, to release it and allow someone else to work on the next step.
- You're done! Move on to the next URL!

<!-- HOW DOES THIS PROCESS WORK NOW:    - If ever a day or more passed  since you originally claimed the item, update the date to today's date.
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, the **Date field will turn red**, signaling that someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.-->
