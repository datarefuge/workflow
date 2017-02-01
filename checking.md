

# Checkers

## What do Checkers do?
Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? 

## Getting set up as a Checker
  - Apply to become a Checker 
    - By asking your DataRescue guide or by filling out [this form](https://docs.google.com/a/temple.edu/forms/d/e/1FAIpQLSfh9YIFnDrc-Cuc0hTd-U37J3D8xw8K7VXmzWkPs6Y5Q0wfVg/viewform) 
    - Skills recommended: in general, Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.
    - Note that an email address is required to apply.
    - Note also that you should be willing to have your real name be associated with the datasets, to follow archival best practices (see [guidelines on archival best practices for Data Refuge](http://www.ppehlab.org/blogposts/2017/2/1/data-refuge-rests-on-a-clear-chain-of-custody) for more information).
  - Credentials, slack invite, Uncrawlable spreadsheet URL, and other details will be provided once your application is approved.
  - Test the Uploader application http://drp-upload.herokuapp.com with the credentials provided
    - Make sure to select the right event in the dropdown
  - Verify that you have write access to the Checkers tab in the Uncrawlable spreadsheet
  - You might also need to have some other software and utilities set up on your computer, depending methods you will use, when needing to harvest supplemental materials to add to a dataset.
  - If you need any assistance:
      - Talk to your DataRescue Guide if you are at an in-person event
      - Or post  questions on Slack in the #Checkers channel.

## Claiming a dataset for the checking step 
  - You will work on datasets that were harvested by Harvesters. 
  - Go to the Uncrawlable spreadsheet, click the Checkers tab, and look for a dataset to check
    - Available datasets are the ones whose cell "Checker Handle" is empty
    - If an item is already claimed but its "Date Opened or Closed" cell has turned red, it is also available for you to claim (for more details see the last section of this document)
  - Claim it by entering your slack handle along with the status "Open" and today's date, for instance: 
  ```
  @khdelphine Open 1/22/2017
  ```
  
## Downloading & opening the dataset
  - Go to the URL containing the zipped dataset (provided in cell "URL from upload of zip") 
  - Download the zip file to your laptop, and unzip it.

## Checking for completeness and meaningfulness
  - Your role is to inspect the dataset and make sure that it is complete.
  - You also need to check that the dataset is *meaningful*, that is: "will the bag make sense to a scientist"? 
    - For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible for a scientist to use it.
   
## Adding missing items
  - You should add any missing file or metadata information to the dataset
  - Please refer to the [Harvesting Tookit](https://github.com/datarefugephilly/workflow/tree/FinalizeRemote-Delphine/harvesting-toolkit) for more details
 
## Re-uploading
  - If you have made any changes to the dataset, zip the all the files and upload the new resulting zip file, using the application http://drp-upload.herokuapp.com/
     - Make sure to select the name of your event in the dropdown (and "remote" if you are working remotely)
    - Note that files beyond 5 Gigs cannot be uploaded through this method
      - Please talk to your DataRescue guide/post on Slack in Checkers channel, if you have a larger file
    - The file you uploaded has now replaced the old version, and it is available at the same url (in cell "URL from upload of zip")
  - Quality assurance: 
    - To ensure that the zip file was uploaded successfully, go to the URL and download it back to your laptop. 
    - Unzip it, open it and spot check to make sure that all the files are there and seem valid.
  
## Finishing up
  - In the Uncrawlable spreadsheet, briefly describe any change you have made in cell "Any Changes?", and answer yes or no in cell "Files in  UUID.zip are all good?" 
  - In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Current Status", for instance: 
  ```
  @khdelphine Closed 1/22/2017
  ```
    - If ever a day or more passed  since you originally claimed the item, update the date to today's date. 
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, the **Date field will turn red**, signaling that someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
