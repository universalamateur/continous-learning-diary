# Daily Learning Journal - 2021-10-21 - Thursday

## Typing Academy

Daily [typing lessons](https://www.typing.academy/typing-tutor/lessons)

- Warum Up - All Letters
- Warum Up - All Rows
- Finger Practice - All Letters
- Finger Practice - All Rows
- Practical Exercise - Top 200 english words
- Bonus Lessons - Written Numbers
- Bonus Lessons - Capitals of Europe
- Bonus Lessons - Phonetic Alphabet

## Greek Language

[DuoLingo greek](https://www.duolingo.com/learn)

## Application security testing

### Fuzzing 101 presentation

#### 1 Overview of application security testing - SAST

SAST - Static Application Security Testing
Analysis of source code for possible vulnerabilities before deployment
Integration into IDE or CI Pipeline after MR/PR
Coaching the developer with direct Feedback leading to better code
Many False Positives lead to noise and heighten effort

#### 2 Overview of application security testing - DAST

DAST - Dynamic Application Security Testing
Automated testing at runtime for possible vulnerabilities from the outside
Blackbox testing for known security vulnerabilities before Deployment in SDLC
Less risk of damaging security breaches in the deployed application
Not full code coverage plus manual investigation necessary

#### 3 Fuzzing Overview

Fuzzing is used in Security Testing of Applications already in Deployment by security agencies to find explotable Bugs like Crashes that lead to Memory Leaks or Buffer Overflows.
It is a big Advantage of including Fuzzing as additional Testing methology, complementary to Unit-, Smoke-Tests, etc. , in a CI/CD Pipeline.
Elevating Fuzzing as a tool in the pre deployment stage of the SDLC

Fuzzer Types
Mutation- or Generation-based
Smart (Grammar and/or Protocol aware) or Dumb
Black-, Grey- or White-Box

#### 4 What is fuzzing?

Fuzzing is automated testing of an application at runtime to discover bugs
Providing semi valid, unexpected, or random input while monitoring the application for hangs, crashes or exceptions
Using different structured inputs like files, network data, stdin, UI interaction, API usage the Fuzzer interacts with the Fuzz target
The Fuzzer records the test cases to reproduce the so found crashes of its Fuzz target

#### 5 How does it work?

The Fuzzer has to be interfaced with its target to deliver the input, sometimes called harnessing
A Crash detection and/or binary instrumentation to measure code coverage has to be integrated
Provide Input grammar, seed and/or dictionaries to start with the Fuzzing
Depending on the type of Fuzzer, input will be delivered to the Fuzz target, the behavior of the target monitored as well as logged together with the input.
Based on Inputs and their effects on the application, more input will be generated and delivered to the Fuzz target

#### 6 What can and can’t it do?

Fuzz testing excels in finding bugs in applications, which could lead to security breaches, through crashes, memory leaks, unhandled exception or other exploitable vulnerabilities, when not corrected in the deployed application.
With the fitting set up a good code coverage and a vast set of test cases can be run repeatedly, with little effort, against every iteration of the target software.
The Fuzz Test provides an overall picture of the robustness of the application.

Running a fuzzing campaign for several weeks does not guarantee a 99% secure application nor not finding a bug does not prove the program correct.
The crashing test cases in the Fuzz Report may be difficult to debug and analyze.
Fuzz testing is less effective for dealing with security vulnerabilities that do not cause program crashes.

#### 7 Whitebox vs Blackbox Fuzzing

Blackbox Fuzzing goes through Inputs, monitoring only the overall behaviour of the application in a nearly digital way (Crash or no crash).
Instrumentation added to the Fuzz target enables a Fuzzer to check for Code Coverage, adapting its inputs and making it a Greybox Fuzzer.
If a Fuzzer is aware of the internal program structure, it is counted as a Whitebox Fuzzer.
