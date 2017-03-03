## What Do Describers Do?

Describers create a descriptive record in the DataRefuge CKAN repository for each bag. Then they link the record to the bag and make the record public.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you have experience working with scientific data (particularly climate or environmental data) or with metadata practices.
</div>

## Getting Set up as a Describer

- Apply to become a Describer by asking your DataRescue guide or by filling out [this form](https://docs.google.com/a/temple.edu/forms/d/e/1FAIpQLSfh9YIFnDrc-Cuc0hTd-U37J3D8xw8K7VXmzWkPs6Y5Q0wfVg/viewform).
    - Note that an email address is required to apply.
    - Note also that you should be willing to have your real name be associated with the datasets, to follow archival best practices (see [guidelines on archival best practices for DataRefuge](http://www.ppehlab.org/blogposts/2017/2/1/data-refuge-rests-on-a-clear-chain-of-custody) for more information).
- The organizers of the event (in-person or remote) will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
  	- Click the invite link, and choose a user name and a password.
- Create an account on the DataRefuge Slack using this [slack-in](https://rauchg-slackin-qonsfhhvxs.now.sh/) (or use the Slack team recommended by your event organizers). This is where people share expertise and answer each other's questions.
	- Ask your event organizer to send you an invite.
- The organizers will also create an account for you in the [datarefuge.org](https://www.datarefuge.org/) CKAN instance.
    - Test that you can log in successfully.
- Get set up with Python and the [`bagit-python`](https://github.com/LibraryOfCongress/bagit-python) script to make a bag at the command line
- If you need any assistance:
    - Talk to your DataRescue guide if you are at an in-person event.
    - Or post questions in the DataRefuge Slack `#describers` channel (or other channel recommended by your event organizers).

## Claiming a Bag

- You will work on datasets that were bagged by Baggers.
- Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `DESCRIBE`: all the URLs listed are ready to be added to the CKAN instance.
    - Available URLs are ones that have not been checked out by someone else, i.e. that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Checkout this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.

<div class = "note">
  <strong>Note: URL vs UUID</strong> <br />  
  The <code>URL</code> is the link to examine and harvest, and the <code>UUID</code> is a canonical ID we use to connect the URL with the data in question. The UUID will have been generated earlier in the process. UUID stands for Universal Unique Identifier.
</div>

## QA Step

- In the Archivers app, scroll down to the `Describe` section.
- The URL of the zipped bag is in the `Bag Url / Location` field.
- Cut and paste that URL into your browser and download it.
- After downloading, unzip it.
- Spot-check some of the files (make sure they open and look normal, i.e., not garbled).
- If the file fails QA:
    - Uncheck the Bagging checkbox.
    - Make a note in the `Notes From Bagging` field, explaining in what way the bag failed QA and asking a bagger to please fix the issue.

## Create New Record in CKAN

- Go to [CKAN](https://www.datarefuge.org/) and click Organizations in the top menu.
- Choose the organization (i.e., federal agency) that your dataset belongs to, e.g. `NOAA`, and click it.
    - If the Organization you need does not exist yet, create it by clicking `Add Organization`.
- Click "Add Dataset".
- Start entering metadata in the new record, following the metadata template below:
    - **Title:** Title of dataset, e.g., "Form EIA-411 Data".
    - __Custom Text: DO NOT Fill OUT (this field does not function properly at this time)__
    - **Description:** Usually copied and pasted description found on webpage.
    - **Tags:** Basic descriptive keywords, e.g., "electric reliability", "electricity", "power systems".
    - **License:** Choose value in dropdown. If there is no indicated license, select "Other - Public Domain".
    - **Organization:** Choose value in dropdown, e.g., "United States Department of Energy".
    - **Visibility:** Select "Public".
    - **Source:** URL where site is live, also in JSON, e.g. "http://www.eia.gov/electricity/data/eia411/".
- To decide what value to enter in each field:
    - Open the JSON file that is in the bag you have downloaded; it contains some of the metadata you need.
    - Go to the original location of the item on the federal agency website (found in the JSON file), to find more facts about the item such as description, title of the dataset, etc.
        - Alternatively, you can also open the HTML file that should be included in the bag and is a copy of that original main page.

## Enhancing Existing Metadata

These sites have federally-sourced metadata that can be added to the CKAN record for more accurate metadata:

- EPA:
    - [https://www.epa.gov/enviro/facility-registry-service-frs](https://www.epa.gov/enviro/facility-registry-service-frs)
    - [https://edg.epa.gov/metadata/catalog/main/home.page](https://edg.epa.gov/metadata/catalog/main/home.page)

These sites are sources of scientific metadata standards to review when choosing keywords:

- GCMD Keywords, downloadable CSV files of the GCMD taxonomies:
    - [https://wiki.earthdata.nasa.gov/display/cmr/gcmd+keyword+access](https://wiki.earthdata.nasa.gov/display/cmr/gcmd+keyword+access)
- ATRAC, a free tool for accessing geographic metadata standards including auto-populating thesauri (GCMD and others commonly used with climate data):
    - [https://www.ncdc.noaa.gov/atrac/index.html](https://www.ncdc.noaa.gov/atrac/index.html)

## Linking the CKAN Record to the Bag

- Click "Next: Add Data" at the bottom of the CKAN form.
- Enter the following information:
    - **Link:** Bag URL, e.g., `https://drp-upload-bagger.s3.amazonaws.com/remote/77DD634E-EBCE-412E-88B5-A02B0EF12AF6_2.zip`.
    - **Name:** filename, e.g., `77DD634E-EBCE-412E-88B5-A02B0EF12AF6_2.zip`.
    - **Format:** select "Zip".
- Click "Finish".
- Test that the link you just created works by clicking it, and verifying that the file begins to download.
    - Note that you don't need to finish downloading it again.
    - Alternatively, use WGET to test without downloading: `wget --spider [BAG URL]`

## Adding the CKAN record to the "Data Rescue Events" group

- Once the record is created, click the tab `Groups`  
- Select `Data Rescue Events` in the dropdown and click `Add to Group`.
- In the future, it will be useful to be able to differentiate that among different groups of records based on how they were generated.

## Finishing Up

- In the Archivers app, add the URL to the CKAN record in the `CKAN URL` field.
    - The syntax will be:
     `https://www.datarefuge.org//dataset/[datasetNameGeneratedByCkan]`
- Add any useful notes to document your work.
- Check the Describe checkbox (far right on the same line as the "Describe" section heading) to mark that step as completed.
- Click `Save`.
- Click `Checkin this URL`, to release it.

## Possible Tools: JSON Viewers

- [jsoneditoronline.org](http://www.jsoneditoronline.org/)
- [jsonviewer.stack.hu](http://jsonviewer.stack.hu/)
