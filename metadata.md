# Describers: CKAN/Metadata

## What do Describers do?
Describers creates a descriptive record in the DataRefuge CKAN repository for each bag. Then they links the record to the bag, and make the record public

## Getting set up as a Describer
  - Apply to become a Describer 
    - By asking your DataRescue guide or by filling out [this form](https://docs.google.com/a/temple.edu/forms/d/e/1FAIpQLSfh9YIFnDrc-Cuc0hTd-U37J3D8xw8K7VXmzWkPs6Y5Q0wfVg/viewform)
    - Skills recommended: in general, Describers need to have a good handle on metadata practices 
    - Note that an email address is required to apply.
    - Note also that you should be willing to have your real name be associated with the datasets, to follow archival best practices (see [guidelines on archival best practices for Data Refuge](http://www.ppehlab.org/blogposts/2017/2/1/data-refuge-rests-on-a-clear-chain-of-custody) for more information).
  - Credentials, slack invite, Uncrawlable spreadsheet URL, and other details will be provided once your application is approved.
 - Test that you can get into the CKAN instance at https://www.datarefuge.org/ with the credentials provided
   - Verify that you have write access to the Describers tab in the Uncrawlable spreadsheet
  - If you need any assistance:
      - Talk to your DataRescue Guide if you are at an in-person event
      - Or post questions on Slack in the #Describers channel.

## Claiming a bag
  - You will work on datasets that were last checked by Checkers. 
  - Go to the Uncrawlable spreadsheet, click the Describers tab, and look for a dataset to describe
    - Available datasets are the ones whose cell "Describer Handle" is empty
    - If an item is already claimed but its "Date Opened or Closed" cell has turned red, it is also available for you to claim (for more details see the last section of this document)
  - Claim it by entering your slack handle along with the status "Open" and today's date, for instance: 
  ```
  @khdelphine Open 1/22/2017
  ```

## QA step 
  - In the "Uncrawlable Content" spreadsheet, click on URL in the "Bag URL" cell.   
  - The file should start downloading
  - When it is downloaded, unzip it 
  - Spot check some of the files (make sure they open and look normal, i.e., not garbled)

## Create new record in CKAN
  - Click "Add Dataset" in [CKAN](https://www.datarefuge.org/)
  - Start entering metadata following the metadata schema spreadsheet (https://docs.google.com/spreadsheets/d/12JAleU6eF4wgu0hIlQ5efoOUCsZjT-UkRxwAofVZp6c/edit#gid=1879921913)
  - To decide what value to enter in each field:
    - Open JSON file that is in the bag you have downloaded; it contains some of the metadata you need
    - Go to the original location of the item on the federal agency website, to find more more facts about the item such as description, title of the dataset, etc. (See "Original URL" cell in Unscrawlable spreadsheet.)
    
## Linking the CKAN record to the bag:
  - Click "Next: Add Data" at the bottom of the CKAN form
  - Click "Link" and enter the Bag URL in the text field
  - Click "Finish"
  - Test that the link you just created work by clicking it, and verifying that the file begins to download. 
    - Note that you don't need to finish downloading it again.

## Finishing up
  - In the Uncrawlable spreadsheet, add URL to the ckan record in cell "ckan record URL"
    - The syntax will be "https://www.datarefuge.org//dataset/[datasetNameGeneratedByCkan]
  - In the Uncrawlable spreadsheet, make sure you document all the actions you have taken by filling out all the cells.
  - In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Current Status", for instance: 
  ```
  @khdelphine Closed 1/22/2017
  ```
    - If ever a day or more passed  since you originally claimed the item, update the date to today's date. 
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, the **Date field will turn red**, signaling that someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
