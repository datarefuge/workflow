# Harvesting Toolkit

This package includes a general purpose toolkit for archiving open data.

## Getting set up as a Data Harvester
- Talk to your DataRescue guide to make sure you can become a Data Harvester.
- Get set up with the application http://drp-upload.herokuapp.com/
   - Credentials and other details will be provided by the organizers.
- Data Harvesters should start by reading this document, which outlines the steps for constructing a proper data archive of the highest possible integrity. The primary focus of this document is on _semi-automated harvesting as part of a team_, and thje workflow described is best-suited for volunteers working to preserve small and medium-sized collections. Where possible, we try to link out to other options appropriate to other circumstances.
- Contact your DataRescue guide, if you need any assistance.

## 1. Claiming a dataset to harvest

- You will work on datasets that were confirmed as unscrawlable by Researchers.
- Go to the Uncrawlable spreadsheet, and look for a dataset that has the status "Researcher status indicator" = Closed. Claim it by entering your slack handle with the status "Open" and today's date in the cell "Researcher status indicator" in Researcher section, for instance:
```
@khdelphine open 1/22/2017
```
- Note that the Uncrawlable spreadsheet is the starting and ending point for the collective archiving efforts. Many people will be working from this shared worksheet, so it's important to report all your work in the spreadsheet and update the status cell that shows that you have claimed a URL or are done working on it.

## URL vs ID
The url (in cell "Original URL")  is the link to examine, the id is a canonical id we'll use to connect the url with the data in question. The id will have been generated already by the researchers -- don't worry about that for now.

## 2a. Classify Source Type & archivability
Before doing anything, take a minute to understand what you're looking at. It's usually best to have a quick check of the url to confirm that this data in fact not crawlable. Often as part of the harvesting team, you'll be the first person with a higher level of technical knowledge to review the url in question.

#### Check for false-positives (content that is in fact crawlable)
Generally, any url that returns standard HTML, links to more [HTML mimetype pages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types), and contains little-to-no non-html content, it's crawlable. "View source" from your browser of choice will help see what the crawler itself is seeing. If in fact the data can be crawled, make a note as such in the Google sheet, remove your name from the "checkout" column, notify the seeding / crawling team and they will make sure the link is crawled, and move on to another url.

#### Some things to think about while reviewing a url
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

Before starting it's best to get a directory going for the data you're going to archive. You will be in charge of creating and collecting this structure for each link that's deemed uncrawlable. Using the example from step 1, the structure of the archive will look like so:

	DAFD2E80-965F-4989-8A77-843DE716D899
		├── DAFD2E80-965F-4989-8A77-843DE716D899.html
		├── DAFD2E80-965F-4989-8A77-843DE716D899.json
		├── /tools
		└── /data

Each row in the above is:

	A directory named by the spreadsheet id
		├── a .html "web archive" file of the url for future reference, named with the id
		├── a .json metadata file that contains relevant metadata, named with the id
		├── a /tools directory to include any scripts, notes & files used to acquire the data
		└── a /data directory that contains the data in question


The goal is to pass this finalized folder off for ["bagging"](example/DAFD2E80-965F-4989-8A77-843DE716D899/DAFD2E80-965F-4989-8A77-843DE716D899.json). We repeatedly use the ID so that we can programmatically work through this data later. It is important that the ID be copied *exactly*, with no leading or trailing spaces, and honoring case-sensitivity.

#### [id].html file
The first thing you'll want to create is a html copy of the page in question. The html file gives the archive a snapshot of the page at the time of archiving which we can use to monitor for changing data in the future, and corrobrate the provenance of the archive itself. We can also use the .html in conjunction with the scripts you'll include in the tools directory to replicate the archive in the future. To generate the html file, navigate to your new folder in a terminal window and run the following command:

	wget -O DAFD2E80-965F-4989-8A77-843DE716D899.html  http://www.eia.gov/electricity/data/eia412/

