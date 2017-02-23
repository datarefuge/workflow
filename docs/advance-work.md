# Organizing an Event

This document is meant for DataRescue event organizers. There are lots of ways to prepare for an event. This document highlights only the technical aspects of preparation. There are lots of logistical and other aspects to look out for as well, but this is the minimum needed to use the workflow we propose.

Note that after an event, participants might want to continue the work remotely, and our workflow is designed to make that possible.

Before starting, your team should go through the following steps.

## The Basics

- Read through the entire workflow documentation
- Sign up for the datarefuge slack and make sure there's a channel for your event
- Define your teams. They are usually: Seeders, Researchers, Harvesters, Checkers, Baggers, and Describers. Although in some cases, some of the roles can be conflated
    - In particular, we recommend that Researchers and Harvesters work very closely with each other, for instance in pairs or in small groups. In some cases, a single person might be both a Researcher and a Harvester.
    - Each team should have team leaders, aka "guides".
- The event organizers and team leaders should schedule a call with DataRefuge to go over the process.
- The event organizers and team leaders for the Seeders should also check in with EDGI folks for info about how to make sure that you're seeding and sorting effectively.

**Note that the Describers role is being redeveloped at the moment, so it is currently not enabled.**

## Primer and sub-primer documents

- Make sure your event has its designated primer and sub-primer documents
- Those are documents that will inform the work of the Seeders at your event. They will tell them which website or website sections they should be focusing on for URL discovery.
- An EDGI coordinator will setup these documents for you.

## Archivers app

- The [Archivers app](http://www.archivers.space/) enables us to collectively keep track of all the archiving work being done.
    - It will also help coordinate the work of different roles (Researchers, Harvesters, Checkers, Baggers, Describers) on each URL.
- The app will include URLs coming from two main sources:
    - URLs that were nominated by Seeders at a previous DataRescue event,
    - URLs that were identified through the Union of Concerned Scientists survey, which asked the scientific community to list the most vulnerable and important data currently on accessible through federal websites
- You need to make sure that:
    - Your event is listed in the app, talk to the DataRefuge organizers about this
    - All the event participants who need it have access to the app (see Credentials section below)

## Crawl vs. Harvest: storage location

- The main triage point of the workflow is whether a URL can be automatically crawled, for instance by the Internet Archive, or whether it needs to be manually harvested.
- The crawling process does not require any separate storage management, as the crawlable URLs are nominated to the Internet Archive, who will take care of the actual file storage after they have crawled the pages. See the [Seeders documentation](seeding.md) for more information on this process.
- The datasets harvested through the harvest process and uploaded through are the Archivers app are stored on S3 storage managed by DataRefuge.
- At this time there is no direct access to the files stored on S3 for security reason.

<!--## S3 storage
- While the file storage process is streamlined and "invisible" to the event participants, as an organizer you should still make sure that the storage has been set up properly for your event.
- Talk to the DataRefuge organizers about this.-->

<!-- - You need two S3 "buckets" (i.e., directories) for your harvested files.
- The Harvesters will upload the files they harvest to the first bucket ("pre-bag" bucket)
    - In some cases, the Checkers will also upload improved versions of the files to the same pre-bag bucket
    - The Baggers will turn those files into bags and upload the bags to the second bucket ("bag" bucket)
- A DataRefuge coordinator will set up the two S3 buckets for you
    - They will also make sure that the Uploader web applications used by Harvesters, Checkers, and Baggers "knows" about your event and has the name of your event listed as an option.
    - Most uploads to S3 will be done through the web-based Uploader application (http://drp-upload.herokuapp.com/ or http://drp-upload-bagger.herokuapp.com/). This application can handle files up to 5 Gigs.
- One person at the event should be designated as the S3 System Administrator and will have direct access to the S3 buckets for the event. The S3 Sys Admin should be someone with advanced technical skills and will be responsible for 2 things:
    - Upload very large sets (beyond 5 Gigs) through an alternate method (provided by DataRefuge)
    - Keep the buckets cleaned up and organized.
- Note that large files Uploaders need not be coders, but they should have a little experience working in command line, and computers with python 2.7.-->

## Credentials

- The Researchers/Harvesters/Checkers/Baggers need to have an account on the [Archivers app](http://www.archivers.space/)
    - You will need to generate invites for each one [within the app](http://www.archivers.space/invites/new), and paste the URL generated in a slack Direct Message or an email
    - Each participant invited will automatically "belongs" to your event in the app
- Checkers and Baggers need to be given explicit privileges in the app to have access to the Checking (i.e. "Finalize") and Bagging sections
- Seeders do not need access to the Archivers app
<!--- The Describers (Ckan/Metadata folks) need **credentials for [ckan](https://www.datarefuge.org/)**. -->
<!--- The S3 System Administrator needs credentials for s3. -->

## Other supplies

Make sure you have a few thumb drives to handle very large data sets (above 5 Gigs).

## After the event

- Participants might want to continue the work started at the event remotely
- This should be possible, as our workflow is meant to function in-person as well as remotely
