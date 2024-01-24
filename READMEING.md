# Project birthPlan

Este README tambem está disponivel em portugues. Clica [aqui](../README.md)

## Context

The birthPlan project arises in the context of the Programming 1 (LTI) course at the Department of Informatics of the Faculty of Sciences of Lisbon, in the academic year 2023/2024. This project aims to develop a Python 3 application called birthPlan, which aims to improve the organization and optimize resources in the maternity services of a group of hospitals.

## Description

birthPlan is software designed to support the nursing team in directing pregnant women to maternity services. It will be used by the smartH hospital coalition to manage the allocation of delivery assistance to specialist doctors and their teams. The program receives information about doctors, scheduled assistance calendars, and unassigned assistance requests. It produces updates in the assistance calendar and the list of doctors after analyzing and distributing the requests.

## Features

- **Input:** The program receives three files with information about doctors, assistance calendars, and assistance requests.

- **Output:** The program generates two output files, one with the updated list of doctors and another with the updated scheduling of assistance.

## How to Run

To execute the software, use the following command in the command line:

```bash
python3 refresh.py inputFile1 inputFile2 inputFile3
```

Make sure the order of the input files (`inputFile1`, `inputFile2`, `inputFile3`) is correct.

`inputFile1` -> This is the file with the list of doctors.

`inputFile2` -> This is the file with the assistance schedule.

`inputFile3` -> This is the file with the list of assistance requests.

## Software Development

The software consists of the following modules:

- `constants.py`: Defines the necessary constants.
- `dateTime.py`: Contains functions to handle formats and operations with dates and times.
- `infoFromFiles.py`: Provides functions to read information from files.
- `planning.py`: Contains functions to perform scheduling and update data structures.
- `infoToFiles.py`: Offers functions to write information to files.
- `refresh.py`: Main program that uses the previous modules to implement the birthPlan application.

## Contributors

- [Guilherme Soares](https://github.com/guimbreon)
- [Duarte Soares](https://github.com/fareskk)

## Implementation Report

Refer to the implementation report (relGrupo13.pdf) for details on each group member's individual contributions, implemented extra features (if applicable), features not implemented (if applicable), and known errors (if applicable).
