The [Archivers.space](https://www.archivers.space/) application is extremely fresh, we have some known issues and workarounds documented below.

## 1) I'm looking at a URL, but I can't edit anything!

Make sure you have clicked the big blue button "**Checkout this URL**" near the top. None of the fields can be edited until the URL is checked out.

## 2) Why are URLs that may have already been archived by Ann Arbor available to research?

When selecting a URL to review "`0`" is the *default* priority; it generally means that no-one has reviewed it *UNLESS* it says `MAY HAVE BEEN HARVESTED AT ANN ARBOR`.

In those cases, assign the priority to "`1`", so the URL drops down in the queue and then *SKIP IT*.

## 3) What does it mean if it says _Crawled by Internet Archive_: Yes?

"_Crawled by Internet Archive_" means the *page itself* was crawled; it may or may not mean the *dataset* was crawled.

Based on what Heretrix [Can and Can't Crawl](https://edgi-govdata-archiving.github.io/guides/internet-archive-crawler/), you will need to judge whether the dataset will be captured by the Internet Archive crawl and use your best judgement about whether to mark as `Do not harvest`.

## 4) How should I handle overly broad sites with just a search form, e.g. noaa.gov?

In cases like [**noaa.gov**](http://www.noaa.gov/), you have to investigate  and try to find the data source a page is referencing and whether or not there is some way to query that data.
In many cases, it might be difficult or near impossible to isolate and query, depending on the kind of database.

Complete the **Research** section to the best of your abilities, especially the _Recommended Approach for Harvesting Data_.

## 5) Do we have a scripting system set up preserving data or data endpoints that are updated regularly?

Not yet; addressing these datasets is a goal going-forward.

Currently, indicate in the notes in both the **Research** and **Harvest** sections that the dataset is updated regularly, and mark it complete anyway (note decision per @mattprice/this FAQ).

## 6) What if I have a site and want to know if it has been crawled already?

Internet Archive has both a [Wayback Machine Chrome Extension](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak) and [APIs](https://archive.org/help/wayback_api.php) you can use to check if something has been archived:

- [**Wayback Machine Chrome Extension**](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  - You can also check on the Internet Archive site directly at [archive.org/web/](https://archive.org/web/)
- [**Wayback CDX Server API**](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server)

There is a `check-ia` script in the [harvesting tools](https://github.com/edgi-govdata-archiving/harvesting-tools/tree/master/url-check) for batch URLs.

## 7) What if the site has in fact been crawled well by the Internet Archive?

If the site includes only crawlable data, then there is no need to harvest it. These should be marked `Do not harvest` in the **Research** phase.

If the site includes one of the forms of uncrawlable content:  
1) FTP  
2) Many Files  
3) Database  
4) Visualization/Interactive  

Then mark accordingly in and harvest the datasets.

## 8) What does it mean when it says "checking out this url will unlock url: xxx"?

That means you have another URL checked out. In order to avoid an overlap in efforts, when you check out a URL only you can work on it. By checking out a new URL the previous one will be unlocked.

## 9) What do I do when there is stuff listed in the Link URL section?

If there are a bunch of sub-sites listed that are **not** links, then you are on the master entry; the child entries are therefore just advisory and you should try to make sure that your harvesting includes all of the datasets contained across them, but otherwise keep going.

If the Link URL section has a single URL listed and it's a link, you are on a child item, which is the wrong place. Click the link and work on the master record.

## 10) How do I partition large "parent" URLs (e.g., to reduce the size of the download < 5 GB)?

From the [overview pane](https://www.archivers.space/urls?phase=research), click `Add Url` on the top right side of app. Add a URL for each child and enter a description indicating these new URLs are children to the "parent URL". Make sure the priority of each child is the same as the parent.

Check out the parent URL, and under **Research** use "Link Url" link it to all of its children and add a description. Make sure the priority of each child is the same as the parent. Start harvesting each child.

## 11) Wifi is kind of Slow, are there workarounds for a faster connection?

1. Do as much of the work as possible remotely: spin up a VM (e.g., AWS EC2, Digital Ocean droplet) or something, `ssh` to those machines and do the downloading to there. The fewer people that are using the bandwidth onsite for big things, the less congestion this network will have.

2. Tether your phone :), thought if you do be mindful of bandwidth caps and don't forget to plug in your charger!

## 12) Why can't I edit the harvesting section?

Archivers is set up such that each URL moves through the stages of the workflow in sequence. In order to edit the **Harvesting** section, you will first need to mark **Research** as complete. Look for the checkbox on the right-hand side at the top of the **Research** section. Once you've checked it, make sure to hit `Save`.

## 13) When harvesting, why doesn't clicking on the `Download Zipstarter` button work?

Unfortunately this is a known issue. Make sure you've marked **Research** complete. Try reloading the page, or switching browsers if you can.

The App is not compatible with Safari.

## 14) In the **Research** section, what are all the checkboxes for?

Please read the DataRescue Workflow documentation for more info!

## 15) I have a process improvement that would make this go better!

Great! Open an issue in the [archivers.space GitHub repository](https://github.com/edgi-govdata-archiving/archivers.space/), or report it in the appropriate channel in your Slack team.

## 16) How do I add a new event?

Admins can add events under the "Events" tab. Regular users will have to ask an admin for help!

## 17) What is the difference between Crawlable and Harvested?

[Researchers](researching.md) investigate whether URLs listed in the [Archivers app](http://www.archivers.space/urls) need to be manually downloaded (harvested) or if they can be automatically saved (crawled) by the Internet Archive. The URLs listed as [Crawlable](http://www.archivers.space/urls?phase=crawlable) were determined as such during that research phase and are submitted to the Internet Archive, they do not need to be harvested. 

These URLs represent only a small portion of those submitted to the Internet Archive from DataRescue events. Most crawlable URLs are identified by [Seeders](seeding.md) at the beginning of the workflow and completely bypass the Archivers app.
