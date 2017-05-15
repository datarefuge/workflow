## What Do Researchers Do?

Researchers review "uncrawlables" identified during [Seeding](seeding.md), confirm the URL/dataset is indeed uncrawlable, and investigate how the dataset could be best harvested. Researchers need to have a good understanding of harvesting goals and have some familiarity with datasets.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you have strong front-end web experience and enjoy research. An understanding of how federal data is organized (e.g. where "master" datasets are) would be valuable.
</div>

## Getting Set up as a Researcher

-   Event organizers (in-person or remote) will tell you how to volunteer for the Researcher role, either through Slack or a form.
    -   They will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
    -   Click the invite link, and choose a username and a password. It is helpful to use the same username on the app and Slack.
-   Create an account on the DataRefuge Slack using this [slack-in](https://rauchg-slackin-qonsfhhvxs.now.sh/) or use the Slack team recommended by your event organizers. This is where people share expertise and answer each other's questions.
-   If you need any assistance:
    -   Talk to your DataRescue guide if you are at an in-person event
    -   Or post questions in the DataRefuge Slack `#researchers` channel (or other channel recommended by your event organizers).

<div class = "note">
  <strong>Researchers and Harvesters</strong> <br />  
  <ul>
    <li>Researchers and Harvesters should coordinate together as their work is closely related and benefits from close communication</li>
    <li>It may be most effective to work together in pairs or small groups, or for a single person to both research and harvest</li>
    <li>As a Researcher, make sure to check out the <a href="/harvesting/">Harvesting documentation</a> to familiarize yourself with their role</li>
  </ul>
</div>

## Claiming a Dataset to Research

<div class = "note">
  <strong>Using Archivers App</strong> <br />  
  Review our walkthrough video below and refer to the <a href="/faq/">FAQ</a> for any additional questions about the <a href="http://www.archivers.space" target="_blank">Archivers app</a><!--_-->. <br />
  &nbsp;<br />
  <p style="text-align:center"><iframe width="80%" height="315" src="https://www.youtube.com/embed/tvSSILnHnpA" frameborder="0" allowfullscreen></iframe></p>
</div>

-   Researchers work on datasets that were listed as uncrawlable by Seeders.
-   Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `RESEARCH`: all the URLs listed are ready to be researched.
    -   Available URLs are ones that have not been checked out by someone else, i.e. that do not have someone's name in the User column.
    -   Priority is indicated by the “!” field.  The range is from 0 to 10, with 10 being highest priority.
-   Select an available URL (you may decide to select a URL relevant to your area of expertise or assigned a high priority) and click its UUID to get to the detailed view, then click `Checkout this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
-   While you go through the research process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

<div class = "note">
  <strong>URL vs UUID</strong> <br />  
  The <code>URL</code> is the link to examine and harvest, and the <code>UUID</code> is a canonical ID we use to connect the URL with the data in question. The UUID will have been generated earlier in the process. UUID stands for Universal Unique Identifier.
</div>

## Evaluating the Data

Go to the URL and start inspecting the content.

### Is the data actually crawlable?

Again, see [EDGI's Guides](https://edgi-govdata-archiving.github.io/guides/) for a mostly non-technical introduction to the crawler:

-   [Understanding the Internet Archive Web Crawler](https://edgi-govdata-archiving.github.io/guides/internet-archive-crawler/)
-   [Seeding the Internet Archive’s Web Crawler](https://edgi-govdata-archiving.github.io/guides/seeding-internet-archive/)
-   A written guide on using the Chrome Nomination tool, the EDGI Primer Database, and a video tutorial are available [in Seeders' Documentation](seeding/#crawlable-urls)

Some additional technical notes for answering this:

-   There is no specific file size cutoff for what is crawlable, but large files should be manually captured anyway.
-   File types like ZIP, PDF, Excel, etc. are crawlable if they are linked, but it may be useful to archive them if they represent a meaningful dataset, or if there are many of them on a page.
-   The crawler can only follow HTTP links that appear directly in the DOM at load time. (That is, they should appear as `<a href ...>` tags in the page source.)
If links are added by JavaScript or require submitting a form, they are not crawlable.
-   The crawler does not tolerate web frames (but it is straightforward to inspect a page to obtain the content in the frame directly, and then nominate *that*).
-   The crawler recently added the ability to crawl FTP, but we will not rely on this; we will treat resources served over FTP as uncrawlable.

#### YES

If the URL is crawlable or you locate a crawlable URL that accesses the underlying dataset:

-   Nominate it using the [EDGI Nomination Chrome Extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok).
-   Click the `Do not harvest` checkbox in the Research section in the Archivers app.
-   Click `Checkin this URL` and move on to another URL.

#### NO

If it is confirmed not crawlable:

-   Search agency websites and data.gov for dataset entry points for your dataset collection.
    -   Tips: Try to understand what datasets are underlying the web pages. Look for related entries in the Archivers app, and ensure that you aren't harvesting a subdirectory if you can harvest the entire directory. Often, data underlying dozens of pages or multiple "access portal" apps is also available as one structured data file.
    -   Make note of any better entry point in the `Recommended Approach for Harvesting Data` field, along with any other recommendations on how to proceed with this harvest.
-   Fill out all of the fields in the Research section to the best of your ability.
-   Occasionally, URL's will have been nominated separately, but are actually different interfaces built on the same dataset. We want to scrape all of this data and do it exactly one time. The `Link URL` field lets you search for associated URLs; add any URLs that should be grouped into a single record.

#### YES and NO

For example, FTP address, mixed content, big data sets:
<!--  - Fill out the cell "Can it be crawled?" = "yes & no" in Researcher section of the spreadsheet-->

-   Nominate it anyway, but also follow the steps for uncrawlable content above.
-   *While we understand that this may result in some dataset duplication, this is not a concern. We are ensuring that the data is fully preserved and accessible.*

<div class = "attention">
  <strong>See FAQ <a href="faq/#17-what-is-the-difference-between-crawlable-and-harvested">"What is the difference between Crawlable and Harvested in Archivers.space?"</a></strong>
</div>

## Finishing Up

-   In the Archivers app, make sure to fill out as much information as possible to document your work.
-   Check the Research checkbox (far right on the same line as the "Research" section heading) to mark that step as completed.
-   Click `Save`.
-   Click `Checkin this URL`, to release it and allow someone else to work on the next step.
-   You're done! Move on to the next URL!

<!-- HOW DOES THIS PROCESS WORK NOW:    - If ever a day or more passed  since you originally claimed the item, update the date to today's date.
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, the **Date field will turn red**, signaling that someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.-->
