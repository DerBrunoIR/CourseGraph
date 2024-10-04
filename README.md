# Introduction
This repository contains 
- utilities for collecting data from the course database `Moses` (TU Berlin) via their webpage.
- collected data for the CS BSc. and CS MSc.

I created this project to improve my understanding of the dependencies between courses.
And to make more informed course choices in the future.

# Content
- [defining the course graph](#defining-the-course-graph)
- [process](#process)
- [Challenges](#challenges)
  - [collecting course descriptions](#collecting-course-descriptions)
  - [translating course requirements into edges](#translating-course-requirements-into-edges)
- [Results](#results)
  - [top requiered modules:](#top-requiered-modules)
  - [all modules](#all-modules)
- [Scripts](#scripts)
- [Ethics](#ethics)
- [Example Labels](#example-labels)
  - [Example 1](#example-1)
  - [Example 2](#example-2)
  - [Example 3](#example-3)
- [course ranking](#course-ranking)

<!-- TOC end -->



<!-- TOC --><a name="defining-the-course-graph"></a>
# defining the course graph
The course graph is a directed graph.

Each node in the graph represents something *a course can depend on*, like another *course* or a *degree*.

An edge from a course node **A** to another node **B** represents a **A requires B** relation between these two nodes.

E.g. A student would have to complete **B** before taking course **A**.

<!-- TOC --><a name="process"></a>
# process
For this project I followed the following steps:
1. collect course descriptions
2. translate course requirements into edges
3. visualiz the course graph

<!-- TOC --><a name="challenges"></a>
# Challenges

<!-- TOC --><a name="collecting-course-descriptions"></a>
### collecting course descriptions
From the `442` course I planed to scrape, `47` failed due to variations in the HTML structure.
The list of missing courses can be found at `./Inforamtik/24_8_30/missing_hrefs.csv`.


The following data points are collected either as *unstructed text* or *raw html tabels* for each scraped course:
- `url, title, id, responsible person, validity, default language`
- `content, learning outcomes, registration precedure, requirements`
- `duration, max num participants, exam type, credis, is graded`
- `faculty, institute, related programs`


Data points are either collected *directly* or together with their *description*. 

By checking for these descriptions, it can be ensured that the css selectors matched the right HTML.

This can also be performed automated.

However until now **only** the `requirement` and `title` fields have been verified.

The raw module data can be found here `./Inforamtik/24_8_30/modules.json`.


<!-- TOC --><a name="translating-course-requirements-into-edges"></a>
### translating course requirements into edges
The requirements fields contain unstructed text describing the requirements of a course.

For determing course dependencies I follwed the following procedure:

- precise requirements are prefered over unprecises, since it signals some importance.

- I try to map vague terms to dependencies by using context and my experience.

- If I can't interpret a vague term it will be ignored.

This ensures that arbitrariness is reduced at labelling time.


However the following issues still hold:
- Course requirements section could be outdated.
- Author's could over or under estimate their course requirements. 
- Author's use vague or ambiguous terms to describe their course requirements.
- Missinterpretation on my side.
- Since I'm using my experience for determing requirements the results are biased and limited to my experience.
 
Nevertheless labelling took me around two days.

You are welcome to contribute to the labels.
This could reduce the amount of missinterpretations, limitations according to my experience and result in a less biased data set.

The guessed dependencies can be found at `./Informatik/24_8_31/graph.json`.


<!-- TOC --><a name="results"></a>
# Results

Here is the resulting graph visulized as a tag cloud. 
A node is weighted by the *amount of other nodes requiring this node*.

I used the open source software `gephi` for this visualization. 

<!-- TOC --><a name="top-requiered-modules"></a>
### top requiered modules:
![top_required_modules](https://github.com/user-attachments/assets/aacfaa38-56a2-4310-be54-b38ea2a8a09d)

As we can see, there are courses that are more required than other courses.

<!-- TOC --><a name="all-modules"></a>
### all modules:
![required_modules](https://github.com/user-attachments/assets/dc825915-2c1f-43c6-be2b-c6ba5fc875c8)


<!-- TOC --><a name="scripts"></a>
# Scripts
At `./scripts` are all utilty scripts located.
- `scrape_moses.py` is the webscraping script
- `print_module_hrefs.js` allows the collection of course urls. 

Both scripts contain detailed descriptions.

<!-- TOC --><a name="ethics"></a>
# Ethics
Webscraping should **not** affect the quality of service for other users.
A custom request scheduler allowed a even distribute of all requests and thus preventing sudden request spikes.

Further the collected data is already publicly available.
Therefore nobody is harmed by providing access to a snapshot.

<!-- TOC --><a name="example-labels"></a>
# Example Labels

<!-- TOC --><a name="example-1"></a>
### Example 1:

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
Dependencies: `Einführung in die Programmierung;Grundlagen der Elektrotechnik (GLET);Digitale Systeme;`


<!-- TOC --><a name="example-2"></a>
### Example 2:

Course: SIP - Stereo Image Processing
```
Desirable prerequisites for participation in the courses:
Recommended: Fundamentals of vector and matrix algebra
```

Guess: `Analysis I und Lineare Algebra für Ingenieurwissenschaften;`


<!-- TOC --><a name="example-3"></a>
### Example 3:

Dependencies: MTV Project: Research at Work
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

Dependencies: `Formale Sprachen und Automaten;Diskrete Strukturen;Berechenbarkeit und Komplexität;Logik;Reaktive Systeme;`


<!-- TOC --><a name="course-ranking"></a>
# course ranking
```
indegree = number of requirements from other nodes
outdegree = number of requirements this node makes
```
|Id                                                                                             |indegree|outdegree|Degree|
|-----------------------------------------------------------------------------------------------|--------|---------|------|
|Analysis I und Lineare Algebra für Ingenieurwissenschaften                                     |46      |0        |46    |
|Algorithmen und Datenstrukturen                                                                |34      |1        |35    |
|Stochastik für Informatik                                                                      |27      |1        |28    |
|Rechnernetze und Verteilte Systeme                                                             |27      |3        |30    |
|Bachelor                                                                                       |27      |0        |27    |
|Machine Learning 1                                                                             |23      |2        |25    |
|Systemprogrammierung                                                                           |20      |1        |21    |
|Network Architectures - Basics                                                                 |19      |2        |21    |
|Einführung in die Programmierung                                                               |18      |0        |18    |
|Rechnerorganisation                                                                            |18      |0        |18    |
|Softwaretechnik und Programmierparadigmen                                                      |18      |2        |20    |
|Diskrete Strukturen                                                                            |16      |2        |18    |
|Logik                                                                                          |13      |2        |15    |
|Formale Sprachen und Automaten                                                                 |12      |0        |12    |
|Berechenbarkeit und Komplexität                                                                |12      |1        |13    |
|Signale und Systeme                                                                            |11      |0        |11    |
|Informationssysteme und Datenanalyse                                                           |11      |0        |11    |
|Machine Intelligence I                                                                         |11      |2        |13    |
|Verteilte Systeme                                                                              |8       |2        |10    |
|Wissenschaftliches Rechnen                                                                     |7       |1        |8     |
|Robotics                                                                                       |7       |1        |8     |
|DMH Data Management on Modern Hardware                                                         |6       |3        |9     |
|DBPRA Datenbankpraktikum                                                                       |6       |1        |7     |
|Kommunikationsnetze                                                                            |6       |1        |7     |
|Rechnernetze und Verteile Systeme                                                              |6       |0        |6     |
|Digital Image Processing                                                                       |6       |0        |6     |
|Analysis II                                                                                    |5       |0        |5     |
|DBT Database Technology                                                                        |5       |2        |7     |
|Lichttechnik: Grundlagen und Anwendungen                                                       |5       |0        |5     |
|Einführung in die Lichttechnik                                                                 |5       |0        |5     |
|Algorithmentheorie                                                                             |5       |2        |7     |
|Cloud Computing                                                                                |5       |1        |6     |
|Integraltransformationen und partielle Differentialgleichungen für Ingenieurwissenschaften     |5       |0        |5     |
|Webtechnologien                                                                                |4       |1        |5     |
|Verteile Systeme                                                                               |4       |0        |4     |
|Digitale Systeme                                                                               |4       |0        |4     |
|Analysis II für Ingenieurwissenschaften                                                        |4       |0        |4     |
|Computer Graphics I (Fundamentals)                                                             |4       |1        |5     |
|Grundlagen der Rechnersicherheit                                                               |4       |3        |7     |
|Einführung in die Lineare und Kombinatorische Optimierung (ADM I)                              |3       |0        |3     |
|Grundlagen der Elektrotechnik (GLET)                                                           |3       |0        |3     |
|Nachrichtenübertragung                                                                         |3       |0        |3     |
|Mikroprozessortechnik                                                                          |3       |0        |3     |
|Automatic Image Analysis                                                                       |3       |1        |4     |
|Photogrammetric Computer Vision                                                                |3       |1        |4     |
|Anwendungssysteme                                                                              |3       |0        |3     |
|Applied Computer Vision                                                                        |3       |0        |3     |
|Machine Learning for Computer Security                                                         |3       |0        |3     |
|Adversarial Machine Learning                                                                   |3       |1        |4     |
|Numerische Lineare Algebra I                                                                   |2       |0        |2     |
|Numerische Lineare Algebra II                                                                  |2       |0        |2     |
|MDS Management of Data Streams                                                                 |2       |1        |3     |
|Quality Assurance of Embedded Systems                                                          |2       |1        |3     |
|Advanced Algorithmics                                                                          |2       |2        |4     |
|Reaktive Systeme                                                                               |2       |3        |5     |
|Architektur Eingebetteter Systeme                                                              |2       |5        |7     |
|Analog- und Digitalelektronik                                                                  |2       |0        |2     |
|Digitale Nachrichtenübertragung                                                                |2       |2        |4     |
|Foundations of Stochastic Processes                                                            |2       |3        |5     |
|Analysis und Lineare Algebra für Ingenieurwissenschaften                                       |2       |0        |2     |
|Kognitive Algorithmen                                                                          |2       |1        |3     |
|Machine Learning 2                                                                             |2       |3        |5     |
|Energiespeichertechnologien                                                                    |2       |0        |2     |
|Grundlagen Batterietechnik                                                                     |2       |0        |2     |
|Informatik Propädeutikum                                                                       |2       |0        |2     |
|Deep Learning 1                                                                                |2       |3        |5     |
|Applied Machine Learning in Engineering                                                        |2       |0        |2     |
|Privacy Engineering                                                                            |2       |0        |2     |
|Technische Akustik I                                                                           |1       |0        |1     |
|Schallmesstechnik und Signalverarbeitung                                                       |1       |0        |1     |
|Diskrete Optimierung (ADM II)                                                                  |1       |6        |7     |
|Analysis I                                                                                     |1       |0        |1     |
|Analysis III                                                                                   |1       |0        |1     |
|Approximationsalgorithmen (ADM III)                                                            |1       |1        |2     |
|Brain-Computer Interfacing                                                                     |1       |2        |3     |
|Analysis and Optimization of Embedded Systems                                                  |1       |0        |1     |
|Robotics: Fundamentals                                                                         |1       |1        |2     |
|Regelungstechnik                                                                               |1       |0        |1     |
|Continuous Software Engineering                                                                |1       |1        |2     |
|Elektronik und Signalverarbeitung                                                              |1       |3        |4     |
|Projekt Elektronik                                                                             |1       |0        |1     |
|Quellencodierung - Multimediasignalverarbeitung                                                |1       |2        |3     |
|Grundlagen der Reglungstechnik                                                                 |1       |0        |1     |
|Grundlagen der Batterietechnik                                                                 |1       |0        |1     |
|Compiler Design                                                                                |1       |2        |3     |
|Advanced Computer Architecture                                                                 |1       |1        |2     |
|Hardwarepraktikum                                                                              |1       |0        |1     |
|Programmierpraktikum: Algorithm Engineering                                                    |1       |2        |3     |
|Parameterized Algorithmics                                                                     |1       |1        |2     |
|Randomized Algorithmics                                                                        |1       |1        |2     |
|Computational Complexity                                                                       |1       |2        |3     |
|Rechnernetze                                                                                   |1       |0        |1     |
|DBPRO - Datenbankprojekt (benotet)                                                             |1       |1        |2     |
|Software Engineering cyber-physischer Systeme                                                  |1       |4        |5     |
|Software Engineering Eingebetteter Systeme                                                     |1       |0        |1     |
|Microwave and Radar Remote Sensing                                                             |1       |0        |1     |
|Künstliche Intelligenz: Grundlagen und Anwendungen                                             |1       |3        |4     |
|Berechenbarkeit und Komplexitätstheorie                                                        |1       |0        |1     |
|Logiken und Kalkühle                                                                           |1       |0        |1     |
|Machine Intelligence II                                                                        |1       |3        |4     |
|Machine Learning I                                                                             |1       |0        |1     |
|Lab Course Machine Learning                                                                    |1       |0        |1     |
|Foundations of Datascience                                                                     |1       |0        |1     |
|Schaltungstechnik                                                                              |1       |0        |1     |
|Signalverarbeitung                                                                             |1       |0        |1     |
|Secure Cryptography                                                                            |1       |2        |3     |
|Elektrische Netzwerke                                                                          |1       |0        |1     |
|Grundlagen der elektronischen Messtechnik                                                      |1       |0        |1     |
|5G / 6G Software Networks                                                                      |1       |0        |1     |
|Advanced Analog Integrated Circuits and Systems (AAIC) (12LP)                                  |1       |0        |1     |
|Analog Integrated Circuits (AIC)                                                               |1       |0        |1     |
|Analysis I und Lineare Algebra                                                                 |1       |0        |1     |
|Fog Computing                                                                                  |1       |4        |5     |
|Einfühung in die Informatik                                                                    |1       |0        |1     |
|reaktive Systeme                                                                               |1       |0        |1     |
|Singale und Systeme                                                                            |1       |0        |1     |
|Cloud Service Benchmarking                                                                     |1       |4        |5     |
|Rechnernezte und Verteilte Systeme                                                             |1       |0        |1     |
|Informatik und Gesllschaft                                                                     |1       |0        |1     |
|Architecture of Machine Learning Systems                                                       |1       |3        |4     |
|Machine Intelligence 1                                                                         |1       |0        |1     |
|Stochastik für Ingenieurwissenschaften                                                         |1       |0        |1     |
|Foundations of Data Science                                                                    |1       |0        |1     |
|Machine Learning and Data Management Systems                                                   |1       |5        |6     |
|Architektur von Anwendungssystemen                                                             |1       |0        |1     |
|Psychologie für Ingenieure und Ingenieurinnen                                                  |1       |0        |1     |
|Matrix Theory (10LP)                                                                           |1       |0        |1     |
|Theoretische Akustik / Virtuelle Akustik                                                       |0       |3        |3     |
|Computational Mixed Integer Programming (ADM III)                                              |0       |2        |2     |
|IMSEM Seminar on Hot Topics in Information Management                                          |0       |3        |3     |
|Project: Brain-Computer Interfacing                                                            |0       |1        |1     |
|Master Project Software Engineering of Embedded Systems                                        |0       |2        |2     |
|Robotics: Current Topics                                                                       |0       |1        |1     |
|IT Operations                                                                                  |0       |1        |1     |
|Logische Methoden der Informatik                                                               |0       |1        |1     |
|Master Seminar: Operating Complex IT Systems                                                   |0       |1        |1     |
|DBTLAB Database Technology Lab                                                                 |0       |3        |3     |
|Praktikum: Intelligente Softwaresysteme                                                        |0       |1        |1     |
|Image and Video Coding                                                                         |0       |1        |1     |
|Angewandte Logiken                                                                             |0       |1        |1     |
|Systemidentifikation und Regelung in der Medizin                                               |0       |1        |1     |
|Models of Higher Brain Functions                                                               |0       |2        |2     |
|Cloud Native Architecture and Engineering                                                      |0       |2        |2     |
|Hot Topics in Information Systems Engineering                                                  |0       |2        |2     |
|VS - View Synthesis                                                                            |0       |1        |1     |
|Hardware Security Lab                                                                          |0       |3        |3     |
|SIP - Stereo Image Processing                                                                  |0       |1        |1     |
|Current Topics in Computational Neuroscience                                                   |0       |2        |2     |
|Programmierpraktikum: Skalierbare Systeme                                                      |0       |1        |1     |
|Aktuelle Themen zu eingebetteten Systemen                                                      |0       |2        |2     |
|Programmierpraktikum Kommunikationstechnologien                                                |0       |1        |1     |
|Hot Topics in Communication Systems                                                            |0       |1        |1     |
|Projekt Nachrichtenübertragung                                                                 |0       |2        |2     |
|Digitale Nachrichtenübertragung - Vertiefung                                                   |0       |1        |1     |
|Entwicklung verteilter eingebetteter Systeme                                                   |0       |1        |1     |
|Multivariable Control Systems                                                                  |0       |1        |1     |
|Nonlinear Control Systems                                                                      |0       |1        |1     |
|Seminar Aktuelle Forschung an Batterien                                                        |0       |1        |1     |
|Projekt Advanced Web Technologies                                                              |0       |1        |1     |
|Angewandte Lichttechnik                                                                        |0       |2        |2     |
|Solarstrahlung                                                                                 |0       |2        |2     |
|Wireless Networking Technologies                                                               |0       |1        |1     |
|Programmierpraktikum: Cyber-Physical Systems                                                   |0       |1        |1     |
|Networked Embedded Systems                                                                     |0       |1        |1     |
|Applications of Robotics and Autonomous Systems                                                |0       |1        |1     |
|AES Bachelor-Projekt                                                                           |0       |3        |3     |
|Agent Competition: RoboCup                                                                     |0       |1        |1     |
|Agententechnologien: Grundlagen und Anwendungen                                                |0       |2        |2     |
|Aktuelle Themen der Algorithmik                                                                |0       |3        |3     |
|Algebraic Process Calculi                                                                      |0       |4        |4     |
|Algorithm Engineering II                                                                       |0       |5        |5     |
|Algorithmic Research in Teams                                                                  |0       |5        |5     |
|Applied Embedded Systems Project                                                               |0       |1        |1     |
|Bachelor Seminar: Operating Complex IT-Systems                                                 |0       |6        |6     |
|BDASEM Big Data Analytics Seminar                                                              |0       |3        |3     |
|Betriebssystempraktikum                                                                        |0       |3        |3     |
|Computer Arithmetic: Circuit Perspective                                                       |0       |2        |2     |
|Computer Graphics Project                                                                      |0       |3        |3     |
|Computer Graphics II (Geometric Modeling)                                                      |0       |3        |3     |
|Computer Graphics Seminar A                                                                    |0       |4        |4     |
|Computer Graphics Seminar B                                                                    |0       |4        |4     |
|DW Data Warehousing and Business Intelligence                                                  |0       |2        |2     |
|DBSEM - Seminar on Advanced Topics in Database and Information Systems                         |0       |2        |2     |
|Introduction into Interactive Theorem Proving                                                  |0       |2        |2     |
|Dependable Embedded Systems                                                                    |0       |1        |1     |
|Embedded Systems Security Lab                                                                  |0       |3        |3     |
|Entwurf eingebetteter Systeme                                                                  |0       |2        |2     |
|Seminar Hot Topics in Computer Vision                                                          |0       |4        |4     |
|BDSPRO Big Data Systems Project                                                                |0       |9        |9     |
|Brain-Computer Interfacing (basic)                                                             |0       |2        |2     |
|Künstliche Intelligenz: Grundlagen, Anwendungen und Seminar                                    |0       |3        |3     |
|Lichtquellen                                                                                   |0       |2        |2     |
|Lichttechnische Forschung                                                                      |0       |2        |2     |
|Licht- und Farbwahrnehmung                                                                     |0       |2        |2     |
|Logik und Komplexität                                                                          |0       |2        |2     |
|Mobile Services                                                                                |0       |2        |2     |
|Modelle zur Informationsverarbeitung im Gehirn                                                 |0       |2        |2     |
|Multicore Systems                                                                              |0       |1        |1     |
|Network Architectures - Bachelor Praxis                                                        |0       |1        |1     |
|Network Architectures - Master Project                                                         |0       |1        |1     |
|Applied Networking Lab                                                                         |0       |1        |1     |
|Network Architectures - Seminar                                                                |0       |1        |1     |
|Networked Systems Specialization (big)                                                         |0       |1        |1     |
|Networked Systems Specialization (small)                                                       |0       |1        |1     |
|Vehicular Networking and Cooperative Driving                                                   |0       |1        |1     |
|Network Architectures - Master Project (small)                                                 |0       |1        |1     |
|Optische Kommunikationstechnik                                                                 |0       |1        |1     |
|Photonische Kommunikationsnetze und Komponenten                                                |0       |1        |1     |
|Project Advanced Network Technologies                                                          |0       |2        |2     |
|DCAITI: Projekt Vertiefung vernetztes und automatisiertes Fahren                               |0       |1        |1     |
|Angewandte Netzwerktechnologien                                                                |0       |1        |1     |
|Machine Learning Project                                                                       |0       |2        |2     |
|Projekt: Symbolische Künstliche Intelligenz                                                    |0       |1        |1     |
|Current trends in graph theory and combinatorics                                               |0       |1        |1     |
|Recent Advances in Computer Architecture                                                       |0       |1        |1     |
|Research Colloquium on Algorithms and Complexity                                               |0       |1        |1     |
|Robotics: Advanced                                                                             |0       |2        |2     |
|Robotics I+II                                                                                  |0       |1        |1     |
|Robotics: Project                                                                              |0       |1        |1     |
|Data Science Project                                                                           |0       |1        |1     |
|Seminar Software and Embedded Systems Engineering                                              |0       |1        |1     |
|Signalprozessor-Projekt                                                                        |0       |5        |5     |
|Special Topics in Communications Networks and Autonomous Security                              |0       |3        |3     |
|Speech Signal Processing and Speech Technology                                                 |0       |1        |1     |
|MTV Project: Research at Work                                                                  |0       |5        |5     |
|Programmierpraktikum: Verteilte Systeme                                                        |0       |3        |3     |
|Cloud Prototyping                                                                              |0       |1        |1     |
|Seminar Energiespeichertechnik                                                                 |0       |2        |2     |
|Satellite Communication Project (SIERRA: aka. Projekt Amateurfunk)                             |0       |3        |3     |
|Grundlagen Digitaler Vernetzung                                                                |0       |2        |2     |
|Research Project Advanced Network Technologies                                                 |0       |2        |2     |
|5G Evolution / 6G Project                                                                      |0       |1        |1     |
|Models of Higher Brain Functions: Theory and Simulation                                        |0       |2        |2     |
|Models of Higher Brain Functions - Introduction                                                |0       |2        |2     |
|Aktuelle Forschung an Energiewandlern und Energiespeichern                                     |0       |2        |2     |
|Algorithmische Graphentheorie                                                                  |0       |1        |1     |
|Game Theory                                                                                    |0       |2        |2     |
|Lambda-Kalkül und Typ-Systeme                                                                  |0       |1        |1     |
|Grundlagen des Softwaretestens                                                                 |0       |1        |1     |
|Master Project and Seminar Software Engineering of Embedded Systems                            |0       |1        |1     |
|Analog Layout Design                                                                           |0       |2        |2     |
|Mathematics of Machine Learning                                                                |0       |4        |4     |
|Programmierpraktikum: Moderne verteilte Anwendungen                                            |0       |3        |3     |
|Projekt - Verteilte industrielle Steuerungssysteme                                             |0       |1        |1     |
|Algorithmics for Discrete Data Science                                                         |0       |2        |2     |
|Hot Topics in Scalable Software Systems                                                        |0       |1        |1     |
|Project Open Distributed Systems                                                               |0       |4        |4     |
|DCAITI: Vernetztes und automatisiertes Fahren                                                  |0       |1        |1     |
|DCAITI: Simulation vernetztes und automatisiertes Fahren                                       |0       |1        |1     |
|DCAITI: Projekt vernetztes und automatisiertes Fahren                                          |0       |1        |1     |
|Advanced Topics in Scalable Software Systems                                                   |0       |1        |1     |
|Multimedia and Wireless Lab                                                                    |0       |1        |1     |
|Machine Learning for Remote Sensing Data Analysis                                              |0       |2        |2     |
|Programmierpraktikum: Wettbewerbsorientierte Algorithmik                                       |0       |2        |2     |
|International Information Security Contest                                                     |0       |1        |1     |
|Programmierpraktikum: Modelle Dynamischer Systeme                                              |0       |1        |1     |
|Graph Minors                                                                                   |0       |1        |1     |
|Programmierpraktikum Batterien                                                                 |0       |1        |1     |
|Programmierpraktikum Leistungselektronik                                                       |0       |1        |1     |
|Programmierpraktikum Algorithmen und Datenstrukturen                                           |0       |2        |2     |
|Advanced Wireless Communications                                                               |0       |4        |4     |
|Information Theory and Applications                                                            |0       |1        |1     |
|Event-based Robot Vision                                                                       |0       |3        |3     |
|Ethics, data science, and networked AI                                                         |0       |1        |1     |
|MTV Seminar: Write, Review and Publish                                                         |0       |5        |5     |
|Open Distributed Systems - Seminar                                                             |0       |4        |4     |
|Bio-inspired Computer Vision                                                                   |0       |3        |3     |
|AI and Robotics: Lab Course                                                                    |0       |1        |1     |
|AI and Robotics: Research                                                                      |0       |1        |1     |
|Quantum Computing                                                                              |0       |1        |1     |
|Aktuelle Themen zu Software and Embedded Systems Engineering                                   |0       |1        |1     |
|Wireless Communication Systems                                                                 |0       |4        |4     |
|Project Computer Vision for Remote Sensing                                                     |0       |2        |2     |
|Selected Areas of Telecommunication Networks                                                   |0       |1        |1     |
|Optimization Algorithms                                                                        |0       |1        |1     |
|Learning and Intelligent Systems: Project                                                      |0       |2        |2     |
|State Estimation for Robotics                                                                  |0       |3        |3     |
|Einführung in die IT-Sicherheit                                                                |0       |7        |7     |
|Reading Group Cloud Systems                                                                    |0       |4        |4     |
|Ausgewählte Themen zu Algorithmen und Datenstrukturen                                          |0       |2        |2     |
|DCAITI: Projekt Simulation Vertiefung vernetztes und automatisiertes Fahren                    |0       |1        |1     |
|Machine Learning in Science and Industry                                                       |0       |1        |1     |
|Molecular Communications and Nanonetworks                                                      |0       |2        |2     |
|Natural Language Processing                                                                    |0       |1        |1     |
|Einführung in die Künstliche Intelligenz                                                       |0       |3        |3     |
|Motion Planning                                                                                |0       |1        |1     |
|Quantum Cryptography                                                                           |0       |2        |2     |
|Aktuelle Forschung in KI & Robotik                                                             |0       |3        |3     |
|Current Topics in Cryptocurrency and Blockchain Networks                                       |0       |2        |2     |
|Internet and Network Security                                                                  |0       |1        |1     |
|Introduction to Camera Geometry                                                                |0       |2        |2     |
|Machine Learning and Inverse Modeling in Neuroimaging                                          |0       |4        |4     |
|Quality Assurance for Machine Learning                                                         |0       |3        |3     |
|Deep Learning 2                                                                                |0       |5        |5     |
|Analyse von (Online) Social Data: methodologische Herausforderungen, soziale Folgen und Grenzen|0       |1        |1     |
|Speech and Audio Technology in Medicine                                                        |0       |1        |1     |
|Klassische Algorithmen der Computer-Graphik                                                    |0       |3        |3     |
|Large-scale Data Engineering                                                                   |0       |1        |1     |
|Programmierpraktikum: Plattformdaten und NLP                                                   |0       |2        |2     |
|Recent Trends in Deep Learning for Computer Vision                                             |0       |5        |5     |
|Seminar Large-scale Data Engineering                                                           |0       |2        |2     |
|System-on-Chip (SoC) + RISC-V Lab                                                              |0       |4        |4     |
|Applied Security Lab                                                                           |0       |3        |3     |
|Machine Learning and Security - Project                                                        |0       |2        |2     |
|Machine Learning and Security - Bachelor Seminar                                               |0       |2        |2     |
|Machine Learning and Security - Master Seminar                                                 |0       |2        |2     |
|Foundations of Statistical Inference, Detection, and Estimation                                |0       |1        |1     |
|Selected Topics in Natural Language Processing                                                 |0       |1        |1     |
|Machine Learning and Communications                                                            |0       |3        |3     |
|Data Integration and Large-scale Analysis                                                      |0       |3        |3     |
|Uncertainty in Machine Learning                                                                |0       |4        |4     |
|Topics in Biomedical Data Science                                                              |0       |2        |2     |
|Foundations of Data Literacy and Data Science                                                  |0       |1        |1     |
|Intelligent Security Lab                                                                       |0       |1        |1     |
|Grundlagen der automatischen Spracherkennung                                                   |0       |1        |1     |
|Scalable Software Systems Project                                                              |0       |2        |2     |
|Websecurity                                                                                    |0       |1        |1     |
|Algorithms for Networked Systems                                                               |0       |4        |4     |
|Advanced Topics in Networked and Distributed Systems                                           |0       |2        |2     |
|Algorithms for Distributed Systems                                                             |0       |4        |4     |
|Project Hot Topics in Computer Vision A                                                        |0       |3        |3     |
|Project Hot Topics in Computer Vision B                                                        |0       |3        |3     |
|Responsible Artificial Intelligence                                                            |0       |2        |2     |
|ROC Foundations for Graduate Research in Data Management and Machine Learning Systems          |0       |5        |5     |
|Programmierpraktikum: Datensysteme                                                             |0       |2        |2     |
|Programmierpraktikum Algorithmen für Spiele und Puzzle                                         |0       |2        |2     |
|Programmierpraktikum: Quality Data Science                                                     |0       |3        |3     |
|Machine Learning 1-X                                                                           |0       |2        |2     |
|Deep Learning 1-X                                                                              |0       |1        |1     |
|Deep Learning 2-X                                                                              |0       |3        |3     |
|Python for Machine Learning                                                                    |0       |1        |1     |
|Julia for Machine Learning                                                                     |0       |1        |1     |
|Machine Learning in Neuroscience                                                               |0       |1        |1     |
|Blockchain Prototyping                                                                         |0       |1        |1     |
|Privacy Prototyping                                                                            |0       |2        |2     |
|Advanced Cloud Prototyping                                                                     |0       |1        |1     |
|Advanced Blockchain Prototyping                                                                |0       |1        |1     |
|Advanced Privacy Prototyping                                                                   |0       |2        |2     |
|Programmierpraktikum Scalable Software Systems                                                 |0       |2        |2     |
|Multi-Robot Systems                                                                            |0       |1        |1     |
|Flying Robots                                                                                  |0       |2        |2     |
|Computational modeling - A practical course                                                    |0       |2        |2     |
|Compiling Techniques                                                                           |0       |3        |3     |
|Programmierpraktikum: Entwurf und Implementierung von Programmiersprachen                      |0       |8        |8     |
|Seminar: Aktuelle Forschungsthemen in Programmiersprachen und Compilern                        |0       |5        |5     |
|Robot Learning                                                                                 |0       |3        |3     |
|The Software Horror Picture Show                                                               |0       |1        |1     |
|Natural Language Processing in Humans and Machines                                             |0       |1        |1     |
|Workshop Machine Learning Foundations for Physicists                                           |0       |1        |1     |
|Machine Learning 2-X                                                                           |0       |4        |4     |
|Medizinische Signalverarbeitung                                                                |0       |1        |1     |
|Project Advanced Research Data Infrastructures                                                 |0       |1        |1     |
|Project Large-scale Data Engineering (benotet)                                                 |0       |1        |1     |
|Graduate Research Project DM I                                                                 |0       |5        |5     |
|Graduate Research Project ML I (6 LP)                                                          |0       |5        |5     |
|Kognitionspsychologie                                                                          |0       |1        |1     |
|Magnetic Resonance Imaging                                                                     |0       |5        |5     |
|Technische Akustik - Grundlagen                                                                |0       |1        |1     |
|Technische studentische Exoskelettentwicklung (RISE) I                                         |0       |1        |1     |
|Technische studentische Exoskelettentwicklung (RISE) II                                        |0       |1        |1     |
|Intellectual Property Management                                                               |0       |1        |1     |



