## Summary of the Code:
1. **Importing Libraries**:
The Script Starts by Importing the Necessary Libraries, Including Google Search, BeautifulSoup, Regex, and Selenium for Web Scraping.

2. **Initializing Data List**:
A List Named Data is Initialized to Store the Scraped Information.

3. **Defining Queries**:
A Set of Queries Related to Canoo (Provided in the Assignment) is Defined to Gather Information on Different Aspects.

4. **Using Google Search**:
The Script Uses the Google Search API to Obtain Search Results for Each Query.

5. **Web Scraping with Selenium**:
For Each URL Obtained from the Search Results, the Script Checks if It's Not a PDF Link. If Not, It Opens the URL in a Headless Chrome Browser Using Selenium, Waits for the Page to Load, Retrieves the Page Source, and Then Closes the Browser.

6. **Parsing with BeautifulSoup**:
The Page Source is Then Parsed Using BeautifulSoup to Extract the Text Content.

7. **Cleaning Text**:
Unnecessary Spaces in the Text are Removed Using Regex, and the Cleaned Text is Stored in the Cleaned_Text Variable.

8. **Checking Text Length**:
The Script Checks if the Length of the Cleaned Text is Greater Than or Equal to 100 Words Before Appending It to the Data List. If the Text is Too Short, It Skips the Content and Prints a Message.

9. **Saving to CSV**:
Finally, the Script Saves the Collected Data to a CSV File Named Output_Data.Csv. It Writes the Header and Rows to the File Using the Csv.DictWriter Class.

## Challenges Faced:
1) **Handling PDF Links**:
The Script Checks if a URL Ends with a PDF Extension to Avoid Scraping PDF Documents, Which Might Not Have Structured Text Content.

2) **Ensuring Page Load**:
Using Selenium, the Script Waits for the Presence of the <Body> Tag to Ensure That the Page is Fully Loaded Before Extracting Content.

3) **Checking Text Length**:
The Script Checks the Length of the Cleaned Text to Filter Out Short or Uninformative Content, Preventing the Storage of Irrelevant Data.


## Techniques Used:
1. **Web Scraping with Selenium**: Used Selenium WebDriver to Programmatically Interact with a Web Browser. This Allows You to Load Web Pages, Interact with JavaScript Elements, and Extract Dynamic Content.

2. **Headless Browser**: Utilized a Headless Chrome Browser to Run Selenium Without a Visible UI. This is Useful for Background Processes and Scraping Without Displaying the Browser.

3. **Google Search**: Employed the Googlesearch Library to Perform Google Searches Programmatically, Obtaining Search Results.

4. **HTML Parsing with BeautifulSoup**: Utilized BeautifulSoup for Parsing the HTML Content of Web Pages, Making It Easier to Extract Relevant Text and Information.

5. **Regex for Text Cleaning**: Used the Regex (Re) Library for Regular Expressions to Clean Up and Normalize Text Extracted from HTML, Removing Unnecessary Spaces.

6. **Error Handling**: Implemented Try-Except Blocks for Error Handling to Gracefully Handle Exceptions During Web Scraping.

7. **CSV File Handling**: Used the Csv Library to Write Data to a CSV File.


## Libraries Used:
1. **Googlesearch**: For Performing Google Searches.
2. **BeautifulSoup (Bs4)**: For HTML Parsing and Extraction of Relevant Text.
3. **Selenium**: For Web Scraping and Browser Automation.
4. **Regex (Re)**: For Text Cleaning Using Regular Expressions.
5. **Csv**: For Reading and Writing CSV Files.


## Summary
I Utilized Python and Various Libraries Like Googlesearch, Selenium, and BeautifulSoup to Automate Web Searches and Data Extraction. The Script Navigates Google Search Results, Uses a Headless Chrome Browser for Discrete Browsing, and Excludes PDFs and Short Content. Extracted Data is Saved in a CSV File. This Assignment Provided Me with a New and Valuable Experience, Offering Insights into Web Scraping, Automation, and Data Handling. Further Improvements Could Focus on Refining Performance, Enhancing Error Handling, and Exploring Additional Features Like User-Agent Rotation for Increased Versatility in Web Scraping Scenarios.
