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
Analysis of source code for possible vulnerabilities before deployment.
Integration into IDE or CI Pipeline after MR/PR.
Coaching the developer with direct Feedback leading to better code.
Many False Positives lead to noise and heighten effort.

> Talking Points

#### 2 Overview of application security testing - DAST

DAST - Dynamic Application Security Testing
Automated testing at runtime for possible vulnerabilities from the outside.
Blackbox testing for known security vulnerabilities before Deployment in SDLC.
Less risk of damaging security breaches in the deployed application.
Not full code coverage plus manual investigation necessary.

> Talking Points

#### 3 Fuzzing Overview

Fuzzing, or Fuzz Testing, is the process of finding security vulnerabilities in input accepting applications by providing semi valid, unexpected, or random input while monitoring the application for hangs, crashes or exceptions.
Fuzzer Types
Mutation-based Dumb or Generation-based Smart (Grammar aware)
Black-, Grey- or White-Box

> Talking Points

Fuzzer Types
Mutation-based
Generation-based
Smart (Grammar and/or Protocol aware): Input structure has been defined, only valid inputs will be generated (json, xml file input for example, webserver fuzzing)
Dumb: a start seed is changed in every iteration
Black-Box: Input to behaviour observation only
Grey-Box: Instrumentation for Code Coverage measurement
White-Box: Intelligent Instrumentation and awareness of program path

#### 4 What is fuzzing?

Fuzzing is an automated testing methodology of an application at runtime.
Using different input like files, network data, stdin, UI interaction, API, etc.
The Fuzzer repeatedly generates test cases for the Fuzz target.
The application is monitored while executing these inputs.
The Fuzzer records test case, application behaviour and optional code coverage.
A report shows the concrete inputs to reproduce and examine the bugs.

> Talking Points

#### 5 How does it work?

Determine and asses Fuzz Target
Identify Inputs and interface Fuzzer
Integrate Crash detection and/or binary instrumentation 
Provide initial seed input or Corpus of prior sessions
Fuzz on and monitor behavior
Log defects
Investigate and debug found misbehaviour

> Talking Points

1. Which Application will have to be fuzzed? Written in which language and built with which tools?
2. What Inputs does this application have? Does it read config files? Network trqaffic? Api Calls? What format and structure have those Inputs? Can a harness be implmented to strip for example the networ traffic out and input comes direct to the application?
3. Is Code Coverage wanted and does it have to be added/attached?
4. Shall this session start from scratch, with a seed as input, with grammar or do we have a set of testcase with already good coverage as this is a continous Fuzzing setup?
5. Determine how long the Fuzzer shall run or what

The Fuzzer has to be interfaced with its target to deliver the input, sometimes called harnessing
A Crash detection and/or binary instrumentation to measure code coverage has to be integrated
Provide Input grammar, seed and/or dictionaries to start with the Fuzzing
Depending on the type of Fuzzer, input will be delivered to the Fuzz target, the behavior of the target monitored as well as logged together with the input.
Based on Inputs and their effects on the application, more input will be generated and delivered to the Fuzz target

#### What can and can’t it do? Possibilities

Fuzz testing excels in finding bugs that lead to security vulnerabilities.
Continuous Fuzzing with a persistent Corpus leads to a more secure SDLC.
With fitting set up a vast set of test cases can be run repeatedly, with little effort, against every iteration of the target software.
The Fuzz Test provides an overall picture of the robustness of the application.
Fuzzing enables the developer to make their own code more secure.

> Talking Points

And because instrumentation enables organizations to integrate application security into IDE and CI/CD tools, developers no longer require teams of specialized application security experts to detect and help remediate vulnerabilities. Instead, developers can fix vulnerabilities as they write code. 

#### What can and can’t it do? Limitations

Running a fuzzing campaign for several weeks does not guarantee a 99% secure application.
Not finding a bug does not prove the program correct.
The crashing test cases in the Fuzz Report may be difficult to debug and analyze.
Fuzz testing is less effective for dealing with security vulnerabilities that do not cause program crashes.
Fuzzing does not replace all other necessary security tests.

#### 7 Whitebox vs Blackbox Fuzzing

Blackbox Fuzzing goes through Inputs, monitoring only the overall behaviour of the application in a nearly digital way (Crash or no crash).
Instrumentation added to the Fuzz target enables a Fuzzer to check for Code Coverage, adapting its inputs and making it a Greybox Fuzzer.
If a Fuzzer is aware of the internal program structure, it is counted as a Whitebox Fuzzer.

> Talking Points

- Blackbox Fuzzing: Simple Setup, not a lot of Engineerg needed. Dependeant on good starting seed for the Inputs. Practical for JPG or png, which can be mutated. 
- Grammar-based fuzzing: Very powerful, the input is kept through engineering in expected valid formats to focus and guide fuzzing toward specific input corner cases of interest. Good for JSON or XML input for example.
- Whitebox Fuzzing: Aware of the source code and its branching, a well formed input as a start seed can lead to nearly full code coverage and finding the explicit values needed for inputs to check all possible cases.
automatically learn input
grammars from input samples for
fuzzing purposes

#### General Fuzzing talking points

Fuzzing, or Fuzz Testing, is the process of finding security vulnerabilities in input accepting appllications by providing semi valid, unexpected, or random input while monitoring the application for hangs, crashes or exceptions.
practice in assessing software security
Fuzzing automatic test generation and execution with the goal of finding security vulnerabilities.
˽ Over the last two decades, fuzzing has
become a mainstay in software security.
Thousands of security vulnerabilities in
all kinds of software have been found
using fuzzing.
˽ If you develop software that may process
untrusted inputs and have never used
fuzzing, you probably should.

Fuzzing is used in Security Testing of Applications already in Deployment by security agencies to find explotable Bugs like Crashes that lead to Memory Leaks or Buffer Overflows.
It is a big Advantage of including Fuzzing as additional Testing methology, complementary to Unit-, Smoke-Tests, etc. , in a CI/CD Pipeline.
Elevating Fuzzing as a tool in the pre deployment stage of the SDLC
