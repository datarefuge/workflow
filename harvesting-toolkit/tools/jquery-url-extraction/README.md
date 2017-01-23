# Using jQuery to extract link data

Use this approach if you have a page that you'd like to extract a list of links from a page. This can be a somewhat messy approach, but will work with pages that have content altered by javascript.

The goal of this guide is to arrive a text file, with each line containing a url to download. We'll save that file as paths.txt, and feed it to the wget-loop tool.

### Overview:

We're going to be loading [jQuery](http://api.jquery.com) into the page, using it to isolate a list of links for download. The general steps we're going to take:

1. Open the console & load jQuery
2. Use jQuery to construct a list of links in the console
3. Copy that list to a text file
4. Feed the text file to the wget-loop tool

### 1. Open the console & load jquery
Start by opening the console, it's often easiest to "inspect element" on a particular link you'd like to start with. You should see

From there, open the jquery.js file in this folder in a text editor. You'll see one very long line of code, copy that line, and paste it into the console, then hit enter. you should see "true" appear in the console, this indicates that jquery has been loaded into the page. If you get an error, make sure you've copied the entire line.

### 2. Use jQuery to construct a list of links in the console
Here's the part where you'll need to exercise a bit of judgement. We're going to build a jQuery [selection](https://learn.jquery.com/using-jquery-core/selecting-elements/) that isolates all of the links to data files on the page. Because pages use different HTML, each solution may be a bit different. As an example (and a great place to start), this command would select every link on the page:

	> $("a")

Try pasting that line into the console & hitting enter. In plain english, this command says "select every a tag on the page". The command returns a jquery *selection*, which is an array of html tags. It's worth having a look at the output, and you'll probably see a long list of tags, many of which don't link to the "data". Running a selector for every "a" (link tag) means that links for navigation, copyright links, social media links, etc.  will be included. Often it's best to scope the selection to a more relevant part of the page. In the example case, looking at the html in the inspector showed that all of the data tags were inside of a ```<div class="simpletable" >```, so we can scope the selection like this:

	> $(".simpletable a")

What this is saying is "select every a tag that is a decendant of the css class simpletable". Looking at the list, it's a neat list of all the zip files on the page.

This updated selectino is close, but what we're after is a list of urls, not a jQuery selection. Urls' are stored in an ```<a>``` tag's ```href``` attribute, so we'll have to run a few more commands to pull the urls from the selection of a tags. The first thing we'll do is declare an array that will hold our results (Copy this line into the console & hit enter):

	> var links = [];

And now we will run the selection, and for each link in the list, we'll "push" the a tag's ```href``` attribute (the url) onto the links array. Be sure to change the ```".simpletable a"``` part to match the selection you've built.

	> $(".simpletable a").each(function(){ links.push($(this).attr("href")); })


### 3. Copy that list to a text file

Now that we have a list of links, it's time to get this list out of the browser and into a text editor. If you are using using chrome, this is a one liner. Type the following into the console & hit enter:

	> copy(links)

That will copy the links array to your clipboard.

If you are using another browser, This will output a big list of all the links:

	> JSON.stringify(links)

Run that, hit enter and copy the output.

Either way, paste your hard-earned list of links into a new text file, and have a look.

The final step before running the downloading bit is to clean & inspect each link to make sure it's formatted properly. You want one url per line, with no spaces before or after, and no quotations around the url. This is where having a good text editor & a little "fing & replace" wizardry can go a long way.

Take your time assembling the list of urls. Moving slowly & thinking about each line will save headaches & broken-link-downloads later.

Now that you have a list of one url per line, the last step is to decide between *absolute* or *relative* urls

#### Absolute vs. Relative urls
In your list you may encounter links that don't have a protocol string in their name (a protocol string is the ```http://``` bit). It may look something like this:

	/electricity/data/eia412/f412sch203.xls

This is a *relative* url, meaning it's relative to the page it was loaded on. When you see links that don't have a protocol string, it is implied that the url is a path from the main one. So in our example the page we're on has this url:

	http://www.eia.gov/electricity/data/eia412/

When you click a link whose ```href``` attribute is ```/electricity/data/eia412/f412sch203.xls```, the browser generates this url:

	http://www.eia.gov/electricity/data/eia412/f412sch203.xls

*but*, if the href attribute had been this:

	electricity/data/eia412/f412sch203.xls

The browser would have generated this url:

	http://www.eia.gov/electricity/data/eia412/electricity/data/eia412/f412sch203.xls

The difference is the first ```/``` in the link's href attribute. a slash at the beginning of a link means "start with the base url and add the href" (in this case: ```http://www.eia.gov```), no slash means "add the href to the current url" (in this case, the current url is: ```http://www.eia.gov/electricity/data/eia412/```). This creates a problem for our text file, as there is no browser to do the interpretation for us, so we need to be explicit.

In your text file, you'll need to decide between absolute or relative urls. Either is fine, but **all links in the text file must be either absolute or relative**. We can't mix between them. It's easiest to just go with whichever is more prevalent in your list. If you're seeing mainly absolute urls, make them all absolute.

If you use relative urls, be sure to set the "url.txt" file to be url you'd like to add to the beginning of the list. Looking at the wget-loop download script, it shows that for each line in the paths.txt file, it adds whatever's in the url.txt file to the line. so if the url.txt file is blank, it will add nothing to the line.


### 4. Feed the text file to the wget-loop tool
The final step is to save the list of links as the "paths.txt" file to feed to the wget-loop tool, set "url.txt", and run the ./download.sh script. Check out the wget-loop readme for more into on how to use it.
