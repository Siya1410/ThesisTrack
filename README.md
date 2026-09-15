# ThesisTrack

**A Python-based Investment Decision Quality Analyzer**

ThesisTrack is a finance-focused decision-support tool designed to help investors evaluate the quality of an investment thesis before making an investment decision.

The project combines structured investment reasoning, confidence assessment, behavioural analysis, thesis classification, and portfolio-level review into a single Python-based framework.

---

## Project Overview

Investment decisions are often influenced by conviction, incomplete reasoning, behavioural bias, and inconsistent evaluation.

ThesisTrack was developed to introduce a more structured approach to investment decision-making.

Instead of simply asking whether an investment is attractive, ThesisTrack evaluates the reasoning behind the investment thesis and helps identify whether the decision is supported by a strong analytical foundation.

The project is designed as a decision-support framework rather than an investment recommendation system.

---

## Key Features

ThesisTrack V1 includes:

- Core investment decision engine
- Investment thesis evaluation
- Confidence review
- Thesis classification
- Decision outcome classification
- Multi-investment portfolio review
- Investor behaviour analytics
- Thesis-type analytics
- Investor profiling
- Input validation

---

## How ThesisTrack Works

The program guides the user through a structured investment review.

The user provides information about an investment thesis through a series of inputs.

ThesisTrack then evaluates the information across several dimensions.

The process broadly follows:

1. Enter investment-related information
2. Evaluate the investment thesis
3. Review the investor's confidence level
4. Classify the thesis
5. Analyse behavioural characteristics
6. Generate a decision outcome
7. Compare multiple investment decisions where applicable
8. Review portfolio-level patterns

The goal is not to predict future stock prices.

Instead, ThesisTrack focuses on evaluating the **quality of the investment decision-making process**.

---

## Decision Analysis Framework

ThesisTrack examines several components of an investment decision.

### Investment Thesis

The program evaluates the reasoning supporting an investment idea and helps determine whether the thesis is sufficiently developed.

### Confidence Review

The system examines the investor's level of confidence in the investment thesis.

This can help distinguish between:

- high-confidence decisions supported by reasoning
- uncertain decisions
- potentially overconfident decisions

### Thesis Classification

Investment theses can be classified according to their characteristics and reasoning structure.

This provides a more structured way to compare different investment ideas.

### Decision Outcome Classification

ThesisTrack produces a structured decision outcome based on the information provided by the user.

### Investor Behaviour Analytics

The project also considers behavioural elements that may influence investment decisions.

This helps identify patterns in how investors approach decisions rather than focusing only on the investment itself.

### Portfolio Review

ThesisTrack can evaluate multiple investment decisions to identify patterns across a broader portfolio of investment theses.

---

## Project Structure

```text
ThesisTrack/
│
├── data/
│   └── Case-study datasets and analytical outputs
│
├── presentation/
│   └── Final ThesisTrack project presentation
│
├── visuals/
│   └── Project charts and visualizations
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── thesis_track.py
```

## Main Files

### `thesis_track.py`

The main Python program containing the ThesisTrack investment decision analysis framework.

### `data/`

Contains the dataset and results used to demonstrate the application of ThesisTrack.

### `visuals/`

Contains visualizations produced for the project and case-study analysis.

### `presentation/`

Contains the final presentation explaining the project, methodology, case study, and findings.

### `requirements.txt`

ThesisTrack V1 uses no external Python libraries.

### `LICENSE`

Contains the license governing the use of the project.

---

## Technology

ThesisTrack V1 is built entirely using **core Python**.

No external Python libraries are required.

This was an intentional design choice to keep the application:

- lightweight
- easy to run
- portable
- understandable
- dependency-free

### Language

- Python 3

### External Dependencies

None.

The project uses Python's built-in functionality only.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Siya1410/ThesisTrack.git
```

Move into the project directory:

```bash
cd ThesisTrack
```

No additional packages need to be installed.

---

## Running ThesisTrack

Run the main Python file:

```bash
python thesis_track.py
```

Depending on your system, you may need to use:

```bash
python3 thesis_track.py
```

The program will then guide you through the investment analysis using interactive inputs.

---

## Example Workflow

A typical ThesisTrack analysis may follow this process:

```text
Investment Idea
      ↓
Investment Thesis
      ↓
Confidence Review
      ↓
Thesis Classification
      ↓
Behavioural Analysis
      ↓
