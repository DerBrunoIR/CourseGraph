# CourseGraph
This repository contains utilities for scraping the module database `Moses` from the technical university Berlin and collected data for the programs CS BSc. and CS MSc.

I created this project to improve my understanding of the dependencies between courses.

# defining the course graph
The course graph is a directed graph.

Each node in the graph represents a single course.

An edge from `A` to `B` represents a `A requires B` relation between two courses.

# process
For this project I followed the following steps:
1. collecting course descriptions
2. translating course requirements into edges
3. visualizing the course graph

# Challenges

## collecting course descriptions
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
**Only** the requirement and title field has been verified until now.

## translating course requirements into edges
The requirements fields contains unstructed text describing the requirements of a course.

For determing course dependencies I follwed the following procedure:
- If the author differentiates between `required` and `recommended`, then only take the `required` ones.
- Vague or unprecise requirements that are hard to understand are ignored.

This ensures that arbitrariness is reduced while guessing dependencies.

However the following issues still stand:
- Course requirements section could be outdated.
- Author's could over or under estimate their course requirements. 
- Author's use vague terms to describe their course requirements.
- Missinterpretation on my side.

The guessed dependencies can be found in `./Informatik/24_8_31/graph.json`.

### Examples Guesses

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



  

1. heterogenous course descriptions.
  - The scraping failed for `47` out of `442` courses due to variations in the html structure.
  - The requirements section in a course description is a free text field.
    Therefore it required manual labour to extract all the dependencies for a given course.
    Further are course descriptions sometimes vague or require specific skills no course offers.
    In such cases I tried to guess the dependencies.

    Example 1:
    ``
    ``

    Example 2:
    ``
    ``


# Results

top requiered modules:
![top_required_modules](https://github.com/user-attachments/assets/aacfaa38-56a2-4310-be54-b38ea2a8a09d)

all modules:
![required_modules](https://github.com/user-attachments/assets/dc825915-2c1f-43c6-be2b-c6ba5fc875c8)
