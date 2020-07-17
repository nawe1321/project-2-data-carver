# Project 2 | Data Carver

> CYBR 5330 - Digital Forensics - Summer 2020

Project 2 of CYBR 5330 - Digital Forensices demonstrating a Data Carving program written in Python supporting the following features:
- Carving Evidence from a Binary File

## Contributors
- Bobbie Bastian
- Preston Church
- Nathan Wendlowsky

## Overview

This project will provide you with experience in recognizing a variety of file types at the byte level. Deleting, hiding, and renaming files are a few methods used to evade a forensics investigation.  Find as many files as you can…

## Project Requirements

Write a Python program to carve evidence from a binary file.
- There are no import library restrictions
- Your program must accept a binary file as a command-line argument (test using a binary file in the same folder as your python program)
- Your program must write carved files to a folder titled with your last name
- Your program must write the MD5 hash of each carved file to a file names hashes.txt in the same folder as the carved images
- Your program must output to screen some basic file information such as file type found, file size, and location offset for each carved file

Recommend you start by carving one file type, then expand your solution to carve various file types.  You solution will be testing using a binary file with primarily jpg, png, and pdf file types.

The following items must be submitted to receive full credit for this project:
1) A document explaining your approach/methodology for this project (.doc, .docx, .txt, .pdf, etc…)
2) Commented code (.py file)
