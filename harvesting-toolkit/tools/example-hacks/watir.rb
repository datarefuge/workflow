# Used to scrape https://iaspub.epa.gov/sor_internet/registry/datareg/searchandretrieve/datadictionaries/browse.do
# This is the last refuge of scraping a site as it programatically driving an instance of chrome.
# It does an action, waits for a few seconds, then dumps the html.
# 
# Colin A. Gross <grosscol@gmail.com>

require 'watir'
require 'fileutils'

# Given url and destination directory
def scrape_tables(browser, url, dest_dir)
  # create subdirectory
  FileUtils.mkdir_p dest_dir

  browser.goto url

  # Get the select_list box that shows all the data tables for the page
  sel_list = browser.select_lists.select{|list| list.id == 'tableSelect'}.first

  # For each option, render the page, output the body as a file.
  sel_list.options.each do |opt|
    sel_list.select(opt.value)
    puts "Scraping #{opt.value}" 

    # Hueristic wait time for the page to load. 
    sleep 5

    # output the body
    filename = File.join(dest_dir, "#{opt.value}.html")
    File.open(filename, 'w'){|f| f.write(browser.html)}
  end
end

jsession_id = 'rPTgmM_iWXwnGWdlphxJS1nuJBH8UvUD1lEN1ORhY9LTxHH3YMYT!-651665866'
ids = [10040, 11062, 12441, 12903, 13102, 15740, 3805, 3806, 5300, 7260, 7280, 7500, 7620, 8440, 8840, 9100, 9942]

# Open browser
browser = Watir::Browser.new :chrome

# Construct urls by string sub session_id and id
ids.each do |id| 
  puts "processing page #{id}"
  url = "https://iaspub.epa.gov/sor_internet/registry/datareg/searchandretrieve/datadictionaries/browse.do;jsessionid=#{jsession_id}?displayDetails=&id=#{id}&verNr=1.0"

  # Scrap the tables on the url into a data directory
  dest_dir = File.join('data',id.to_s)
  scrape_tables( browser, url, dest_dir )
end

browser.close

puts "done"
