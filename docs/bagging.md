## What do Baggers do?

Baggers do some quality assurance on the dataset to make sure the content is correct and corresponds to what was described in the spreadsheet. Then they package the data into a bagit file (or "bag"), which includes basic technical metadata and upload it to final DataRefuge destination.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you have data or web archiving experience, or have strong tech skills and an attention to detail.
</div>

## Getting set up as a Bagger

- Skills recommended for this role: in general, Baggers need to have some tech skills and a good understanding of harvesting goals.
- Apply to become a Bagger:
    - By filling out [this form](https://docs.google.com/a/temple.edu/forms/d/e/1FAIpQLSfh9YIFnDrc-Cuc0hTd-U37J3D8xw8K7VXmzWkPs6Y5Q0wfVg/viewform)
        - Note that an email address is required to apply.
        - Note also that you should be willing to have your real name be associated with the datasets, to follow archival best practices (see [guidelines on archival best practices for Data Refuge](http://www.ppehlab.org/blogposts/2017/2/1/data-refuge-rests-on-a-clear-chain-of-custody) for more information).
- The organizers of the event (in-person or remote) will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
  	- Click the invite link, and choose a user name and a password.
- Make sure you have an account on the DataRefuge slack (or other slack team recommended by your event organizers) This is where people share expertise and answer each other's questions.
- Ask your event organizer to send you an invite
- Get set up with Python and the Python script to make a bag at the command line  
[https://github.com/LibraryOfCongress/bagit-python](https://github.com/LibraryOfCongress/bagit-python)
- If you need any assistance:
  - Talk to your DataRescue Guide if you are at an in-person event
  - Or post questions on Slack in the #Baggers channel(or other channel recommended by your event organizers).

## Claiming a dataset for bagging

- You will work on datasets that were harvested by Harvesters.
- Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `BAG`: all the URLs listed are ready to be bagged
    - Available URLs are the ones that have not been checked out by someone else, that is, that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Check out this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
- While you go through the bagging process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

## Note: URL vs UUID

The `URL` is the link to examine and harvest, and the `UUID` is a canonical ID we use to connect the url with the data in question. The UUID will have been generated earlier earlier in the process. UUID stands for Universal Unique Identifier.

## Downloading & Opening the Dataset

- The zipped dataset that is ready to be bagged is under `Harvest Url / Location` in the the Archivers app. Download it to your laptop, and unzip it.
- Extra check: Is this URL truly ready to bag?
    - While everybody is doing their best to provide accurate information, occasionally a URL will be presented as "ready to bag", but, in fact, is not. Symptoms include:
   	- There is no value in the "Harvest Url / Location" field
  	- There is a note in the Harvest section that seem to indicate that the harvest was only partially performed.  
        - In either case, uncheck the "Harvest" checkbox, and add a note in the Harvest note, indicating that the URL does not seem ready for bagging and needs to be reviewed by a Harvester.

## Quality Assurance

- Confirm the harvested files:
    - Go to the original URL and check that the dataset is complete and accurate.
    - You also need to check that the dataset is meaningful, that is: "will the bag make sense to a scientist"?
    For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible for a scientist to use it.
    - Spot check to make sure the files open properly and are not faulty in any way.
- Confirm contents of Json file:
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

- If you make any changes, make sure to save this as a .json file.
- Confirm that the json file is within the package with the dataset(s)

## Creating the bag

- Run python command line script which creates the bag  
```
bagit.py --contact-name '[your name]' /directory/to/bag
```
- You should be left with a 'data' folder (which contains the downloaded content and metadata file) and four separate bagit files
    - bag-info.txt
    - bagit.txt
    - manifest-md5.txt
    - tagmanifest-md5.txt
- **IMPORTANT: It's crucial that you do not move or open the bag once you have created it. This may create hidden files that could make the bag invalid later.**
- Run the following python command line script to do an initial validation of a bag  
```
bagit.py --validate [directory/of/bag/to/validate]
```

- If it comes back as valid, proceed to the next step of creating the zip file and uploading it. If it does not, make a note of the error, review your steps, and re-bag the file. If you continue to get invalid bags, please see a DataRescue guide or reach out to the #bagging Slack channel.

## Creating the Zip file and uploading it

- Zip this entire collection (data folder and bagit files) and confirm that it is named with the row's UUID.
- **Without moving the file**, upload the zipped bag using the application http://drp-upload-bagger.herokuapp.com/ using the user ID and password provided
  - Make sure to select the name of your event in the dropdown (and "remote" if you are working remotely)
- The application will return the location URL for your zip file.
  - The syntax will be `[UrlStub]/[UUID].zip`
  - Cut and paste that URL to the `Bag URL` field in the Archivers app.
  - Note that files beyond 5 Gigs must be uploaded through the more advanced `Generate Upload Token` option. This will require using the aws command line interface.
  - Please talk to your DataRescue guide/post on Slack in Baggers channel, if you are having issues with this more advanced method.

## Quality assurance and finishing up

- Once the zip file has been fully uploaded, download the bag back to your computer (use the URL provided by the Archiver App) and run the following python command line script for validation
```
bagit.py --validate [directory/of/bag/to/validate]
```

- If it comes back as valid, open the bag and spot-check to make sure everything looks the same as when you uploaded it. (This will not affect the validity of the bags already uploaded). If all seems right, proceed to the rest of the quality assurance steps. If it does not come back as valid, make a note of the error, review your steps, and re-bag the file. If you continue to get invalid bags, please see a DataRescue guide or reach out to the #bagging Slack channel.
- Fill out as much information as possible in the `Notes From Bagging` field in the Archivers app to document your work.
- Check the checkbox that certifies this is a "well-checked bag"
- Check the Bag checkbox (on the right-hand side) to mark that step as completed.
- Click `Save`.
- Click `Check in URL` to release it and allow someone else to work on the next step.
