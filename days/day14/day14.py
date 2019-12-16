import utils.input
import math
import re
import sys
from typing import List, Dict

class Component:
    def __init__(self, name:str, qty:int):
        self.name = name
        self.qty = qty

    @classmethod
    def fromString(cls, str):
        match = re.search('(\d+) (.*)', str)

        return cls(match.group(2), int(match.group(1)))

class Reaction:

    # input_reactions: List['Reaction']
    inputs: List[Component]
    output: Component
    run_count: int

    def __init__(self, inputs:List[Component], output:Component):
        self.output = output
        self.inputs = inputs
        self.input_reactions = []
        self.run_count = 0

    def run(self, desired_qty: int, resource_pool:dict, reactions:dict):
        runs = int(math.ceil(desired_qty / float(self.output.qty)))

        for c in self.inputs:
            total_needed = (c.qty * runs) - resource_pool.get(c.name)
            if total_needed > 0:
                reactions.get(c.name).run(total_needed, resource_pool, reactions)
            resource_pool[c.name] = resource_pool.get(c.name) - (c.qty * runs)

        resource_pool[self.output.name] = resource_pool.get(self.output.name) + (self.output.qty * runs)
        self.run_count += runs



def parse_input():
    reactions = {}
    reactions['ORE'] = Reaction([], Component("ORE", 1))
    for row in utils.input.getInput().readlines():
        a = row.strip().split(" => ")
        output = Component.fromString(a[1])
        inputs = []
        for i in a[0].split(", "):
            inputs.append(Component.fromString(i))

        reactions[output.name] = Reaction(inputs, output)
    return reactions

def part1():

    reactions = parse_input()
    resources = {}
    for k in reactions.keys():
        resources[k] = 0

    reactions.get('FUEL').run(1, resources, reactions)

    print(reactions.get('ORE').run_count)



    return


def part2():
    reactions = parse_input()
    resources = {}
    for k in reactions.keys():
        resources[k] = 0

    # reactions.get('FUEL').run(int(1000000000000/13312), resources, reactions)
    fule_for_one = 1590844
    runs = int((1000000000000 - reactions.get('ORE').run_count) / fule_for_one)
    while reactions.get('ORE').run_count <= 1000000000000 and runs > 0:

        reactions.get('FUEL').run(runs, resources, reactions)
        print(reactions.get('FUEL').run_count)
        runs = int((1000000000000 - reactions.get('ORE').run_count) / fule_for_one)

    print(reactions.get('FUEL').run_count )


part2()