Decision Evaluation
      ↓
Final Decision Classification
```

For multiple investments, the program can also analyse patterns across the investor's broader decision portfolio.

---

## Case Study

A case study is included in the repository to demonstrate how ThesisTrack can be applied to investment decision analysis.

The case study demonstrates how structured investment reasoning can be transformed into measurable decision-quality indicators.

Supporting materials can be found in:

- `data/`
- `visuals/`
- `presentation/`

The case study is intended to demonstrate the analytical framework rather than provide investment recommendations.

---

## Visual Analysis

The `visuals/` folder contains charts and analytical outputs generated as part of the ThesisTrack case study.

These visualizations help demonstrate:

- investment decision patterns
- thesis characteristics
- confidence levels
- behavioural tendencies
- portfolio-level observations

---

## Why I Built ThesisTrack

Investment analysis often focuses heavily on outcomes.

However, a profitable investment does not necessarily mean that the original decision was analytically strong.

Similarly, an investment that performs poorly does not automatically mean that the underlying reasoning was poor.

This project therefore focuses on a different question:

> **Was the investment decision supported by a high-quality investment thesis and a structured reasoning process?**

ThesisTrack was developed to explore the distinction between **investment outcome quality** and **investment decision quality**.

---

## Project Objectives

The primary objectives of ThesisTrack are to:

- introduce structure into investment decision-making
- improve investment-thesis evaluation
- identify behavioural patterns
- analyse investor confidence
- distinguish decision quality from investment outcomes
- support more disciplined investment reasoning
- create a framework that can be expanded into a more advanced investment analytics system

---

## Current Scope

ThesisTrack V1 focuses primarily on:

- structured qualitative investment analysis
- investment thesis assessment
- confidence evaluation
- behavioural analysis
- decision classification
- portfolio-level thesis review

The current version does not attempt to forecast security prices or generate automated buy/sell recommendations.

---

## Limitations

ThesisTrack V1:

- does not use live market data
- does not perform automated valuation
- does not conduct portfolio optimisation
- does not include historical backtesting
- does not currently calculate advanced risk-adjusted performance metrics
- relies on user-provided information
- does not guarantee investment performance

The quality of the output therefore depends partly on the quality and accuracy of the information entered by the user.

---

## Future Development

Potential future versions of ThesisTrack may include:

- historical backtesting
- benchmark comparison
- risk-adjusted performance metrics
- automated financial-data integration
- expanded portfolio analytics
- quantitative investment scoring
- financial statement integration
- valuation analysis
- improved behavioural-finance analytics
- automated reporting
- interactive dashboards
- larger investment datasets
- machine-learning-supported analysis

These extensions could allow ThesisTrack to evolve from a structured decision-quality framework into a broader investment research and analytics platform.

---

## Design Philosophy

ThesisTrack is based on the principle that:

> **Good investment outcomes and good investment decisions are not always the same thing.**

An investor can make a poorly reasoned decision and still generate a positive return.

Likewise, a well-researched investment thesis may experience an unfavourable outcome because of unexpected market developments.

For this reason, ThesisTrack focuses on analysing the **process behind the investment decision**, rather than judging decisions solely by their final returns.

---

## Learning Outcomes

Developing ThesisTrack involved applying concepts across:

- finance
- investment analysis
- behavioural finance
- decision-making
- Python programming
- analytical framework design
- data interpretation
- portfolio analysis
- project documentation
- financial communication

The project was designed to connect financial reasoning with practical programming and analytical problem-solving.

---

## Repository Contents

The repository includes:

- complete Python source code
- case-study dataset
- case-study results
- analytical visualizations
- project documentation
- final project presentation
- dependency information
- project license

---

## Disclaimer

ThesisTrack is an educational and analytical project.

It does **not** constitute financial advice, investment advice, or a recommendation to buy, sell, or hold any financial security.

The framework is intended to support structured thinking and investment research.

Users should conduct their own research and seek appropriate professional advice before making investment decisions.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Author

**Siya Sandeep Kulkarni**

Finance undergraduate with interests in:

- Investment Analysis
- Asset Management
- Business Analytics
- Financial Markets
- Data-Driven Decision Making

---

## Project Status

**ThesisTrack V1 — Completed**

The current version establishes the core investment decision-quality framework.

Future versions may extend the platform with quantitative investment analytics, backtesting, market-data integration, and risk-adjusted performance analysis.