You'll replace ```DAFD2E80-965F-4989-8A77-843DE716D899.html``` with the id + .html, and the url with the one you're looking at.

#### [id].json file
The json file is one you'll create by hand to create a machine readable record of the archive. This file contains vital data, including the url that was archived, and date of archiving. The [id.json readme](docs/id-json.md) goes into much more detail.

## 4. Acquire the Data
Your method for doing this will depend on the shape and size of the data you're dealing with. A few methods are described below.

### 4a. Identify Data Links & acquire them in a wget loop
If you encounter a page that links to lots of data (for example a "downloads" page), this approach may well work. It's important to only use this approach when you encounter *data*, for example pdf's, .zip archives, .csv datasets, etc.

The tricky part of this approach is generating a list of urls to download from the page. If you're skilled with using scripts in combination with html-parsers (for example python's wonderful [beautiful-soup package](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)), go for it. Otherwise, we've included the [jquery-url-extraction guide](tools/jquery-url-extraction)], which has the advantage of working within a browser and can operate on a page that has been modified by javascript.

Our example dataset uses jquery-url, [leveraging that tool to generate a list of urls to feed the wget loop](tools/jquery-url-extraction/README.md).

### 4b. Identify Data Links & acquire them via WARCFactory

For search results from large document sets, you may need to do more sophisticated "scraping" and "crawling" -- again, check out tools built at previous events such as the [EIS WARC archiver](https://github.com/edgi-govdata-archiving/eis-WARC-archiver) or the [EPA Search Utils](https://github.com/edgi-govdata-archiving/epa-search-utils) for ideas on how to proceed.


### 4c. FTP download
Government datasets are often stored on FTP. It's pretty easy to crawl these FTP sites with a simple Python script. Have a look at [download_ftp_tree.py](tools/ftp/download_ftp_tree.py) as an example. Note thatteh Internet Archive is doing an FTP crawl, so another option (especially if the dataset is large) would be to nominate this as a seed (though FTP seeds should be nominated **seperately** from http seeds).

### 4d. API scrape / Custom Solution
If you encounter an api, chances are you'll have to build some sort of custom solution, or investigate a social angle. For example: asking someone with greater access for a database dump.

### 4e. Automated Full Browser
The last resort of harvesting should be to drive it with a full web browser.  It is slower than other approaches such as wget, curl, or a headless browser.  Addiionally, it's prone to issues where the resuling page is saved before it's done loading.  There is a ruby example in [tools/example-hacks/watir.rb](tools/example-hacks/watir.rb)

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

## Tips
- If you encounter a Search bar, try entering "*" to check to see if that returns "all results".
- Leave the data unmodified
During the process you may feel inclined to clean things up, add structure to the data, etc. Avoid temptation. Your finished archive will be hashed so we can compare it later for changes, and it's important that we archive original, unmodified content.

## 6. Uploading the data
- Zip the all the files pertaining to your dataset, so that you have a resulting zip file.
- Upload the Zip file using the application http://drp-upload.herokuapp.com/
   - Make sure to select the name of your event in the dropdown (and "remote" if you are working remotely)
   -  Note that files beyond 5 Gigs cannot be uploaded through this method
     - Please talk to your DataRescue guide, if you have a larger file
 - Quality assurance:
   - To ensure that the zip file was uploaded successfully, go to the URL and download it back to your computer.
   - Unzip it, open it and spot check to make sure that all the files are there and seem valid.
- Re-uploading: if you found a problem in your first zip (e.g., you realized you missed a file) and would like to upload an improved one, that's ok. Just proceed as you did for the first upload.

## 7. Finishing up
- In the Uncrawlable spreadsheet, briefly describe the method used for harvesting in cell "Method Used" in Harvester section
- In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Harvester status indicator", for instance:
  ```
  @khdelphine closed 1/22/2017
  ```
  - If ever a day or more passed since you originally claimed the item, update the date to today's date.
  - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, someone else can claim it in your place and start working on it
    - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
- You're done! Stand up, do a happy dance, and move on to the next url!
