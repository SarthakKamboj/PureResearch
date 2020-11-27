import random


def sort_evals(evals: list) -> list:
    for eval_idx in range(len(evals)):
        evals[eval_idx] = sorted(evals[eval_idx])
    return evals


def create_rand_alloc(num_resources: int = 10, num_agents: int = 10):
    alloc = {}
    for i in range(num_resources):
        alloc[str(i)] = [random.randint(0, 100) for _ in range(num_agents)]
    return alloc


def main():
    return


main()
