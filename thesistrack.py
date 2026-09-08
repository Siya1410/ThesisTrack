"""
ThesisTrack - A Python-based Investment Decision Quality Analyzer

V1:
1. Core investment engine
2. Thesis engine
3. Confidence review
4. Thesis classification
5. Decision outcome classification
6. Multi-investment portfolio review
7. Investor behaviour analytics
8. Thesis-type analytics
9. Investor profile
10. Input validation

Built using only core Python.
No external libraries are required.
"""


# ================================================================
# RECORD LAYOUT
# ================================================================

IDX_TICKER = 0
IDX_BUY_PRICE = 1
IDX_FINAL_PRICE = 2
IDX_SHARES = 3
IDX_DIVIDEND_PER_SHARE = 4
IDX_EXPECTED_RETURN = 5
IDX_CONFIDENCE = 6
IDX_THESIS_TYPE = 7
IDX_INITIAL_INVESTMENT = 8
IDX_ENDING_MARKET_VALUE = 9
IDX_DIVIDEND_INCOME = 10
IDX_TOTAL_ENDING_VALUE = 11
IDX_DOLLAR_PNL = 12
IDX_ACTUAL_RETURN = 13
IDX_FORECAST_ERROR = 14
IDX_DIRECTION = 15
IDX_CONFIDENCE_ASSESSMENT = 16
IDX_DECISION_ASSESSMENT = 17

RECORD_SIZE = 18

CONFIDENCE_NAMES = ["", "Low", "Medium", "High"]

THESIS_NAMES = [
    "",
    "Growth",
    "Value",
    "Dividend",
    "Momentum",
    "Other"
]


# ================================================================
# INPUT VALIDATION
# ================================================================

def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Please enter a value.")
            continue

        return value


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than 0.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter 0 or a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a whole number greater than 0.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_return_percentage(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print(
                "Invalid input. Please enter a number, "
                "for example 12 or -5.5."
            )


def get_choice_in_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))

            if value < low or value > high:
                print(
                    f"Please enter a whole number between {low} and {high}."
                )
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True

        elif answer in ("n", "no"):
            return False

        else:
            print("Please answer y or n.")


# ================================================================
# FORMATTING
# ================================================================

def format_currency(value):
    if value > 0:
        return f"+${value:,.2f}"

    elif value < 0:
        return f"-${abs(value):,.2f}"

    else:
        return "$0.00"


# ================================================================
# STAGE 1 - CORE INVESTMENT ENGINE
# ================================================================

def calculate_dividend_income(dividend_per_share, shares):
    return dividend_per_share * shares


def calculate_dollar_pnl(
    buy_price,
    final_price,
    shares,
    dividend_per_share
):
    capital_gain = (final_price - buy_price) * shares

    dividend_income = calculate_dividend_income(
        dividend_per_share,
        shares
    )

    total_pnl = capital_gain + dividend_income

    return total_pnl


def calculate_actual_return(
    buy_price,
    final_price,
    shares,
    dividend_per_share
):
    initial_investment = buy_price * shares

    dollar_pnl = calculate_dollar_pnl(
        buy_price,
        final_price,
        shares,
        dividend_per_share
    )

    actual_return = (dollar_pnl / initial_investment) * 100

    return actual_return


# ================================================================
# STAGE 2 - THESIS ENGINE
# ================================================================

def calculate_forecast_error(expected_return, actual_return):
    return abs(actual_return - expected_return)


def check_thesis_direction(expected_return, actual_return):
    if expected_return > 0 and actual_return > 0:
        return "Correct"

    elif expected_return < 0 and actual_return < 0:
        return "Correct"

    elif expected_return == 0 and actual_return == 0:
        return "Correct"

    else:
        return "Incorrect"


# ================================================================
# STAGE 3 - CONFIDENCE REVIEW
# ================================================================

def assess_confidence(confidence, forecast_error, direction):
    if confidence == 3 and direction == "Incorrect":
        return "Potential Overconfidence"

    elif confidence == 3 and forecast_error > 10:
        return "Potential Overconfidence"

    elif confidence == 3 and forecast_error <= 5:
        return "Well Aligned"

    elif confidence == 1 and direction == "Correct" and forecast_error <= 5:
        return "Possible Underconfidence"

    else:
        return "Reasonable"


