
## Advance work

This document is meant for DataRescue event organizers. There are lots of ways to prepare for an event. This document highlights only the technical aspects of preparation. There are lots of logistical and other aspects to look out for as well, but this is the minimum needed to use the workflow we propose.  

Note that after an event, participants might want to continue the work remotely, and our workflow is designed to make that possible.


Before starting, your team should go through the following steps. 

### The basics
- Read through the entire workflow documentation
- Sign up for the datarefuge slack and make sure there's a channel for your event. 
- Define your teams. They are usually: Seeders/Sorters, Researchers, Harvesters, Checkers, Baggers, and Describers. Although in some cases, some of the roles can be conflated. Each team should have team leaders, aka "guides". 
- The event organizers and team leaders should schedule a call with DataRefuge to go over the process. 
- The event organizers and team leaders for the Seeders and Sorters should also check in with EDGI folks for info about how to make sure that you're seeding and sorting effectively. 

### Spreadsheets
- Make sure you know the spreadsheets you will be using and where to begin. Talk to a DataRefuge coordinator to establish that.
 - The goal is keep track of which URLs have already been archived and which ones have not, and avoid any duplication of effort. 

### Crawl vs. Harvest: storage needs 
- The main triage point of the workflow is whether a URL can be automatically crawled, for instance by the Internet Archive, or whether it  needs to be manually harvested.
 - The crawling process does not require any separate storage management, as the crawlable URLs are nominated to the Internet Archive, who will take care of the actual file storage after they have crawled the pages. See the [Seeders/Sorters documentation](seednsort.md) for more information on this process. 
 - The datasets harvested through the Harvest process are stored on S3 storage managed directly by DataRefuge.

### S3 storage
- You need two S3 "buckets" (i.e., directories) for your harvested files.  
 - The Harvesters will upload the files they harvest to the first bucket ("pre-bag" bucket), and then
 - The Baggers will turn those files into bags and upload the bags to the second bucket ("bag" bucket)
- Get the **name of the two s3 buckets** for your event from DataRefuge. Each event has its own pair of buckets, so you'll need to refer to those specific bucket names in all URLs pointing to S3 (e.g., the URLs to the pre-bag and bag Zip files).
 - Most uploads to S3 will be done through the web-based Uploader application (http://drp-upload.herokuapp.com/ or http://drp-upload-bagger.herokuapp.com/). This application can handle files up to 5 Gigs.
 - One person at the event should be designated as the S3 System Administrator and will have direct access to the S3 buckets for the event. The S3 Sys Admin should be someone with advanced technical skills and will be responsible for 2 things:
  - Upload very large sets (beyond 5 Gigs) through an alternate method (provided by DataRefuge)
  - Keep the buckets cleaned up and organized . Uploaders need not be coders, but they should have a little experience working in command line, and computers with python 2.7.
  
### Credentials
Specific roles need special credentials:
- The S3 System Administrator needs **credentials for s3**. 
- The Describers (Ckan/Metadata folks) need **credentials for ckan**. 

### Other supplies
Make sure you have a few thumb drives to handle very large data sets (above 5 Gigs).

### Spreadsheet Minder

A designated Spreadsheet Minder needs to keep an eye on the Unscrawlable spreadsheet. The Spreadsheet Minder's tasks include:
- Generating enough universal unique ID (UUIDs) ahead of time, and cutting and pasting them in the UUID column (in the spreadsheet's empty rows). They will allow new URLs being added to the spreadsheet to be immediately associated with a UUID.
 -  The web-based tool [UUID generator](https://www.browserling.com/tools/random-uuid) can generate individual or multiple UUIDs.
- While participants are doing active work and adding information to the spreadsheet, keeping an eye on it, making sure that everything looks in good order.
- Making sure the spreadsheet remains stocked with enough new UUIDS, as more URLs get added by participants. 



