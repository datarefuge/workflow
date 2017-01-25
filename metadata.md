# Describers: CKAN/Metadata

- Getting set up as a Describer
  - Ask DataRescue guide for a CKAN account
  - Log into the CKAN instance at https://www.datarefuge.org/

- Claiming a bag
  - In the "Uncrawlable" spreadsheet, locate a bag that has been uploaded and is ready for the CKAN/Metadata step
  - Such a bag would have the status "Closed" in the cell "Bagger status indicator" 
  - Claim the bag by entering your slack handle with the status "Open" and today's date in the cell "Describer status indicator" in the Describer section, for instance: 
  ```
  @khdelphine open 1/22/2017
  ```

- QA step 
  - In the "Uncrawlable Content" spreadsheet, click on URL in the "Bag URL" cell in the Bagger section.   
  - It should start downloading
  - When it is downloaded, unzip it 
  - Spot check some of the files (make sure they open and look normal, i.e., not garbled)

- Create new record in CKAN 
  - Click "Add Dataset"
  - Start entering metadata following the metadata schema spreadsheet (https://docs.google.com/spreadsheets/d/12JAleU6eF4wgu0hIlQ5efoOUCsZjT-UkRxwAofVZp6c/edit#gid=1879921913)
  - To decide what value to enter in each field:
    - Open JSON file that is in the bag you have downloaded; it contains some of the metadata you need
    - Go to the original location of the item on the federal agency website, to find more more facts about the item such as     description, title of the dataset, etc. (See "Original URL" cell in Unscrawlable spreadsheet.)
    
- Linking the CKAN record to the bag:
  - Click "Next: Add Data" at the bottom of the CKAN form
  - Click "Link" and enter the Bag URL in the text field
  - Click "Finish"
  - Test that the link you just created work by clicking it, and verifying that the file begins to download. 
    - Note that you don't need to finish downloading it again.

- Finishing up
  - Add URL to the CKAN record in cell "CKAN record URL"
    - The syntax will be "https://www.datarefuge.org//dataset/[datasetNameGeneratedByCkan]
  - In the Uncrawlable spreadsheet, change the status to "Closed" in the cell "Describer status indicator", for instance: 
  ```
  @khdelphine closed 1/22/2017
  ```

  - If ever a day or more passed since you originally claimed the item, update the date to today's date. 
      - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, someone else can claim it in your place and start working on it
        - This will avoid datasets being stuck in the middle of the workflow and not being finalized.
