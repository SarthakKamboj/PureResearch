from random import randint
from dag import DAG


def sort_evals(evals: list) -> list:
    for eval_idx in range(len(evals)):
        evals[eval_idx] = sorted(evals[eval_idx])
    return evals


def create_rand_alloc(num_resources: int = 10, num_agents: int = 10, min_val: int = 0, max_val: int = 100):
    alloc = {}
    for num_agent in range(num_agents):
        resource_evals = {}
        for num_resource in range(num_resources):
            resource_evals[f"r{num_resource}"] = randint(min_val, max_val)
        alloc[num_agent] = resource_evals
    return alloc


def main():
    alloc = create_rand_alloc()
    dag = DAG(alloc=alloc)
    return


main()
