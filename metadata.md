# CKAN/METADATA

- At the beginning of the session 
  - Ask the event organizer for a CKAN account
  - Log in at https://www.datarefuge.org/

- Claiming a bag
  - In the "Uncrawlable Content" spreadsheet list, locate a bag that has been uploaded and is ready for the CKAN/Metadata step
  - Claim the bag by entering your slack name in the "Ckan record created by" cell

- QA step 
  - In the "Uncrawlable Content" spreadsheet, click on S3 URL for the bag  
  - It should start downloading
  - When it is downloaded, unzip it 
  - Spot check some of the files (make sure they open and look normal, i.e., not garbled)

- Create new record in CKan 
  - Click "Add Dataset"
  - Start entering metadata following the metadata schema spreadsheet (https://docs.google.com/spreadsheets/d/12JAleU6eF4wgu0hIlQ5efoOUCsZjT-UkRxwAofVZp6c/edit#gid=1879921913)
  - To decide what value to enter in each field:
    - Open Json file that is in the bag you have downloaded; it contains some of the metadata you need
    - Go to the original location of the item (on the federal agency website), to find more more facts about the item
    
- Linking the CKAN record to the bag:
  - Click "Next: Add Data" at the bottom of the CKAN form
  - Click "Link" and enter the URL to the bag in S3
  - Click "Finish"
  - Test the link you just created by clicking it, and verifying that it is beginning to download. 
    - Note that you don't need to finish downloading it again.

- **Let everyone know you are done **

