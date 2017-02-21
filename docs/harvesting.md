## What do Harvesters do?

Harvesters take the "uncrawlable" data and try to figure out how to actually capture it based on the recommendations of the Researchers. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you're a skilled technologist with a programming language of your choice (e.g., Python, JavaScript, C, etc.), are comfortable with the command line (bash, shell, powershell), or experience working with structured data. Experience in front-end web development a plus.
</div>

## Important notes

- **Researchers and Harvesters**
    - Researchers and Harvesters should work very closely together as their work will feed from each other and much communication is needed between the two roles
    - For instance they could work in pairs or in small groups
        - In some cases, a single person might be both a Researcher and a Harvester
    - As a Harvester, make sure to check out the [Researchers documentation](https://github.com/datarefuge/workflow/blob/master/research.md) to familiarize yourself with their role

- **The notion of "meaningful dataset"**
    - Your role is to harvest datasets that are complete and *meaningful*. By meaningful we mean: "will the bag make sense to a scientist"?
    - For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible for a scientist to use it.

## Getting set up as a Harvester

- Skills recommended for this role: in general, Harvesters need to have some tech skills and a good understanding of harvesting goals.
- The organizers of the event (in-person or remote) will tell you how to volunteer for the Harvester role, either through slack or a form.
    - As a result, they will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
    - Click the invite link, and choose a user name and a password.
- Make sure you have an account on the DataRefuge slack (or other slack team recommended by your event organizers) This is where people share expertise and answer each other's questions.
- Ask your event organizer to send you an invite
- You might also need to have some other software and utilities set up on your computer, depending on the harvested methods you will use.
- Harvesters should start by reading this document, which outlines the steps for constructing a proper data archive of the highest possible integrity. The primary focus of this document is on _semi-automated harvesting as part of a team_, and the workflow described is best-suited for volunteers working to preserve small and medium-sized collections. Where possible, we try to link out to other options appropriate to other circumstances.
    - If you need any assistance:
        - Talk to your DataRescue Guide if you are at an in-person event
        - Or post questions on Slack in the #Researchers/Harvesters channel (or other channel recommended by your event organizers).

## Harvesting Toolkit

For in-depth information on tools and techniques to harvest open data, please check EDGI's extensive [toolkit](https://github.com/edgi-govdata-archiving/harvesting-tools).

## 1. Claiming a dataset to harvest
- You will work on datasets that were confirmed as unscrawlable by Researchers.
- Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `HARVEST`: all the URLs listed are ready to be harvested
   - Available URLs are the ones that have not been checked out by someone else, that is, that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Check out this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
- While you go through the harvesting process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

### Note: URL vs UUID

The `URL` is the link to examine and harvest, and the `UUID` is a canonical ID we use to connect the url with the data in question. The UUID will have been generated earlier earlier in the process. UUID stands for Universal Unique Identifier.

## 2a. Classify Source Type & archivability

Before doing anything, take a minute to understand what you're looking at. It's usually best to have a quick check of the url to confirm that this data in fact not crawlable. Often as part of the harvesting team, you'll be the first person with a higher level of technical knowledge to review the url in question.

### Check for false-positives (content that is in fact crawlable)

Generally, any url that returns standard HTML, links to more [HTML mimetype pages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), and contains little-to-no non-html content, it's crawlable. "View source" from your browser of choice will help see what the crawler itself is seeing. If in fact the data can be crawled, make a note as such in the Google sheet, remove your name from the "checkout" column, notify the seeding / crawling team and they will make sure the link is crawled, and move on to another url.

### Some things to think about while reviewing a url

* Does this page use javascript to render its content, especially to _generate links_ or _dynamically pull up images and pdf content_? Crawlers generally cannot parse dynamically-generated content.
* Does this url contain links to non-html content? (For example, zip files, pdfs, excel files, etc...)
* Is this url some sort of interface for a large database or service? (For example, an interactive map, api gateway, etc.)
* Does this url contain instructions for connecting to a server, database, or other special source of data?

### Check the terms of service!!!

Before you go any further, it is *always* worth confirming that the data in question is in fact open for archiving. If the terms of service explicitly prohibit archiving, *make a note of it*. Generally archive-a-thons are purposely only aimed at publically available data, but it is easy to follow a link away from a publically-available source onto a site that has different terms of service.

**Data acquired outside terms of service is not usable**

If there is harvestable data, the next step is to set up a directory (step three), and then choose the appropriate strategy for archiving!

## 2b. Determine Scale of the Dataset

If the dataset you're looking at is quite large -- say, more than 1000 documents -- capturing it may require more elaborate programming than is described here, and it may be difficult to complete in the timeframe of the event. In that case, you may want to look outside the scope of this document and read the documentation of tools such as the [EIS WARC archiver](https://github.com/edgi-govdata-archiving/eis-WARC-archiver), which shows how to initiate a larger, fully automated harvest on a web-based virtual machine. Talk to your DataRescue Guide to determine how to best proceed.

## 3. Generate HTML, JSON & Directory

To get started click `Download Zip Starter`, which will download an empty Zip archive structure for the data you are about to harvest.
The structure looks like this:

```
DAFD2E80-965F-4989-8A77-843DE716D899
	├── DAFD2E80-965F-4989-8A77-843DE716D899.html
	├── DAFD2E80-965F-4989-8A77-843DE716D899.json
	├── /tools
	└── /data
```

Each row in the above is:

```
A directory named by the UUID
	├── a .html "web archive" file of the url for future reference, named with the ID
	├── a .json metadata file that contains relevant metadata, named with the ID
	├── a /tools directory to include any scripts, notes & files used to acquire the data
	└── a /data directory that contains the data in question
```

### UUID

The goal is to pass this finalized folder off for ["bagging"](bagging.md). We repeatedly use the UUID so that we can programmatically work through this data later. It is important that the ID be copied *exactly* wherever it appears, with no leading or trailing spaces, and honoring case-sensitivity.

#### [id].html file

The zip starter archive will automatically include a copy of the page corresponding to the URL. The html file gives the archive a snapshot of the page at the time of archiving which we can use to monitor for changing data in the future, and corroborate the provenance of the archive itself. We can also use the `.html` in conjunction with the scripts you'll include in the tools directory to replicate the archive in the future.

<!--To generate the html file, navigate to your new folder in a terminal window and run the following command:

	wget -O DAFD2E80-965F-4989-8A77-843DE716D899.html  http://www.eia.gov/electricity/data/eia412/

You'll replace ```DAFD2E80-965F-4989-8A77-843DE716D899.html``` with the ID + .html, and the url with the one you're looking at.-->

#### [id].json file

The json file is one you'll create by hand to create a machine readable record of the archive. This file contains vital data, including the url that was archived, and date of archiving. The [id.json readme](https://github.com/edgi-govdata-archiving/workflow/blob/master/id-json.md) goes into much more detail.

## 4. Acquire the Data

Your method for doing this will depend on the shape and size of the data you're dealing with. A few methods are described below.

### 4a. Identify Data Links & acquire them in a wget loop

If you encounter a page that links to lots of data (for example a "downloads" page), this approach may well work. It's important to only use this approach when you encounter *data*, for example pdf's, .zip archives, .csv datasets, etc.

The tricky part of this approach is generating a list of urls to download from the page. If you're skilled with using scripts in combination with html-parsers (for example python's wonderful [beautiful-soup package](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)), go for it. Otherwise, we've included the [jquery-url-extraction guide](thttps://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/jquery-url-extraction)], which has the advantage of working within a browser and can operate on a page that has been modified by javascript.

