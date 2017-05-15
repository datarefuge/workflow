## What Do Harvesters Do?

Harvesters take the "uncrawlable" data and try to figure out how to actually capture it based on the recommendations of the Researchers. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you're a skilled technologist with a programming language of your choice (e.g., Python, JavaScript, C, etc.), are comfortable with the command line (bash, shell, powershell), or experience working with structured data. Experience in front-end web development a plus.
</div>

## Getting Set up as a Harvester

-   The organizers of the event (in-person or remote) will tell you how to volunteer for the Harvester role, either through Slack or a form.
    -   They will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
    -   Click the invite link, and choose a username and a password. It is helpful to use the same username on the app and Slack.
-   Create an account on the DataRefuge Slack using this [slack-in](https://rauchg-slackin-qonsfhhvxs.now.sh/) (or use the Slack team recommended by your event organizers). This is where people share expertise and answer each other's questions.
-   You might also need other software and utilities set up on your computer, depending on the harvesting methods you use.
-   Harvesters should start by reading this document, which outlines the steps for constructing a proper data archive of the highest possible integrity. The primary focus of this document is on _semi-automated harvesting as part of a team_, and the workflow described is best-suited for volunteers working to preserve small and medium-sized collections. Where possible, we try to link out to other options appropriate to other circumstances.
-   If you need any assistance:
    -   Talk to your DataRescue guide if you are at an in-person event
    -   Or post questions in the DataRefuge Slack `#harvesters` channel (or other channel recommended by your event organizers).

<div class = "note">
  <strong>Researchers and Harvesters</strong> <br />  
  <ul>
    <li>Researchers and Harvesters should coordinate together as their work is closely related and benefits from close communication</li>
    <li>It may be most effective to work together in pairs or small groups, or for a single person to both research and harvest</li>
    <li>As a Harvester, make sure to check out the <a href="/researching/">Researching documentation</a> to familiarize yourself with their role</li>
  </ul>
</div>

## Harvesting Tools

For in-depth information on tools and techniques to harvest open data, please check EDGI's extensive [harvesting tools](https://github.com/edgi-govdata-archiving/harvesting-tools).

## 1. Claiming a Dataset to Harvest

<div class = "note">
  <strong>Using Archivers App</strong> <br />  
  Review our walkthrough video below and refer to the <a href="/faq/">FAQ</a> for any additional questions about the <a href="http://www.archivers.space" target="_blank">Archivers app</a><!--_-->. <br />
  &nbsp;<br />
  <p style="text-align:center"><iframe width="80%" height="315" src="https://www.youtube.com/embed/tvSSILnHnpA" frameborder="0" allowfullscreen></iframe></p>
</div>

-   You will work on datasets that were confirmed as uncrawlable by Researchers.
-   Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `HARVEST`: all the URLs listed are ready to be harvested.
     - Available URLs are the ones that have not been checked out by someone else, i.e. that do not have someone's name in the User column.
-   Select an available URL and click its UUID to get to the detailed view, then click `Checkout this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
-   While you go through the harvesting process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

<div class = "note">
  <strong>URL vs UUID</strong> <br />  
  The <code>URL</code> is the link to examine and harvest, and the <code>UUID</code> is a canonical ID we use to connect the URL with the data in question. The UUID will have been generated earlier in the process. UUID stands for Universal Unique Identifier.
</div>

## 2. Investigate the Dataset

<div class = "note">
  <strong>A "Meaningful Dataset"</strong> <br />  
  Your role is to harvest datasets that are complete and <em>meaningful</em>, by which we mean: "will the dataset make sense to a scientist"? <br />
  For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible for a scientist to use it.
</div>

### 2a. Classify Source Type & Archivability

Before doing anything, take a minute to understand what you're looking at. It's usually best to do a quick check of the URL to confirm that this data in fact not crawlable. Often as part of the harvesting team, you'll be the first person with a higher level of technical knowledge to review the URL in question.

#### Check for False-Positives (Content That Is in Fact Crawlable)

Generally, any URL that returns standard HTML, links to more [HTML mimetype pages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), and contains little-to-no non-HTML content, is crawlable. "View source" from your browser of choice will help see what the crawler itself is seeing. If in fact the data can be crawled, nominate it to the Internet Archive using the [EDGI Nomination Chrome Extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok), click the `Do not harvest` checkbox in the Research section of the Archivers app, click `Checkin this URL`, and move on to another URL.

A written guide on using the Chrome Nomination tool, the EDGI Primer Database, and a video tutorial are available [in Seeders' Documentation](seeding/#crawlable-urls). 

#### Some Things to Think About While Reviewing a URL

-   Does this page use JavaScript to render its content, especially to _generate links_ or _dynamically pull up images and PDF content_? Crawlers generally cannot parse dynamically generated content.
-   Does this URL contain links to non-HTML content? (For example, zip files, PDFs, Excel files, etc...)
-   Is this URL some sort of interface for a large database or service? (For example, an interactive map, API gateway, etc.)
-   Does this URL contain instructions for connecting to a server, database, or other special source of data?

#### Check the Terms of Service!

Before you go any further, it is _always_ worth confirming that the data in question is in fact open for archiving. If the terms of service explicitly prohibit archiving, _make a note of it_. Generally archive-a-thons are purposely only aimed at publically available data, but it is easy to follow a link away from a publically available source onto a site that has different terms of service.

_**Data acquired outside terms of service is not usable.**_

### 2b. Determine Scale of the Dataset

If the dataset you're looking at is quite large -- say, more than 1000 documents -- capturing it may require more elaborate programming than is described here, and it may be difficult to complete in the timeframe of the event. In that case, you may want to look outside the scope of this document and read the documentation of tools such as the [EIS WARC archiver](https://github.com/edgi-govdata-archiving/eis-WARC-archiver), which shows how to initiate a larger, fully automated harvest on a web-based virtual machine. Talk to your DataRescue guide to determine how to best proceed.

## 3. Generate HTML, JSON & Directory

To get started, click `Download Zip Starter`, which will download an empty zip archive structure for the data you are about to harvest.
The structure looks like this:

```no-highlight
DAFD2E80-965F-4989-8A77-843DE716D899
	├── DAFD2E80-965F-4989-8A77-843DE716D899.html
	├── DAFD2E80-965F-4989-8A77-843DE716D899.json
	├── /tools
	└── /data
```

Each row in the above is:

```no-highlight
A directory named by the UUID
	├── a .html "web archive" file of the URL for future reference, named with the ID
	├── a .json metadata file that contains relevant metadata, named with the ID
	├── a /tools directory to include any scripts, notes & files used to acquire the data
	└── a /data directory that contains the data in question
```

### Folder Structure

#### UUID

The goal is to pass this finalized folder off for ["bagging"](bagging.md). We repeatedly use the UUID so that we can programmatically work through this data later. It is important that the ID be copied _exactly_ wherever it appears, with no leading or trailing spaces, and honoring case-sensitivity.

#### [UUID].html file

The zip starter archive will automatically include a copy of the page corresponding to the URL. The HTML file gives the archive a snapshot of the page at the time of archiving which we can use to monitor for changing data in the future, and corroborate the provenance of the archive itself. We can also use the `.html` in conjunction with the scripts you'll include in the tools directory to replicate the archive in the future.

#### [UUID].json file

You'll need to inspect the .json manifest to be sure all fields are correct. This file contains vital data, including the url that was archived and date of archiving. The manifest should contain the following fields:

```
{
	"Date of capture": "",
	"File formats contained in package": "",
	"Free text description of capture process": "",
	"Individual source or seed URL": "",
	"Institution facilitating the data capture creation and packaging": "",
	"Name of package creator": "",
	"Name of resource": "",
	"Type(s) of content in package": "",
	"recommended_approach": "",
	"significance": "",
	"title": "",
	"url": ""
}
```

#### [UUID]/tools/

Directory containing any scripts, notes & files used to acquire the data. Put any scripts you write or tools you use into this directory. This is useful in case new data needs to be archived from the same site again at a later date.

#### [UUID]/data/

Directory containing the data in question.

## 4. Acquire the Data

Your method for doing this will depend on the shape and size of the data you're dealing with. A few methods are described below.

### 4a. Identify Data Links & Acquire Them in a wget Loop

If you encounter a page that links to lots of data (for example a "downloads" page), this approach may work well. It's important to only use this approach when you encounter _data_, for example PDF's, .zip archives, .csv datasets, etc.

The tricky part of this approach is generating a list of URLs to download from the page. If you're skilled with using scripts in combination with html-parsers (for example python's wonderful [beautiful-soup package](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)), go for it. Otherwise, we've included the [jquery-url-extraction guide](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/jquery-url-extraction), which has the advantage of working within a browser and can operate on a page that has been modified by JavaScript.

Our example dataset uses jquery-URL, [leveraging that tool to generate a list of URLs to feed the wget loop](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/jquery-url-extraction/README.md).

### 4b. Identify Data Links & Acquire Them via WARCFactory

For search results from large document sets, you may need to do more sophisticated "scraping" and "crawling" -- again, check out tools built at previous events such as the [EIS WARC archiver](https://github.com/edgi-govdata-archiving/eis-WARC-archiver) or the [EPA Search Utils](https://github.com/edgi-govdata-archiving/epa-search-utils) for ideas on how to proceed.

### 4c. FTP Download

Government datasets are often stored on FTP. It's pretty easy to crawl these FTP sites with a simple Python script. Have a look at [download_ftp_tree.py](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/ftp/download_ftp_tree.py) as an example. Note that the Internet Archive is doing an FTP crawl, so another option (especially if the dataset is large) would be to nominate this as a seed (though FTP seeds should be nominated **separately** from HTTP seeds).

### 4d. API Scrape / Custom Solution

If you encounter an API, chances are you'll have to build some sort of custom solution, or investigate a social angle. For example: asking someone with greater access for a database dump.

### 4e. Automated Full Browser

The last resort of harvesting should be to drive it with a full web browser. It is slower than other approaches such as `wget`, `curl`, or a headless browser. Additionally, this implementation is prone to issues where the resulting page is saved before it's done loading. There is a [ruby example](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/ruby-watir-collect).

### Tips

-   If you encounter a search bar, try entering "*"<!--*--> to see if that returns "all results".
-   Leave the data unmodified. During the process, you may feel inclined to clean things up, add structure to the data, etc. Avoid temptation. Your finished archive will be hashed so we can compare it later for changes, and it's important that we archive original, unmodified content.

## 5. Complete [UUID].json & Add /tools

From there you'll want to complete the [UUID].json. Use the template below as a guide.

-   The json should match the information from the Researcher and use the following format:

```
{
	"Date of capture": "Fri Feb 24 2017 21:44:07 GMT-0800 (PST)",
	"File formats contained in package": ".xls, .zip",
	"Free text description of capture process": "Metadata was generated by viewing page, data was bulk downloaded using download_ftp_tree.py and then bagged.",
	"Individual source or seed URL": "ftp://podaac-ftp.jpl.nasa.gov/allData/nimbus7",
	"Institution facilitating the data capture creation and packaging": "DataRescue SF Bay",
	"Name of package creator": "JohnDoe",
	"Name of resource": "Nimbus-7 SMMR global 60km gridded ocean parameters for 1979 - 1984",
	"Type(s) of content in package": "These files are the Wentz Nimbus-7 SMMR global 60km gridded ocean parameters for 1979 - 1984.  There are 72 files which breaks down to 1 file per month. So, NIMBUS7-SMMR00000.dat is January 1979, NIMBUS7-SMMR00001.dat is February 1979, etc.",
	"UUID": "F3499E3B-7517-4C06-A661-72B4DA13A2A2",
	"recommended_approach": "",
	"significance": "These files are the Wentz Nimbus-7 SMMR global 60km gridded ocean parameters for 1979 - 1984.  There are 72 files which breaks down to 1 file per month. So, NIMBUS7-SMMR00000.dat is January 1979, NIMBUS7-SMMR00001.dat is February 1979, etc.",
	"title": "Nimbus-7 SMMR global 60km gridded ocean parameters for 1979 - 1984",
	"url": "ftp://podaac-ftp.jpl.nasa.gov/allData/nimbus7"
}
```

-   Make sure to save this as a .json file.

In addition, copy any scripts and tools you used into the /tools directory. It may seem strange to copy code multiple times, but this can help later to reconstruct the archiving process for further refinement later on.

It's worth using some judgement here. If a "script" you used includes an entire copy of JAVA, or some suite beyond a simple script, it may be better to document your process in a file and leave that in the tools directory instead.

## 6. Uploading the data

-   Zip all the files pertaining to your dataset within the zip started archive structure and confirm that it is named with the original UUID.
-   Upload the zip file by selecting `Choose File` and then clicking `Upload` in the Archivers app.
-   Note that files beyond 5 Gigs must be uploaded through the more advanced `Generate Upload Token` option. This will require using the aws command line interface.
    -   Please talk to your DataRescue guide or post on Slack in the Harvesters channel, if you are having issues with this more advanced method.

<div class = "attention">
  <strong>See FAQ <a href="faq/#17-what-is-the-difference-between-crawlable-and-harvested">"What is the difference between Crawlable and Harvested in Archivers.space?"</a></strong>
</div>

## 7. Finishing up

-   In the Archivers app, make sure to fill out as much information as possible to document your work.
-   Check the Harvest checkbox (far right on the same line as the "Harvest" section heading) to mark that step as completed.
-   Click `Save`.
-   Click `Checkin this URL`, to release it and allow someone else to work on the next step.
-   You're done! Move on to the next URL!
