# DataRescue Workflow

This document describes DataRescue activities both at in-person events and remotely, as developed by the [DataRefuge project](http://www.ppehlab.org/) and [EDGI](https://envirodatagov.org/). It explains the process that a URL/dataset goes through from the time it has been identified, either by a [Seeder](seeding.md) as difficult to preserve, or  "uncrawlable," until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) data catalog. The process involves several stages and is designed to maximize smooth hand-offs. At each step the data is with someone with distinct expertise and the data is always being tracked for security.

### Event Organizers

- Learn about what you need to do to [before an event](advance-work.md).

### Event Attendees

- Create an account on the [DataRefuge Slack](https://rauchg-slackin-qonsfhhvxs.now.sh/) or use the Slack team recommended by event organizers. This is where people share expertise and answer each other's questions.  
- Pick your role from below, get account credentials, and make sure you have access to the key documents and tools you need to work. Organizers will instruct you on these steps.
- Go over the workflow documentation below and read the relevant sections(s).

**********************

## Overview

### 1. [Seeding](seeding.md)

Seeders canvass the resources of a given government agency, identifying important URLs. They identify whether those URLs can be crawled by the Internet Archive's webcrawler. If the URLs are crawlable, the Seeders nominate them to the End-of-Term (EOT) project. Otherwise, they add them to the Archivers app using the project's Chrome Extension.

### 2. [Researching](researching.md)

Researchers inspect the "uncrawlable" list to confirm that Seeders' assessments were correct (that is, that the URL/dataset is indeed uncrawlable), and investigate how the dataset could be best harvested. [Researching.md](researching.md) describes this process in more detail.

*We recommend that Researchers and Harvesters (see below) work together in pairs, as much communication is needed between the two roles. In some cases, one person will fulfill both roles.*

### 3. [Harvesting](harvesting.md)

Harvesters take the "uncrawlable" data and try to figure out how to actually capture it based on the recommendations of the Researchers. This is a complex task which can require substantial technical expertise and different techniques for different tasks. Harvesters should also review the [Harvesting Toolkit](https://github.com/edgi-govdata-archiving/harvesting-tools) for tools.

### 4. Checking

**Note: This role is currently performed by the Baggers, and does not exist separately.**

Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.

### 5. [Bagging](bagging.md)

Baggers perform some quality assurance on the dataset to make sure the content is correct and corresponds to the original URL. Then they package the data into a bagit file (or "bag"), which includes basic technical metadata, and upload it to the final DataRefuge destination.

### 6. [Describing](describing.md)

Describers create a descriptive record in the DataRefuge CKAN repository for each bag. Then they link the record to the bag and make the record public.

**********************

## Partners

DataRescue is a broad, grassroots effort with support from numerous local and nationwide networks. [DataRefuge](http://www.ppehlab.org/datarefuge/) and [EDGI](https://envirodatagov.org/) partner with local organizers in supporting these events. See more of our institutional partners on the [DataRefuge home page](http://www.ppehlab.org/datarefuge#partners).