# ================================================================
# STAGE 5 - DECISION OUTCOME CLASSIFICATION
# ================================================================

def assess_decision_quality(direction, dollar_pnl):
    if dollar_pnl > 0:
        if direction == "Correct":
            return "CORRECT THESIS / POSITIVE OUTCOME"
        else:
            return "POSITIVE OUTCOME / FORECAST MISS"

    elif dollar_pnl < 0:
        if direction == "Correct":
            return "CORRECT DIRECTION / NEGATIVE OUTCOME"
        else:
            return "FORECAST MISS / NEGATIVE OUTCOME"

    else:
        if direction == "Correct":
            return "CORRECT DIRECTION / BREAKEVEN OUTCOME"
        else:
            return "FORECAST MISS / BREAKEVEN OUTCOME"


# ================================================================
# STAGE 4 + 6 - COLLECT ONE INVESTMENT
# ================================================================

def collect_investment():
    print()

    ticker = get_non_empty_text(
        "Enter ticker: "
    ).upper()

    buy_price = get_positive_float(
        "Enter purchase price: "
    )

    final_price = get_non_negative_float(
        "Enter current/sale price: "
    )

    shares = get_positive_int(
        "Enter number of shares: "
    )

    dividend_per_share = get_non_negative_float(
        "Enter total dividend received per share (0 if none): "
    )

    expected_return = get_return_percentage(
        "Enter your expected total return (%): "
    )

    confidence = get_choice_in_range(
        "Confidence level (1=Low, 2=Medium, 3=High): ",
        1,
        3
    )

    thesis_type = get_choice_in_range(
        "Thesis type (1=Growth, 2=Value, 3=Dividend, "
        "4=Momentum, 5=Other): ",
        1,
        5
    )

    initial_investment = buy_price * shares
    ending_market_value = final_price * shares

    dividend_income = calculate_dividend_income(
        dividend_per_share,
        shares
    )

    total_ending_value = (
        ending_market_value
        + dividend_income
    )

    dollar_pnl = calculate_dollar_pnl(
        buy_price,
        final_price,
        shares,
        dividend_per_share
    )

    actual_return = calculate_actual_return(
        buy_price,
        final_price,
        shares,
        dividend_per_share
    )

    forecast_error = calculate_forecast_error(
        expected_return,
        actual_return
    )

    direction = check_thesis_direction(
        expected_return,
        actual_return
    )

    confidence_assessment = assess_confidence(
        confidence,
        forecast_error,
        direction
    )

    decision_assessment = assess_decision_quality(
        direction,
        dollar_pnl
    )

    record = [None] * RECORD_SIZE

    record[IDX_TICKER] = ticker
    record[IDX_BUY_PRICE] = buy_price
    record[IDX_FINAL_PRICE] = final_price
    record[IDX_SHARES] = shares
    record[IDX_DIVIDEND_PER_SHARE] = dividend_per_share
    record[IDX_EXPECTED_RETURN] = expected_return
    record[IDX_CONFIDENCE] = confidence
    record[IDX_THESIS_TYPE] = thesis_type
    record[IDX_INITIAL_INVESTMENT] = initial_investment
    record[IDX_ENDING_MARKET_VALUE] = ending_market_value
    record[IDX_DIVIDEND_INCOME] = dividend_income
    record[IDX_TOTAL_ENDING_VALUE] = total_ending_value
    record[IDX_DOLLAR_PNL] = dollar_pnl
    record[IDX_ACTUAL_RETURN] = actual_return
    record[IDX_FORECAST_ERROR] = forecast_error
    record[IDX_DIRECTION] = direction
    record[IDX_CONFIDENCE_ASSESSMENT] = confidence_assessment
    record[IDX_DECISION_ASSESSMENT] = decision_assessment

    return record


# ================================================================
# INDIVIDUAL INVESTMENT SUMMARY
# ================================================================