Our example dataset uses jquery-url, [leveraging that tool to generate a list of urls to feed the wget loop](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/jquery-url-extraction/README.md).

### 4b. Identify Data Links & acquire them via WARCFactory

For search results from large document sets, you may need to do more sophisticated "scraping" and "crawling" -- again, check out tools built at previous events such as the [EIS WARC archiver](https://github.com/edgi-govdata-archiving/eis-WARC-archiver) or the [EPA Search Utils](https://github.com/edgi-govdata-archiving/epa-search-utils) for ideas on how to proceed.

### 4c. FTP download

Government datasets are often stored on FTP. It's pretty easy to crawl these FTP sites with a simple Python script. Have a look at [download_ftp_tree.py](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/ftp/download_ftp_tree.py) as an example. Note that the Internet Archive is doing an FTP crawl, so another option (especially if the dataset is large) would be to nominate this as a seed (though FTP seeds should be nominated **separately** from http seeds).

### 4d. API scrape / Custom Solution

If you encounter an API, chances are you'll have to build some sort of custom solution, or investigate a social angle. For example: asking someone with greater access for a database dump.

### 4e. Automated Full Browser

The last resort of harvesting should be to drive it with a full web browser. It is slower than other approaches such as `wget`, `curl`, or a headless browser. Additionally, this implementation is prone to issues where the resulting page is saved before it's done loading. There is a [ruby example](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/ruby-watir-collect).

## 5. Write [id].json metadata, add /tools

From there you'll want to fill out the metadata.json. Use the template below as a guide.

- The json should match the information from the Harvester and use the following format:

```
{
 "Individual source or seed URL": "http://www.eia.gov/renewable/data.cfm",
 "UUID" : "E30FA3CA-C5CB-41D5-8608-0650D1B6F105",
 "id_agency" : 2,
 "id_subagency": ,
 "id_org":,
 "id_suborg":,
 "Institution facilitating the data capture creation and packaging": "Penn Data Refuge",
 "Date of capture": "2017-01-17",
 "Federal agency data acquired from": "Department of Energy/U.S. Energy Information Administration",
 "Name of resource": "Renewable and Alternative Fuels",
 "File formats contained in package": ".pdf, .zip",
 "Type(s) of content in package": "datasets, codebooks",
 "Free text description of capture process": "Metadata was generated by viewing page and using spreadsheet descriptions where necessary, data was bulk downloaded from the page using wget -r on the seed URL and then bagged.",
 "Name of package creator": "Mallick Hossain and Ben Goldman"
 }
```
 - Make sure to save this as a .json file.

In addition, copy any scripts and tools you used into the /tools directory. It may seem strange to copy code multiple times, but this can help later to reconstruct the archiving process for further refinement later on.

It's worth using some judgement here. If a "script" you used includes an entire copy of JAVA, or some suite beyond a simple script, it may be better to document your process in a file and leave that in the tools directory instead.

### Tips

- If you encounter a Search bar, try entering "*" to check to see if that returns "all results".
- Leave the data unmodified  
  During the process you may feel inclined to clean things up, add structure to the data, etc. Avoid temptation. Your finished archive will be hashed so we can compare it later for changes, and it's important that we archive original, unmodified content.

## 6. Uploading the data

- Zip the all the files pertaining to your dataset within the zip started archive structure and confirm that it is named with the original UUID
- Upload the zip file by clicking `Upload` in the Archivers app, and selecting `Choose File`
- Note that files beyond 5 Gigs must be uploaded through the more advanced `Generate Upload Token` option. This will require using the aws command line interface.
    - Please talk to your DataRescue guide/post on Slack in Baggers channel, if you are having issues with this more advanced method.

## 7. Finishing up

- In the Archivers app, make sure to fill out as much information as possible to document your work.
- Check the Harvest checkbox (on the right-hand side) to mark that step as completed.
- Click `Save`.
- Click `Check in URL`, to release it and allow someone else to work on the next step.
- You're done! Move on to the next URL!
