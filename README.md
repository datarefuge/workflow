# Overview

This document describes the process that a url/dataset goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves four distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security. 







**The [Seeders and Sorters](seednsort.md) **
- canvas the resources of a given government agency, identifying important URLs. 
- Sort them by whether their data can be automatically captured by the Internet Archive webcrawler 
- Nominate urls for the internet archive if they are crawlable and mark them as "uncrawlable" if they're not.

**The [Researchers](research.md) **
- evaluate a url to see if it is indeed crawlable
- make a plan for how the data might be accessed.
  
**The [Harvesters](harvesting.md)***
- download uncrawlable data. Often is it easiest for the person who researched an entry to also harvest it, obtaining technical assistance
  from fellow researchers/harvesters as needed. 
  Create brief metadata json file and notes for the next steps
- At the end of the harvesting process, this data is uploaded to a temporary storage location. 

**The [Baggers](bagging.md)** 
- do quality assurance on the work of the harvesters to make sure that a second pair of eyes has passed over each dataset
- ensre that everything a researcher would need to understand the data is present. 
- Package the data into a bagit file, which includes some metadata, and move it into an Amazon S3 bucket where it will be accessible from ckan.

**The [Metadata](metadata.md) team** 
- creates a CKan record for this S3 resource.
- links bag, makes public