def print_investment_summary(record):
    print()

    print("-----------------------------------------")
    print("THESISTRACK - INVESTMENT REVIEW")
    print("-----------------------------------------")

    print(f"Ticker: {record[IDX_TICKER]}")
    print(f"Thesis Type: {THESIS_NAMES[record[IDX_THESIS_TYPE]]}")
    print(f"Confidence: {CONFIDENCE_NAMES[record[IDX_CONFIDENCE]]}")

    print()

    print(
        f"Initial Investment: "
        f"${record[IDX_INITIAL_INVESTMENT]:,.2f}"
    )

    print(
        f"Ending Market Value: "
        f"${record[IDX_ENDING_MARKET_VALUE]:,.2f}"
    )

    print(
        f"Dividend Income: "
        f"${record[IDX_DIVIDEND_INCOME]:,.2f}"
    )

    print(
        f"Total Ending Value: "
        f"${record[IDX_TOTAL_ENDING_VALUE]:,.2f}"
    )

    print(
        f"Profit/Loss: "
        f"{format_currency(record[IDX_DOLLAR_PNL])}"
    )

    print()

    print(
        f"Actual Total Return: "
        f"{record[IDX_ACTUAL_RETURN]:+.2f}%"
    )

    print(
        f"Expected Total Return: "
        f"{record[IDX_EXPECTED_RETURN]:+.2f}%"
    )

    print(
        f"Forecast Error: "
        f"{record[IDX_FORECAST_ERROR]:.2f} pp"
    )

    print()

    print(
        f"Thesis Direction: "
        f"{record[IDX_DIRECTION].upper()}"
    )

    print(
        f"Confidence Review: "
        f"{record[IDX_CONFIDENCE_ASSESSMENT]}"
    )

    print()

    print(
        f"Decision Assessment: "
        f"{record[IDX_DECISION_ASSESSMENT]}"
    )

    print("-----------------------------------------")


# ================================================================
# STAGE 6 - PORTFOLIO REVIEW
# ================================================================

def portfolio_review(portfolio):
    total_capital = 0
    total_ending_value = 0

    profitable_count = 0
    loss_count = 0
    breakeven_count = 0

    best_ticker = portfolio[0][IDX_TICKER]
    best_return = portfolio[0][IDX_ACTUAL_RETURN]

    worst_ticker = portfolio[0][IDX_TICKER]
    worst_return = portfolio[0][IDX_ACTUAL_RETURN]

    for record in portfolio:
        total_capital += record[IDX_INITIAL_INVESTMENT]
        total_ending_value += record[IDX_TOTAL_ENDING_VALUE]

        if record[IDX_DOLLAR_PNL] > 0:
            profitable_count += 1

        elif record[IDX_DOLLAR_PNL] < 0:
            loss_count += 1

        else:
            breakeven_count += 1

        if record[IDX_ACTUAL_RETURN] > best_return:
            best_return = record[IDX_ACTUAL_RETURN]
            best_ticker = record[IDX_TICKER]

        if record[IDX_ACTUAL_RETURN] < worst_return:
            worst_return = record[IDX_ACTUAL_RETURN]
            worst_ticker = record[IDX_TICKER]

    total_pnl = total_ending_value - total_capital
    portfolio_return = (total_pnl / total_capital) * 100

    print()

    print("=========================================")
    print("THESISTRACK PORTFOLIO REVIEW")
    print("=========================================")

    print(f"Investments Analysed: {len(portfolio)}")

    print()

    print(f"Total Capital Invested: ${total_capital:,.2f}")
    print(f"Total Ending Value: ${total_ending_value:,.2f}")
    print(f"Total Profit/Loss: {format_currency(total_pnl)}")
    print(f"Portfolio Return: {portfolio_return:+.2f}%")

    print()

    print(f"Profitable Investments: {profitable_count}")
    print(f"Loss-Making Investments: {loss_count}")
    print(f"Breakeven Investments: {breakeven_count}")

    print()

    print(
        f"Best Performer: "
        f"{best_ticker} {best_return:+.2f}%"
    )

    print(
        f"Worst Performer: "
        f"{worst_ticker} {worst_return:+.2f}%"
    )

    return portfolio_return


