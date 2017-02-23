While DataRefuge/DataRescue strives to be a distributed effort, there is need for a certain level of coordination to make sure there is no effort duplication between events. We are not going to cover all the tasks that Coordinators tackle in this document; instead we will focus on specific tasks that will help all project participants better understand the overall workflow.

# EDGI Coordinators

[Add a paragraph on EDGI and links to other relevant documents/sites --> Could someone from EDGI please do that?]
EDGI focuses particularly on helping Seeders teams get set up. They also provide advanced recommendations and know-how on the harvesting process.

# DataRefuge Coordinators

DataRefuge Coordinators help facilitate the DataRefuge project and the development of the [DataRefuge repository](https://www.datarefuge.org/). In particular they help each DataRescue event get set up with their list of Uncrawlable URLS.

## Uncrawlable Spreadsheet structure

- While eventually we hope to be able to develop an integrated web-based application that will facilitate the entire workflow, for now we have to rely on a system based on Google Spreadsheets to manage harvesting activities.

- Uncrawlable Action spreadsheets
  - An Uncrawlable Action spreadsheets contains no more than 500 URLs
  - It is divided into tabs (one per role)
    - with formulas that help populate rows from one tab to the other
  - It contain a number of column per tab to support various aspects of the role's work
  - Each DataRescue event is attributed one separate Action spreadsheet
    - The event participants can continue working on it remotely after the event until it is completed
    - Or alternatively they could "give it back" to the organizers at the end of the event

- An Uncrawlable Index spreadsheet
  - A single Uncrawlable Index spreadsheet is used to keep track of all URLs being managed in the project
  - Using formulas, it automatically compiles a list of all URLS listed in all Uncrawlable Action spreadsheets.
  - This spreadsheet only contains minimal information about each URL (URL, UUID, Done/Not Done)
  - It is not meant to be edited in any way.
  - However its can be downloaded and imported into a tool like OpenRefine to help with deduplication.

- Seeders spreadsheet
  - The Chrome Extension used by the Seeders automatically populate a separate spreadsheet.
  - We have found that keeping that spreadsheet separate helps with the workflow

## How each Uncrawlable Action spreadsheet is populated

It will include URLs coming from two main sources:

- URLs that were nominated by Seeders at a previous DataRescue event
- URLs that were identified througth the Union of Concerned Scientists survey, which asked the scientific community to list the most vulnerable and important data currently on accessible through federal websites.

## Spreadsheet Minder

- A Spreadsheet Minder (or Spreadsheet Minder Team) is in charge with managing the Uncrawlable Index and Action spreadsheets
- Here are the task they are responsible for:
    - Prepare new Uncrawlable Action spreadsheets by moving URLs from the Seeders spreadsheet and the Survey into new Uncrawlable Action spreadsheets.
    - Generate UUIDs (see "UUID generation" below) and add them to the Uncrawlable Action spreadsheets, making sure that each URL has a UUID
    - Add a rough importance rating (in the "Importance" cell)
    - E.g., a URL coming from the Survey would automatically get a high importance rating
- Add the name of the event (in the "Event Name" cell)
- Keep an eye on all spreadsheets making sure that everything is in order.
- Regularly take snapshots of each spreadsheet in case an problem occurs and the content of a spreadsheet needs to get recovered
- Use the Index spreadsheet to track overall progress (ratio Done / Not Done) and to help with deduplication efforts

## UUID generation

- UUIDs are "universal unique IDs"
- Each URL listed in an Uncrawlable spreadsheet is assigned one UUID (in cell "UUID").
- Generating enough (UUIDs) ahead of time, and cutting and pasting them in the UUID column (in the spreadsheet's empty rows).
- The web-based tool [UUID generator](https://www.browserling.com/tools/random-uuid) can generate individual or multiple UUIDs.
