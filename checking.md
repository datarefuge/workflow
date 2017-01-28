

# Checkers

- Getting set up as a Checker
  - Talk to your DataRescue guide to make sure you can become a Checker.
    - In general, Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.
  - Get set up with the application http://drp-upload-checker.herokuapp.com
    - Credentials and other details will be provided by the organizers.
  - Contact your DataRescue guide, if you need any assistance.

- Claiming a dataset for the checking step 
  - You will work on datasets that were harvested by Harvesters. 
  - Go to the Uncrawlable spreadsheet, and look for a dataset that has the status "Harvester status indicator" = Closed
  - Claim it by entering your slack handle with the status "Open" and today's date in the cell "Checker status indicator" in Checker section, for instance: 
  ```
  @khdelphine open 1/22/2017
  ```
  
- Downloading & opening the dataset
  - Go to the URL containing the zipped dataset (in cell "URL from upload of zip", in the Harvester section) 
  - Download the zip file to your laptop, and unzip it.

- Checking for completeness and meaningfulness
  - Your role is to inspect the dataset and make sure that it is complete.
  - You also need to check that the dataset is *meaningful* 
    - This is: "will the bag make sense to a scientist"? 
    - For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible to a scientist to use it.
   
- Adding missing items
  - You should add any missing file or metadata information to the dataset
  - Please refer to the [Harvesting Tookit](https://github.com/datarefugephilly/workflow/tree/FinalizeRemote-Delphine/harvesting-toolkit) for more details
 
- Re-uploading
  - If you have made any changes to the dataset, zip the all the files and re-upload the resulting single zip file, using the application http://drp-upload.herokuapp.com/
    - Make sure to select the name of your event in the dropdown (and "remote" if you are working remotely)
    -  Note that files beyond 5 Gigs cannot be uploaded through this method
      - Please talk to your DataRescue guide, if you have a larger file
  - Quality assurance: 
    - To ensure that the zip file was uploaded successfully, go to the URL and download it back to your laptop. 
    - Unzip it, open it and spot check to make sure that all the files are there and seem valid.
  
- Finishing up
  - In the Uncrawlable spreadsheet, briefly describe any change you have made in cell "Any Changes?" in Checker section
  - In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Checker status indicator", for instance: 
  ```
  @khdelphine closed 1/22/2017
  ```
    - If ever a day or more passed  since you originally claimed the item, update the date to today's date. 
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
