# CourseGraph
This repository contains 
- utilities for collecting data from the course database `Moses` via their webpage.
- collected data for the CS BSc. and CS MSc.

I created this project to improve my understanding of the dependencies between courses.
And to make more informed course choices in the future.

# defining the course graph
The course graph is a directed graph.

Each node in the graph represents something a course can depend on, like another course or a degree.

An edge from a course node `A` to another node `B` represents a `A requires B` relation between two nodes.

A student would have to take course `B` before course `A`.

# process
For this project I followed the following steps:
1. collecting course descriptions
2. translating course requirements into edges
3. visualizing the course graph

# Challenges

### collecting course descriptions
From the `442` course I planed to scrape `47` failed due to variations in the HTML structure.
The list of missing courses can be found at `./Inforamtik/24_8_30/missing_hrefs.csv`.


The following data points are collected either as unstructed text or html tabels for each scraped course:
- url, title, id, responsible person, validity, default language
- content, learning outcomes, registration precedure, requirements
- duration, max num participants, exam type, credis, is graded
- faculty, institute, related programs


Data points are either collected directly or together with their description. 
By checking for the description content it can be ensured that indeed the right data has been scraped.


This is usefull because it can be automated.

**Only** the requirement and title field have been verified.


### translating course requirements into edges
The requirements fields contain unstructed text describing the requirements of a course.


For determing course dependencies I follwed the following procedure:
- precise requirements are prefered over unprecises, since it signals some importance.
- I try to map vague terms to dependencies by using context and my experience.
- If I can't a vague term it will be ignored.

This ensures that arbitrariness is reduced at labelling time.


However the following issues still hold:
- Course requirements section could be outdated.
- Author's could over or under estimate their course requirements. 
- Author's use vague terms to describe their course requirements.
- Missinterpretation on my side.
- Since I'm using my experience for determing requirements the results are biased and limited to my experience.
 
The labelling took me around two days.

You are welcome to contribute to the labels.
This could reduce the amount of missinterpretations, limitations according to experience and result in a less biased data set.

The guessed dependencies can be found at `./Informatik/24_8_31/graph.json`.


# Results

Here are the results visulized as a tag cloud. 
A node is weighted by the amount of other nodes requiring this node.

I used the open source software `gephi` for this visualization. 

top requiered modules:
![top_required_modules](https://github.com/user-attachments/assets/aacfaa38-56a2-4310-be54-b38ea2a8a09d)

all modules:
![required_modules](https://github.com/user-attachments/assets/dc825915-2c1f-43c6-be2b-c6ba5fc875c8)


# Scripts
In `./scripts` are all utilty scripts.
- `scrape_moses.py` is the webscraping script
- `print_module_hrefs.js` allows the collection of course urls. 

Both scripts contain detailed comments.

# Ethics
Webscraping should affect the quality of service for other users.
A custom request scheduler allowed to distribute all requests over a longer periode of time and preventing sudden request spikes.

Further the collected data is already publicly available.
Therefore nobody is harmed by providing access to a snapshot.


# Example Labels

Example 1:
Course: Hardware Security Lab
```
Desirable prerequisites for participation in the courses:
Prerequisites:
- Compulsory modules of the Bachelor degree.
- Experience with C programming
Recommended additional skills:
- Familiarity with HDL and logic design
- Familiarity with electronics
- Familiarity with test and measurement equipment

For the practical course students will be provided access to workstations as well as test and measurement equipment used for the course.
```
Guess: `Einführung in die Programmierung;Grundlagen der Elektrotechnik (GLET);Digitale Systeme;`

Example 2:
Course: SIP - Stereo Image Processing
```
Desirable prerequisites for participation in the courses:
Recommended: Fundamentals of vector and matrix algebra
```
Guess: `Analysis I und Lineare Algebra für Ingenieurwissenschaften;`

Example 3:
Course: MTV Project: Research at Work
```
Wünschenswerte Voraussetzungen für die Teilnahme an den Lehrveranstaltungen:
Inhaltlich werden fundierte (wenngleich nicht alle) Kenntnisse aus den Modulen 
- Formale Sprachen und Automaten
- Diskrete Strukturen
- Berechenbarkeit und Komplexität
- Logik
- Reaktive Systeme
des Bachelor Informatik der TU Berlin vorausgesetzt.
Kenntnisse aus den Mastermodulen des FG MTV sind vorteilhaft, je nach Forschungsgegenstand. 
Gute Englisch-Kenntnisse sind absolut notwendig.
```
Guess: `Formale Sprachen und Automaten;Diskrete Strukturen;Berechenbarkeit und Komplexität;Logik;Reaktive Systeme;`