# ================================================================
# STAGE 7 - INVESTOR BEHAVIOUR ANALYTICS
# ================================================================

def behaviour_analytics(portfolio):
    total = len(portfolio)

    correct_direction = 0
    total_error = 0

    most_accurate = portfolio[0]
    least_accurate = portfolio[0]

    high_confidence_count = 0
    high_confidence_correct = 0
    overconfidence_flags = 0

    for record in portfolio:
        if record[IDX_DIRECTION] == "Correct":
            correct_direction += 1

        total_error += record[IDX_FORECAST_ERROR]

        if (
            record[IDX_FORECAST_ERROR]
            < most_accurate[IDX_FORECAST_ERROR]
        ):
            most_accurate = record

        if (
            record[IDX_FORECAST_ERROR]
            > least_accurate[IDX_FORECAST_ERROR]
        ):
            least_accurate = record

        if record[IDX_CONFIDENCE] == 3:
            high_confidence_count += 1

            if record[IDX_DIRECTION] == "Correct":
                high_confidence_correct += 1

        if (
            record[IDX_CONFIDENCE_ASSESSMENT]
            == "Potential Overconfidence"
        ):
            overconfidence_flags += 1

    direction_accuracy = (
        correct_direction / total
    ) * 100

    average_error = (
        total_error / total
    )

    if high_confidence_count > 0:
        high_confidence_accuracy = (
            high_confidence_correct
            / high_confidence_count
        ) * 100

    else:
        high_confidence_accuracy = 0

    print()

    print("-------------------------------")
    print("FORECASTING PERFORMANCE")
    print("-------------------------------")

    print(
        f"Direction Predictions Correct: "
        f"{correct_direction}/{total}"
    )

    print(
        f"Direction Accuracy: "
        f"{direction_accuracy:.1f}%"
    )

    print(
        f"Average Forecast Error: "
        f"{average_error:.2f} pp"
    )

    print()

    print(
        f"Most Accurate Forecast: "
        f"{most_accurate[IDX_TICKER]} "
        f"(expected "
        f"{most_accurate[IDX_EXPECTED_RETURN]:+.2f}%, "
        f"actual "
        f"{most_accurate[IDX_ACTUAL_RETURN]:+.2f}%)"
    )

    print(
        f"Largest Forecast Miss: "
        f"{least_accurate[IDX_TICKER]} "
        f"(expected "
        f"{least_accurate[IDX_EXPECTED_RETURN]:+.2f}%, "
        f"actual "
        f"{least_accurate[IDX_ACTUAL_RETURN]:+.2f}%)"
    )

    print()

    print("-------------------------------")
    print("CONFIDENCE REVIEW")
    print("-------------------------------")

    print(
        f"High-Confidence Decisions: "
        f"{high_confidence_count}"
    )

    print(
        f"High-Confidence Direction Correct: "
        f"{high_confidence_correct}"
    )

    print(
        f"High-Confidence Direction Accuracy: "
        f"{high_confidence_accuracy:.1f}%"
    )

    print(
        f"Potential Overconfidence Flags: "
        f"{overconfidence_flags}"
    )

    return (
        direction_accuracy,
        average_error,
        high_confidence_accuracy,
        overconfidence_flags
    )


# ================================================================
# STAGE 8 - THESIS-TYPE ANALYTICS
# ================================================================

