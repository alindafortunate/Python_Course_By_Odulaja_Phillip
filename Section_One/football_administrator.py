# A program to administer a football match.

match_status = input(
    "What is the status of the match? Answer is either played or suspended "
)

if match_status == "suspended":
    print("Match suspended.")
elif match_status == "played":
    home_team = int(input("How many goals were scored by the home team? "))
    away_team = int(input("How many goals were scored by the away team? "))

    if home_team > away_team:
        print("Home team won the match.")
    elif home_team == away_team:
        print("The match was a draw.")
    else:
        print("Away team won the match.")
else:
    print("Invalid match status.")
