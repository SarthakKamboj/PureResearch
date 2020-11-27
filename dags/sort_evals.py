import random


def sort_evals(evals: list) -> list:
    for eval_idx in range(len(evals)):
        evals[eval_idx] = sorted(evals[eval_idx])
    return evals


def create_rand_alloc(num_resources: int = 10, num_agents: int = 10, min_val: int = 0, max_val: int = 100):
    alloc = {}
    for i in range(num_resources):
        alloc[str(i)] = [random.randint(min_val, max_val)
                         for _ in range(num_agents)]
    return alloc


def main():
    return


main()
