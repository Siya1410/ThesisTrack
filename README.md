# ThesisTrack

### A Python-Based Investment Decision Quality Analyzer

> **Can a profitable investment still come from a poor forecast?**

ThesisTrack is a Python project designed to evaluate investment decisions beyond simple profit and loss.

Instead of asking only whether an investment made money, ThesisTrack compares the investor's original expectations with the realised outcome to explore forecast accuracy, confidence, investment thesis performance, and decision outcomes.

---

## Why I Built ThesisTrack

While learning Python, I wanted to apply programming fundamentals to a problem connected to my interest in finance and analytics.

Investment performance is often judged purely by the final return. However, a positive outcome does not necessarily mean that the original forecast was accurate.

ThesisTrack was created to explore a different question:

**How well did the investor's expectations match what actually happened?**

The project combines introductory Python programming with investment analysis and elements of behavioural decision-making.

---

## What ThesisTrack Analyses

For each investment, the user enters:

- Ticker
- Purchase price
- Current or sale price
- Number of shares
- Dividend received per share
- Expected return
- Confidence level
- Investment thesis type

ThesisTrack then calculates:

- Initial investment
- Ending market value
- Dividend income
- Total profit or loss
- Actual total return
- Forecast error
- Forecast direction accuracy
- Confidence assessment
- Decision outcome classification

---

## Portfolio-Level Analytics

When multiple investments are entered, ThesisTrack produces a portfolio review including:

- Total capital invested
- Total ending value
- Portfolio profit or loss
- Portfolio return
- Number of profitable and loss-making investments
- Best and worst performers
- Directional forecast accuracy
- Average forecast error
- High-confidence forecast accuracy
- Potential overconfidence flags

---

## Investment Thesis Analytics

Investments can be classified as:

1. Growth
2. Value
3. Dividend
4. Momentum
5. Other

ThesisTrack compares thesis categories using:

- Number of investments analysed
- Capital-weighted return
- Forecast direction accuracy

This allows the user to explore whether certain investment approaches have historically produced stronger outcomes or more accurate forecasts.

---

## Confidence Review

Users classify their confidence as:

- Low
- Medium
- High

ThesisTrack then compares confidence with forecast performance.

For example, a high-confidence forecast with an incorrect direction or a forecast error above the defined threshold may be flagged as:

**Potential Overconfidence**

This is intended as a simple analytical heuristic rather than a psychological diagnosis.

---

## Decision Outcome Framework

ThesisTrack separates forecast direction from financial outcome.

Possible classifications include:

- Correct Direction / Positive Outcome
- Positive Outcome / Forecast Miss
- Correct Direction / Negative Outcome
- Forecast Miss / Negative Outcome
- Breakeven variations

This distinction is central to the project:

> **A good outcome and a good forecast are not necessarily the same thing.**

---

## Python Concepts Used

ThesisTrack V1.0 was built using core Python concepts including:

- Variables
- User input
- Numeric conversion
- Conditional statements
- `for` and `while` loops
- Functions
- Return values
- Lists
- Exception handling using `try` / `except`
- Input validation
- Formatted output

No external Python libraries are required for V1.0.

---

## How to Run ThesisTrack

Download or clone the repository.

Open a terminal inside the project folder and run:

```bash
python thesistrack.py
```

If required on Windows:

```bash
py thesistrack.py
```

Follow the prompts to enter investment information.

When finished entering investments, type:

```text
n
```

when asked whether you would like to add another investment.

ThesisTrack will then generate the full portfolio and decision-analysis report.

---

## Example

### Example Input

```text
Ticker: TEST
Purchase Price: 100
Final Price: 110
Shares: 10
Dividend per Share: 2
Expected Return: 8%
Confidence: High
Thesis: Growth
```

### Example Output

```text
Initial Investment: $1,000.00
Ending Market Value: $1,100.00
Dividend Income: $20.00
Total Ending Value: $1,120.00
Profit/Loss: +$120.00

Actual Total Return: +12.00%
Expected Total Return: +8.00%
Forecast Error: 4.00 pp

Thesis Direction: CORRECT
Confidence Review: Well Aligned
Decision Assessment: CORRECT DIRECTION / POSITIVE OUTCOME
```

---

## Current Limitations

ThesisTrack V1.0 intentionally remains a fundamental Python project.

Current limitations include:

- Investment information is entered manually
- Returns are holding-period returns rather than annualised returns
- Transaction costs and taxes are not included
- Benchmark-relative performance is not yet considered
- Confidence classifications use simplified rules
- Forecast-error thresholds are heuristic
- Results depend on the quality of the user's original expectations

---

## Future Development

Potential future versions could incorporate:

- CSV import and export
- Historical market-data APIs
- Pandas for data analysis
- Matplotlib visualisations
- Annualised investment returns
- Benchmark comparison
- Portfolio risk measures
- Sector analysis
- Interactive dashboards
- More sophisticated confidence-calibration analysis

---

## Project Philosophy

ThesisTrack is not designed to predict stock prices or recommend investments.

Its purpose is to explore a different question:

**Was the investment outcome consistent with the expectations and confidence behind the original decision?**

---

## Disclaimer

ThesisTrack was created for educational and analytical purposes only.

It does not provide financial or investment advice.
