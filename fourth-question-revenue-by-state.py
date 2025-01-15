revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53
}

total_monthly = sum(revenue.values())

percentages = {state: (value / total_monthly) * 100 for state, value in revenue.items()}

for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")