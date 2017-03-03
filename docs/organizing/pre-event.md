Below we've outlined the critical technical considerations for planning a DataRescue event.

## Key Steps

1. **Read the [DataRescue Paths](https://docs.google.com/document/d/19A_0W1QWBgaiu42XPjMyV5BPn8Wjw4vc01v82S-uT5w/edit)** available as part of [DataRefuge's Overview](http://www.ppehlab.org/datarescueworkflow) or [EDGI's DataRescue Event Toolkit](https://envirodatagov.org/event-toolkit/).
1. **Join the [DataRefuge Slack team](https://rauchg-slackin-qonsfhhvxs.now.sh/)** and start a channel for your event.
1. **Review the [workflow documentation](https://datarefuge.github.io/workflow/)** and decide which paths your event will have.
1. **Schedule a call with DataRefuge** to:
    - review the workflow and confirm event logistics like volunteer support
    - receive access to the [Archivers app](http://www.archivers.space/) to archive complex datasets
1. **Schedule a call with EDGI** to:
    - receive training on using [Agency Primers](https://envirodatagov.org/agencyprimers/) and EDGI's [Chrome Extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok) to identify and preserve web pages on federal government web sites
    - receive an orientation on event [harvesting tools](https://github.com/edgi-govdata-archiving/harvesting-tools)

## Event Preservation Tools

### Archivers App

A DataRefuge organizer will set up your event in the app and coordinate initial account creation. The [Archivers app](http://www.archivers.space/) enables us to keep track of all the DataRescue event preservation and coordinate the work across different roles.

The app includes URLs coming from two main sources:
- URLs nominated by Seeders at previous DataRescue events
- URLs identified by a Union of Concerned Scientists survey which asked the scientific community to list the most vulnerable and important data currently accessible through federal websites.

### Agency Primers and Chrome Extension for Seeding

An EDGI coordinator will set up access to Agency Primer and Sub-primer documents as well as a seed progress spreadsheet. These documents will inform the work of the Seeders at your event. They will tell them which website or website sections they should be focusing on for URL discovery.

<div class = "note">
  <strong>Crawl vs. Harvest: Where is the Data Stored?</strong> <br />  
  The workflow is designed to triage whether a URL will be stored by the Internet Archive or in the <a href="https://www.datarefuge.org/" target="_blank">DataRefuge repository</a><!---_---> based on whether it can be automatically crawled by the Internet Archive web crawler or needs to be manually harvested.<br />
  <ul>
    <li>Nominating crawlable URLs makes use of Internet Archive's existing infrastructure. See <a href="/seeding/">Seeding</a> for more information on this process.</li>
    <li>Datasets manually harvested are uploaded through the Archivers app to an Amazon S3 storage managed by DataRefuge.</li>
  </ul>
</div>

## Permissions and Credentials

- **All** Path II Attendees need to have an account on the [Archivers app](http://www.archivers.space/).
    - You will need to generate invites for each one [within the app](http://www.archivers.space/invites/new), and paste the URL generated in a Slack Direct Message or email.
    - Each participant invited will automatically "belong" to your event in the app.
- In addition, Checkers and Baggers need to be given additional privileges in the app to access the Checking (i.e. "Finalize") and Bagging sections.

## Technical Resources

- Access to Wi-Fi
- Extra Power Strips and Extension Cords
- Backup storage (e.g., large (>16GB) thumb drives)
- Backup cloud compute resources
