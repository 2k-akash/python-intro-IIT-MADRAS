n = int(input())
scores_dataset = []
for i in range(n):
    record = dict()
    record['Name'] = input()
    record['City'] = input()
    record['SeqNo'] = int(input())
    record['Mathematics'] = int(input())
    record['Physics'] = int(input())
    record['Chemistry'] = int(input())
    scores_dataset.append(record)