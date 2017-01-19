# Overview

This document describes the process that a url/dataset goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves four distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security. 







**The *[Seeders and Sorters](seednsort.md)* team: **
- canvases the resources of a given government agency, identifying important URLs. 
- Sort them by whether their data can be automatically captured by the Internet Archive webcrawler 
- Nominate urls for the internet archive if they are crawlable and mark them as "uncrawlable" if they're not.

**The *[Researchers](research.md)* **
- evaluate a url to see if it is indeed crawlable
- make a plan for how the data might be accessed.
  
The *[Harvesters](harvesting.md)* download uncrawlable data. Often is it easiest for the person
  who researched an entry to also harvest it, obtaining technical assistance
  from fellow researchers/harvesters as needed. At the end of the harvesting process, this data is uploaded to a temporary storage location. 
* The *[Baggers](bagging.md)* do quality assurance on the work of the harvesters to make sure that a second pair of eyes has passed over each dataset, and that everything a researcher would need to understand the data is present. They then package the data into a bagit file, which includes some metadata, and move it into an Amazon S3 bucket where it will be accessible from ckan.
* The *[Metadata](metadata.md)* team creates a CKan record for this S3 resource.







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
