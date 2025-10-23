def bpm(graph, u, matchR, seen):
    for v in range(len(graph[0])):
        if graph[u][v] and not seen[v]:
            seen[v] = True
            if matchR[v] == -1 or bpm(graph, matchR[v], matchR, seen):
                matchR[v] = u
                return True
    return False

def max_bipartite_matching(graph):
    matchR = [-1] * len(graph[0])
    result = 0
    for u in range(len(graph)):
        seen = [False] * len(graph[0])
        if bpm(graph, u, matchR, seen):
            result += 1
    return result, matchR

def main():
    print("=== Volunteer-NGO Bipartite Matching ===")
    num_volunteers = int(input("Enter number of volunteers: "))
    num_ngos = int(input("Enter number of NGOs: "))

    print("\nEnter compatibility (1 for compatible, 0 for not) for each Volunteer-NGO pair:")
    graph = []
    for i in range(num_volunteers):
        while True:
            row = input(f"Volunteer {i} (space separated {num_ngos} values [0 or 1]): ").strip().split()
            if len(row) == num_ngos and all(x in ['0', '1'] for x in row):
                graph.append([x == '1' for x in row])
                break
            else:
                print(f"Invalid input. Enter exactly {num_ngos} values of 0 or 1.")

    max_matches, match_result = max_bipartite_matching(graph)
    print(f"\nMaximum number of volunteer-NGO pairs: {max_matches}")
    for ngo, volunteer in enumerate(match_result):
        if volunteer != -1:
            print(f"NGO {ngo} is assigned to Volunteer {volunteer}")

if __name__ == "__main__":
    main()