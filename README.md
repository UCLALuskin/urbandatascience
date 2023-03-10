# UP229 Urban Data Science
Spring 2022: Wednesdays 9-11.50, Public Affairs 2343

**Instructor:** [Adam Millard-Ball](https://millardball.its.ucla.edu), he/him

**Teaching assistant:** Tiffany Green

**Office hours:** 
* Adam Millard-Ball: Varies, but normally Tuesdays 2-3 and Wednesdays 12-1. [Sign up here](https://goo.gl/X7vFOD)
* Tiffany Green: Fridays 2-3 on [Zoom](https://ucla.zoom.us/j/96599076393). No sign up needed.

**About this course:** New data sources are a potential goldmine for urban planners and policy makers. But sometimes they are large, sometimes they are messy, sometimes they are awkward to access, and often they are all of these things. In this hands-on course, we’ll develop skills in scraping, processing, and managing urban data, and using tools such as natural language processing, geospatial analysis, and machine learning. We’ll use examples from transit, housing, and equity planning, and build competence in open-source tools and languages such as Python and SQL. We’ll also consider the limits to data science, and the biases and pitfalls that "big data" can entail.

**Prerequisites:** Basic Python programming experience, for example through UP206A (Introduction to Geographic Information Systems and Spatial Data Science), or an introductory Python course. One good, free option is offered by [Data Carpentry](https://datacarpentry.org/python-socialsci/index.html). Another is the University of Michigan [Introduction to Data Science in Python](https://www.coursera.org/learn/python-data-analysis) course; if you have no prior knowledge, you should take [Programming for Everyone](https://www.coursera.org/learn/python) first. (You can take these for free if you choose the "audit" option.) Whichever option you choose, *before* starting this course you should be familiar with Python syntax, Jupyter notebooks, plotting via `matplotlib`, and `pandas` and `geopandas` dataframes.

## Learning objectives
* Expand your urban data analysis, visualization, and Python skills, regardless of your starting point
* Identify applications of these techniques to urban planning challenges
* Know how to read API documentation and where to get more information
* Understand how to collaborate using git and other software tools
* Critically analyze the constraints to data science methods, particularly in terms of ethics and causal inference

## Course tools
All the assignments, and lecture notebooks will be posted on this GitHub site. Readings will be on Canvas.

I ask you to do the assignments using a Jupyter Notebook in [Anconda](https://www.anaconda.com/products/individual). That helps make sure that we all have a consistent Python setup across different computers (Mac, Windows, etc.).

We will primarily use Slack to maintain communication outside of scheduled class times. In particular, it provides a space for problem solving and for you to help each other. You’ll receive an email invitation from me to join our Slack workspace. If you have not used Slack before, please familiarize yourself with the tool using the [resources here](https://www.it.ucla.edu/support-training/tutorials/how-use-slack).

## Textbook
There is no textbook for the class. All required readings will be posted here on GitHub. However, you may find some of the following books helpful.
* [Python for Data Analysis, 2nd edition](https://bookshop.org/books/python-for-data-analysis-data-wrangling-with-pandas-numpy-and-ipython-9781491957660/9781491957660). This focuses on the `pandas` library. The UCLA Library has a copy.
* [Think Python, 2nd edition](https://greenteapress.com/wp/think-python-2e/). This is a free ebook and is an excellent general refresher on Python syntax and data structures.

## Class participation
Your active participation is essential to making this course successful and enjoyable. I expect you to:

* Actively follow the examples in class through your own copy of the Jupyter notebook posted in advance. Tweak and experiment with the examples. If you don't follow an example, let me know—others will undoubtedly have the same question.
* Discuss the substantive readings on Slack. Post a question, idea, or comment by 8.30am on the day of class.  Please engage with the posts of others as well as writing your own—this is a discussion board, not a repository of essays.  
* Use Slack to help each other out with questions on the assignments and projects.

## Graded assignments
**Biweekly homeworks** (25%). You must submit at least 4 out of 5 homeworks on time (but please do them all). *We'll spend time in class on Wednesdays working through the homeworks, so please make a start on it before then.*

**Challenge problems** (25%). Most homeworks will include a challenge problem, which is more open ended. You must do at least 2 of these, and present one in class.

**Final project** (35%). Working in groups of 2-3, you'll conceptualize and implement an urban data science project. You'll submit a proposal (Week 3), and make lightening presentations of your interim (Weeks 6-7) and final analysis (Weeks 9-10).

**Class participation** (15%). Your class participation grade will consider attendance and active participation in class and on Slack.

## Course Policies

### Accessibility and Disabilities
If you require any accommodations because of a disability, please talk to me within the first two weeks of the quarter if possible. The sooner that I am aware of any accessibility needs, the quicker I can try and accommodate them.

### Late Submission of Assignments
Students can make a formal request to the instructor for special consideration
for an extension to an assignment due date. This request should be received at least 48 hours in advance. Otherwise, one partial grade will be deducted for every 24-hour period an assignment is late. For example, an A- will go to a B+. Note that no extensions are possible for the homeworks (because I post the solutions promptly)—that's why only 4 out of 5 homeworks are required.

## Academic Integrity
UCLA’s policy about plagiarism is clear: the sources of all ideas, text, pictures, or graphics that are not your (or your team’s) own must be fully cited, all passages copied from other sources must be in quotation marks with the source cited, and you absolutely cannot submit materials that have previously been submitted by other students in previous iterations of this course, even if you have re-worked this material for your submission. Being in this class constitutes an acknowledgment and willingness to abide by UCLA’s academic integrity policies. Should you have any questions about these policies, [see here](http://www.studentgroups.ucla.edu/dos/students/integrity/). (Thanks to Prof. Mike Manville for permission to use this text.)

The same principles of academic integrity apply to your code. If you borrow any code snippets or ideas, acknoweldge them with a comment in the code. E.g.

```
# Iteration code from: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
``` 

# Weekly schedule
The schedule is preliminary and subject to change, depending on how quickly or slowly we move through the material. 

Jupyter notebooks for the pre-recorded lectures and in-class assignments will be posted on GitHub. The course readings and lecture videos will all be posted on Canvas.

Pre-course:

* Please fill out the [pre-course survey](https://forms.gle/XN1mh2D6UR7kvANeA)
* Complete Module 0 on Canvas, which sets you up with [GitHub](https://github.com/) and [Anaconda](https://www.anaconda.com/products/individual)

Week 1: Introduction and APIs
* [APIs](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/3%20APIs.ipynb)
* [Getting census data](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/4%20Getting%20census%20data.ipynb)
* [The Socrata API](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/5%20The%20Socrata%20API.ipynb)
* [Class activities](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%201.ipynb) and [solutions](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%201%20solutions.ipynb)

[HW1: Due Tuesday Apr 12](https://classroom.github.com/a/d6Qhu_kb). 

Week 2: Web scraping
* [Scraping permits](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/6%20Scraping%20permits.ipynb)
* [Scraping Craigslist](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/7%20Scraping%20craigslist.ipynb)
* [Class activities](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%202.ipynb) and [solutions](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%202%20solutions.ipynb)

Week 3: Data wrangling
* [Data wrangling](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/8%20Data%20wrangling.ipynb)
* [Class activities](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%203.ipynb)

[HW2: Due Tuesday Apr 26](https://classroom.github.com/a/c4U5F6hq)
 
Week 4: Spatial joins
* [Spatial joins](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/9%20Spatial%20joins.ipynb)
* [Advanced spatial joins](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/10%20Advanced%20spatial%20joins.ipynb)
* [GTFS](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/11%20GTFS.ipynb)
* [Class activities](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/classes/Class%204.ipynb)

Week 5: Machine learning: prediction
* [Part 1: Preparation](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/12%20Classification%20part%201%20Preparation.ipynb)
* [Part 2: Random forests](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/13%20Classification%20part%202%20Random%20forests.ipynb)
* [Part 3: Neural nets](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/14%20Classification%20part%203%20Neural%20nets.ipynb)

[HW3: Due Tuesday May 10](https://classroom.github.com/a/NJt91CEo)

Week 6: Machine learning: clustering
* [Clustering](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/15%20Clustering.ipynb)
* [Spatial clusters](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/16%20Spatial%20clusters.ipynb)

Week 7: Catch up

[HW4: Due Tuesday May 24](https://classroom.github.com/a/5OEGgXfm)

Week 8: Natural language processing: parsing
* [Parsing PDFs](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/17%20Parsing%20PDFs.ipynb)
* [Parsing text](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/18%20Parsing%20text.ipynb)

Week 9: Natural language processing: topic modeling and sentiment analysis
* [Topic modeling](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/19%20Topic%20modeling.ipynb)
* [Twitter](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/20%20Twitter.ipynb)
* [Sentiment analysis](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/21%20Sentiment%20analysis.ipynb)

Week 10: Databases, big data, privacy, and ethics
* [Big data](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/22%20Big%20data.ipynb)
* [Parallel processing](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/23%20Parallelization.ipynb)
* [Databases and SQL](https://github.com/UCLALuskinDataScience/urbandatascience-s22/blob/main/Lectures/24%20Databases%20and%20SQL.ipynb)

[HW5: Due Tuesday June 7](https://classroom.github.com/a/9nXQyBOA)
