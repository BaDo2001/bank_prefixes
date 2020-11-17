data = []

with open("bank_nums.txt") as f:
    for line in f:
        data.append(line.strip().split())

def is_unique(prefix):
    fitting_banks = set()
    for num, bank in data:
        if num[:len(prefix)] == prefix:
            fitting_banks.add(bank)
    
    if len(fitting_banks) == 1:
        return True, True, fitting_banks.pop()
    elif len(fitting_banks) == 0:
        return False, False, None
    return False, True, None

def find_unique_prefixes(prefix="", solution={}):
    unique, needs_to_continue, bank = is_unique(prefix)

    if unique:
        solution[prefix] = bank
    elif needs_to_continue:
        for i in range(10):
            solution = {**solution, **find_unique_prefixes(f"{prefix}{i}", solution)} 
    return solution

solution = find_unique_prefixes()

with open("my_bic.ts", "w") as f:
    f.write("export const bic = new Map<RegExp, String>([\n")
    for prefix, bank in solution.items():
        f.write(f"  [/^{prefix}/, '{bank}'],\n")
    f.write("]);")
