A_1_runs, A_1_wickets, A_2_runs, A_2_wickets = int(input()),int(input()),int(input()),int(input())
B_1_runs, B_1_wickets, B_2_runs, B_2_wickets = int(input()),int(input()),int(input()),int(input())
total_A_runs = A_1_runs + A_2_runs
total_B_runs = B_1_runs + B_2_runs
if (total_B_runs > total_A_runs):
    print("Team B")
if (total_A_runs > total_B_runs and B_2_wickets == 10):
    print('Team A')
else:
    print('DRAW')