def thesis_type_analytics(portfolio):
    print()

    print("-------------------------------")
    print("PERFORMANCE BY THESIS")
    print("-------------------------------")

    best_return_type = None
    best_return_value = None

    best_accuracy_type = None
    best_accuracy_value = None

    for thesis_type in range(1, 6):
        matching = []

        for record in portfolio:
            if record[IDX_THESIS_TYPE] == thesis_type:
                matching.append(record)

        if len(matching) == 0:
            continue

        thesis_initial = 0
        thesis_ending = 0
        correct_count = 0

        for record in matching:
            thesis_initial += record[IDX_INITIAL_INVESTMENT]
            thesis_ending += record[IDX_TOTAL_ENDING_VALUE]

            if record[IDX_DIRECTION] == "Correct":
                correct_count += 1

        weighted_return = (
            (
                thesis_ending
                - thesis_initial
            )
            / thesis_initial
        ) * 100

        accuracy = (
            correct_count
            / len(matching)
        ) * 100

        print()

        print(THESIS_NAMES[thesis_type])

        print(
            f"Capital-Weighted Return: "
            f"{weighted_return:+.2f}%"
        )

        print(
            f"Forecast Direction Accuracy: "
            f"{accuracy:.1f}%"
        )

        if (
            best_return_value is None
            or weighted_return > best_return_value
        ):
            best_return_value = weighted_return
            best_return_type = THESIS_NAMES[thesis_type]

        if (
            best_accuracy_value is None
            or accuracy > best_accuracy_value
        ):
            best_accuracy_value = accuracy
            best_accuracy_type = THESIS_NAMES[thesis_type]

    return (
        best_return_type,
        best_return_value,
        best_accuracy_type,
        best_accuracy_value
    )


# ================================================================
# STAGE 9 - INVESTOR PROFILE
# ================================================================

def investor_profile(
    portfolio_return,
    direction_accuracy,
    average_error,
    high_confidence_accuracy,
    overconfidence_flags,
    best_return_type,
    best_return_value,
    best_accuracy_type,
    best_accuracy_value
):
    print()

    print("=========================================")
    print("THESISTRACK - INVESTOR PROFILE")
    print("=========================================")

    print(
        f"Overall Portfolio Return: "
        f"{portfolio_return:+.2f}%"
    )

    print()

    print(
        f"Directional Forecast Accuracy: "
        f"{direction_accuracy:.1f}%"
    )

    print(
        f"Average Forecast Error: "
        f"{average_error:.2f} pp"
    )

    print()

    print(
        f"High-Confidence Direction Accuracy: "
        f"{high_confidence_accuracy:.1f}%"
    )

    print(
        f"Potential Overconfidence Cases: "
        f"{overconfidence_flags}"
    )

    print()

    print(
        f"Strongest Thesis Type by Return: "
        f"{best_return_type} "
        f"({best_return_value:+.2f}%)"
    )

    print(
        f"Most Accurate Thesis Type: "
        f"{best_accuracy_type} "
        f"({best_accuracy_value:.1f}%)"
    )

    print()

    print("Observation:")

    if best_return_type == best_accuracy_type:
        print(
            f"Your {best_return_type} investments "
            f"were both your strongest-returning "
            f"and most accurately forecast thesis type."
        )

    else:
        print(
            f"Your {best_return_type} investments "
            f"generated the strongest capital-weighted "
            f"return, while your {best_accuracy_type} "
            f"investments produced the highest "
            f"directional forecast accuracy."
        )

    print()

    print("Note:")

    print(
        "Returns are holding-period returns "
        "and are not annualised for differences "
        "in investment duration."
    )

    print("=========================================")
    
# ================================================================
# MAIN PROGRAM
# ================================================================
def main():
    print("=========================================")
    print("THESISTRACK")
    print("Investment Decision Quality Analyzer")
    print("=========================================")

    portfolio = []

    while True:
        record = collect_investment()

        print_investment_summary(
            record
        )

        portfolio.append(
            record
        )

        if not get_yes_no(
            "\nAdd another investment? (y/n): "
        ):
            break

    portfolio_return = portfolio_review(
        portfolio
    )

    (
        direction_accuracy,
        average_error,
        high_confidence_accuracy,
        overconfidence_flags
    ) = behaviour_analytics(
        portfolio
    )

    (
        best_return_type,
        best_return_value,
        best_accuracy_type,
        best_accuracy_value
    ) = thesis_type_analytics(
        portfolio
    )
    investor_profile(
        portfolio_return,
        direction_accuracy,
        average_error,
        high_confidence_accuracy,
        overconfidence_flags,
        best_return_type,
        best_return_value,
        best_accuracy_type,
        best_accuracy_value
    )
input("\nPress Enter to close ThesisTrack...")

if __name__ == "__main__":
    main()
