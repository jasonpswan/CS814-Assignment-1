from collections import deque

import time

def next_states(s):
    results = []
    if s[-1] == 'I':
        results.append(s + 'U')
    if s[0] == 'M':
        results.append(s + s[1:])
    for i in range(len(s)-1):
        if s[i:i+3] == 'III':
            s_list = s[0:i] + 'U' + s[i+3:]
            if test not in results:
                results.append(s_list)
        if s[i:i+2] == 'UU':
            s_list2 = s[0:i] + s[i+2:]
            if test not in results:
                results.append(s_list2)
    return results

def extend_path(p):
    results = []
    ns = next_states(p[-1])
    for s in ns:
        results.append(p + [s])
    return results

def depth_limited_dfs(goal_state, limit, extend_count):
    agenda = deque([['MI']])
    current_path = agenda.popleft()
    agenda.extendleft(extend_path(current_path))
    extend_count += 1
    while agenda:
        if agenda == []:
            return [], extend_count, 0
        current_path = agenda.popleft()
        if current_path[-1] == goal_state:
            return current_path, extend_count, len(agenda)
        if len(current_path) < limit:
            agenda.extendleft(extend_path(current_path))
            extend_count += 1
            
def iterative_deepening(goal_state):
    limit = 1
    extend_count = 0
    while True:
        res = depth_limited_dfs(goal_state, limit, extend_count)
        if res != None:
            return res[0]
        else:
            limit += 1
            
def test_MIU(goal):
    start = time.time()
    search_result = iterative_deepening(goal)
    end = time.time()
    print('Time taken:', end - start)
    return search_result