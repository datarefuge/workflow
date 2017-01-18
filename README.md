# Overview

This document describes the process that a site goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves four distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security. 







* The *[Seeders and Sorters](seednsort.md)* team canvases the resources of a given government
  agency, identifying important URLs. They sort them by whether their data
  can be automatically captured by the Internet Archive webcrawler (about which
  more
  [here](https://docs.google.com/document/d/1PeWefW2toThs-Pbw0CMv2us7wxQI0gRrP1LGuwMp_UQ/edit)
  and
  [here](https://docs.google.com/document/d/1qpuNCmBmu4KcsS_hE2srewcCiP4f9P5cCyDfHmsSAVU/edit)).
  URLs judged to be possibly crawlable are "nominated" (equivalently, "seeded")
  using our
  [Chrome extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok)
  or
  [bookmarklet](http://digital2.library.unt.edu/nomination/eth2016/about/).
  This sorting is only provisional: when in doubt seeders mark a URL as possibly
  *not* crawlable, and these URLs populate a spreadsheet.
* The *Researchers* evaluate each entry in the spreadsheet to confirm whether
  it is indeed not automatically crawlable by the Internet Archive and, if so,
  how the data might be accessed.
* The *Havesters* download uncrawlable data. Often is it easiest for the person
  who researched an entry to also harvest it, obtaining technical assistance
  from fellow researchers/harvesters as needed. At the end of the harvesting process, this data is uploaded to a temporary storage location. 
* The *Baggers* do quality assurance on the work of the harvesters to make sure that a second pair of eyes has passed over each dataset, and that everything a researcher would need to understand the data is present. They then package the data into a bagit file, which includes some metadata, and move it into an Amazon S3 bucket where it will be accessible from ckan.
* The *Metadata* team creates a CKan record for this S3 resource.

**NOTE THAT THE COLUMNS REFERED TO IN THIS DOCUMENT, UNLESS OTHERWISE NOTED COME FROM [THIS SPREADSHEET](https://docs.google.com/spreadsheets/d/1nevyzpc-vwoK6krngEASPJS5_ngrOwD2qYUPxLVesrg/edit).**

## SEEDERS AND SORTERS

TO DO

# RESEARCH (BLUE Cell Headers, Columns L-R)

First pick a link in the spreadsheet to evaluate. 

Fill in your name in Column __ to claim ("check out") your link so there are no
duplicate researching efforts.

Keep in mind two things when looking at the spreadsheet: 



### Is the data actually actually crawlable?

Again, see [here](https://docs.google.com/document/d/1PeWefW2toThs-Pbw0CMv2us7wxQI0gRrP1LGuwMp_UQ/edit)
and
[here](https://docs.google.com/document/d/1qpuNCmBmu4KcsS_hE2srewcCiP4f9P5cCyDfHmsSAVU/edit)
for a mostly non-techincal introduction to the crawler. Some additional
technical notes for answering this:

- There is no specific file size cutoff on what is crawlable, but large files
  should be manually captured anyway.
- Files types like ZIP, PDF, Excel, etc. are crawlable if they are linked.
- The crawler can only follow HTTP links that appear directly in the DOM at load
  time. (That is, they should appear as `<a href ...>` tags in the page source.)
  If links are added by Javascript or require submitting a form, they are
  not crawlable.
- The crawler does not tolerate web frames (but it straightforward to inspect
  a page to obtain the content in the frame directly, and then nominate *that*).
- The crawler recently added the ability to crawl FTP, but we will not rely on
  this; we will treat resources served over FTP as uncrawlable.

What to do in each case:

- YES: If the URL is crawlable or you locate a crawlable URL that accesses the
  underlying dataset:
  - Nominate it: use our
    [Chrome extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok),
    and if that doesn't work then use the
    [bookmarklet](http://digital2.library.unt.edu/nomination/eth2016/about/)
  - Fill out that you seeded (Column __)
  - Fill out that link is done (Column __)
- NO: If it is confirmed not crawlable:
  - Search agency websites and data.gov for dataset entry points for your dataset collection   
  - Add harvastable data url to spreadsheet (Column ), REALLY IMPORTANT! 
  - Learn what actual datasets look like in terms of format  (SQL, FTP, ZIP, PDF Collections, etc.), size,  what you found, etc. (Column )
- YES AND NO: for example, FTP address, mixed content, big data sets:
  - Nominate it anyway, but folow the steps for uncrawlable content above.
  - *While we understand that this may mean duplicate sets of data in the ckan, that is not a concern. We are ensuring that the data is fully preserved and accessible.*

Try to understand what data sets are underlying the web pages. Look for related
entries in the spreadsheet, and ensure that you aren't harvesting a subdirectory
if you can harvest the entire directory. Often, data underlying dozens of pages
or multiple "access portal" apps is also available as one structured data file.

# HARVESTING 

Check out a URL on a google sheet 

Link identification - method of identification 

List of URLS 

WGet loop —> consumes list with 4 second delay between each download so we don't get kicked out  —> data directory 

Write metadata. Json with as much info as possible

Package as [uuid.zip] and [uuid.json] 

Mark as Harvested google sheet

# BAGGING 

- Check out a package (Column Y)
- Data comes from S3 Bucket
- Take folder and create metadata folder for Json template. 
- Label the json file and the folder where the json folder where it is located with the uuid.
- The json should 

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

- Make sure to save as a .json file.

- Copy the metadata file into folder where the package is 

- Run python command line script which creates the bag 

  - [Python script to make a bag (command line)]: https://github.com/LibraryOfCongress/bagit-python

    ****

  ```
  bagit.py --contact-name 'John Kunze' /directory/to/bag
  ```

- You should be left with a metadata file and four seperate bagit files 

  - bag-info.txt
  - bagit.txt
  - manifest-md5.txt
  - tagmanifest-md5.txt
  - data  (package of stuff)

- Zip this entire bagit file, data file, plus four txt files listed 

- Put the zip file onto a thumb drive and give to an uploader

# UPLOADING (Yellow Cell Headers)

- Claim you the link you are uploading (Column)
- Follow the instructions below:

You will need python and pip in order for this to work.

#### **Getting your machine ready to upload:**

**Download:**

```
pip install awscli
```

Get your access keys from the system administrator for the s3 bucket. You should have two access keys, an "Access key ID" and a "Secret access key"

**Run:**

```
aws configure
```

The script will ask for a few things:

```
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: 
Default output format [None]: 
```

Enter your two aws access keys

Press enter for the default output format and region name (you don't need to have anything in this field)

**Run:**

`aws s3 ls nameofbucket`

You should see a list of files, such as:

```
2017-01-12 16:38:44  713031680 CentOS-7-x86_64-Minimal-1611.iso
2017-01-12 18:35:20     104065 Linear_Bone_13.stl
2017-01-12 16:25:00         21 index.html
```

------

### **Uploading files**

**To upload a file or folder to the s3 bucket:**

```
aws s3 cp --recursive [folder name]  s3://nameofbucket

aws s3 cp [file name]  s3://nameofbucket
```

# METADATA (GREEN Cell Headers, Columns AB-AD)

- Get data from CKAN S3 Bucket

- Checkout metadata link for file (column)

- Create new record in CKan

- Follow metadata schema spreadsheet (https://docs.google.com/spreadsheets/d/12JAleU6eF4wgu0hIlQ5efoOUCsZjT-UkRxwAofVZp6c/edit#gid=1879921913)

- Go to original url (Column) to gather the rest of the metadata facts needed to populate the fields in the metadata mapping form

- Upload the JSON file (from thumbdrive) to CKan

- Click link from the S3 bucket that you have populated in the form that you copied from the spreadsheet. 

- The link should download the bag file, but we want to double check.

- Unzip the file

- Spot check the files (Column )

  - If there are problems talk to a guid

- Let everyone know you are done (Column )

  ​
