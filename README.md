# DataRescue Workflow -- Overview

This document describes the workflow we use for the [DataRefuge project](http://www.ppehlab.org/), both at in-person events and when people work remotely. It explains the process that a url/dataset goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves several distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security.

## Before you begin
We are so glad that you are participating in this project!
- If you are an event organizer: learn about [what you need to do to prepare the event](advance-work.md).
- If you are a regular participant: get a role assignment (e.g., Seeder, or Harvester), get account credentials needed for your role, and go over the workflow corresponding to your role. 

## Plan Overview
### 1. [Seeders/Sorters](seednsort.md)
Seeders and Sorters will use the EDGI subprimer systems ([found here](https://envirodatagov.org/agency-forecasts/)), or a similar set of resources, to identify important/at risk data. Individual events should set up spreadsheets or other tools in which search efforts can be recorded. The work of this group includes:

- Canvassing the resources of a given government agency, identifying important URLs.
- Identifying whether those URL's [can be crawled by the Internet Archive's webcrawler](./what-heritrix-does.md)
    - If URL's are crawlable, nominate them to the EOT crawl using the [EDGI Nomination Tool](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok?hl=en)
    - If they are not crawlable, add them to the "Uncrawlable" spreadsheet, generating a UUID for this dataset.  the web-based tool [UUID Generator](https://www.uuidgenerator.net) can generate individual or multiple UUID's.

### 2. [Researchers](research.md)
Researchers inspect the "uncrawlable" list to confirm that seeders' assessments were correct (that is, that the URL/dataset is indeed uncrawlable). [Research.md](research.md) describes this process in more detail. 

*Often this step is incorporated into either "Seeding and Sorting" or "Harvesting".*

### 3. [Harvesters](harvesting-toolkit)
Harvesters take the "uncrawlable" data and try to figure out how to capture it. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks. Harvesters should see the included [Harvesting Toolkit](./harvesting-toolkit) for more details and tools. 

### 4. [Checkers](checking.md)
Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.

### 5. [Baggers](bagging.md)
- Do some quality assurance on the dataset to make sure the content is correct and corresponds to what was described in the spreadsheet
- Package the data into a bagit file (or "bag"), which includes basic technical metadata and upload it to final DataRefuge destination.


### 7. [Describers](metadata.md)
- Creates a CKan record for this S3 resource
- Links bag, makes public
