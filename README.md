# CourseGraph

This repository contains utilities for scraping the module database `Moses` from the technical university Berlin and collected data for the programs CS BSc. and CS MSc.

I created this project to get a better understanding of the dependencies between different courses.

# Challenges

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
