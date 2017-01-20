# Overview

This document describes the process that a url/dataset goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves several distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security.

## [Before you begin](advance-work.md)
- Get account credentials and go over workflow. 

## Plan Overview
### 1. [Seeding and Sorting](seednsort.md)
Seeders and Sorters will use the EDGI subprimer systems ([found here](https://envirodatagov.org/agency-forecasts/)), or a similar set of resources, to identify important/at risk data. Individual events should set up spreadsheets or other tools in which search efforts can be recorded. The work of this group includes:

- canvassing the resources of a given government agency, identifying important URLs.
- Idntifying whether those URL's [can be crawled by the Internet Archive's webcrawler](./what-heritrix-does.md)
    - If URL's are crawlable, nominate them to the EOT crawl using the [EDGI Nomination Tool](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok?hl=en)
    - If they are not crawlable, add them to the "uncrawlable" spreadsheet, generating a UUID for this dataset.  the web-based tool [UUID Generator](https://www.uuidgenerator.net) can generate individual or multiple UUID's.

### 2. Research
Resarchers inspect the "uncrawlable" list to confirm that seeders' assessments were correct (that is, that the URL/dataset is indeed uncrawlable. [Research.md](research.md) describes this process in more detail. 

*Often this step is incorporated into either "Seeding and Sorting" or "Harvesting".

### 3. [Harvesting](harvesting-toolkit)
Harvesters take the "uncrawlable" data and try to figure out how to capture it. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks. Harvesters should see the included [Harvesting Toolkit](./harvesting-toolkit) for more details and tools. **Group Leaders should familiarize themselves with this process before the start of the event.

### 4. [Bagging](bagging.md)
- do quality assurance on the work of the harvesters to make sure that a second pair of eyes has passed over each dataset
- ensure that everything a researcher would need to understand the data is present
- package the data into a bagit file, which includes basic technical metadata

### 5. [Uploading](uploaders.md)
- take finished bag-it file and upload to S3 instance

### 6. [Metadata](metadata.md)
- creates a CKan record for this S3 resource
- links bag, makes public
