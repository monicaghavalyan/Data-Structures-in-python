import math
import sys


def main():
    tasks = [(1, 4, 10), (2, 8, 4), (3, 3, 20), (4, 6, 11), (5, 5, 2),
             (6, 7, 8), (7, 3, 6), (8, 2, 7), (9, 6, 14), (10, 9, 30)]
    time = 9
    print('Job sequencing problem recursively:',job_sequencing_problem_rec(tasks, time))
    print('Job sequencing problem memoized:', job_sequencing_problem_memo(tasks, time, [[None]*(time)] * len(tasks)))
    print('Job sequencing problem bottom-up:', job_sequencing_problem_bottom_up(tasks, time))
    print('Job sequencing problem greedy:', job_sequencing_problem_greedy(tasks, time))
    print('Job sequencing problem greedy recursively:', job_sequencing_problem_greedy_rec(tasks, time))


def job_sequencing_problem_rec(tasks, time):
    if len(tasks) == 0 or time == 0:
        return 0
    
    last_task = tasks[-1]
    profit_with_task = last_task[2] + job_sequencing_problem_rec(tasks[:-1], time - 1)
    profit_without_task = job_sequencing_problem_rec(tasks[:-1], time)
    return max(profit_with_task, profit_without_task)


def job_sequencing_problem_memo(tasks, time, cache):
    if len(tasks) == 0 or time == 0:
        return 0
    if cache[len(tasks) - 1][time - 1] is not None:
        return cache[len(tasks) - 1][time - 1]
    last_task = tasks[-1]

    if last_task[1] > time:
        cache[len(tasks) - 1][time - 1] = job_sequencing_problem_memo(tasks[:-1], time, cache)
    else:
        profit_with_task = last_task[2] + job_sequencing_problem_memo(tasks[:-1], time - 1, cache)
        profit_without_task = job_sequencing_problem_memo(tasks[:-1], time, cache)
        cache[len(tasks) - 1][time - 1] = max(profit_with_task, profit_without_task)
    return cache[len(tasks) - 1][time - 1]


def job_sequencing_problem_bottom_up(tasks, time):
    matrix = [[0]*(time + 1)] * (len(tasks) + 1)
    for i in range(0, len(tasks)):
        for j in range(0, time):
            task_deadline = tasks[i][1]
            task_profit = tasks[i][2]
            if task_deadline > j + 1:
                matrix[i + 1][j + 1] = matrix[i][j + 1]
            else:
                profit_with_task = task_profit + matrix[i][j]
                profit_without_task = matrix[i][j + 1]
                matrix[i + 1][j + 1] = max(profit_with_task, profit_without_task)
    return matrix[len(tasks)][time]


def job_sequencing_problem_greedy(tasks, time):
    tasks = sorted(tasks, key=lambda x: x[2], reverse=True)
    max_profit = 0
    schedule = [0] * time
    for task in tasks:
        deadline, profit = task[1], task[2]
        if deadline <= time:
            for i in range(deadline - 1, -1, -1):
                if schedule[i] == 0:
                    schedule[i] = 1
                    max_profit += profit
                    break
        else:
            for i in range(time - 1, -1, -1):
                if schedule[i] == 0:
                    schedule[i] = 1
                    max_profit += profit
                    break
    return max_profit


def job_sequencing_problem_greedy_rec(tasks, time):
    tasks = sorted(tasks, key=lambda x: x[2], reverse=True)
    return job_sequencing_problem_greedy_rec_helper(tasks, time, [0] * time)

def job_sequencing_problem_greedy_rec_helper(tasks, time, schedule):
    if time == 0 or not tasks:
        return 0
    tasks = sorted(tasks, key=lambda x: x[2], reverse=True)
    first_task = tasks[0]
    deadline, profit = first_task[1], first_task[2]
    if deadline <= time:
        for i in range(deadline - 1, -1, -1):
            if schedule[i] == 0:
                schedule[i] = 1
                return job_sequencing_problem_greedy_rec_helper(tasks[1:], time, schedule) + profit
    else:
        for i in range(time - 1, -1, -1):
            if schedule[i] == 0:
                schedule[i] = 1
                return job_sequencing_problem_greedy_rec_helper(tasks[1:], time, schedule) + profit
    return job_sequencing_problem_greedy_rec_helper(tasks[1:], time, schedule)



def activity_selection_rec(s, f, i, j):
    max_act = 2
    res = [0] * len(s)
    for k in range(i+1, j):
        if f[i] <= s[k] and f[k] <= s[j]:
            res1 = activity_selection_rec(s, f, i, k)
            res2 = activity_selection_rec(s, f, k, j)
            l = res1[0] + res2[0] - 1
            if l > max_act:
                max_act = l
                for m in range(len(res1[1])):
                    res[m] = res1[1][m]
                for m in range(len(res2[1])):
                    res[m] = res2[1][m]
    res[i] = 1
    res[j] = 1
    return (max_act, res)


def activity_selection_dyn(s, f):
    max_act = 0
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if f[i] <= s[j]:
                res = activity_selection_rec(s, f, i, j)
                if res[0] > max_act:
                    max_act = res[0]
                    result = res[1]
    return (max_act, result)


def activity_selection_greedy_rec(s, f):
    if len(s) == 0:
        return 0
    k = len(s)
    for i in range(1, len(s)):
        if f[0] <= s[i]:
            k = i
            break
    return 1+activity_selection_greedy_rec(s[k:], f[k:])


def activity_selection_greedy(s, f):
    k = 0
    res = [0] * len(s)
    count = 0
    while k < len(s):
        res[k] = 1
        count += 1
        temp = k
        for i in range(k+1, len(s)):
            if f[k] <= s[i]:
                temp = i
                break
            if temp != k:
                k = temp
            else:
                k = len(s)
    return (count, res)


def get_substrings_sorted(s):
    if s == '':
        return []
    l = []
    c = s[0]
    l.append(c)
    for i in get_substrings_sorted(s[1:]):
        l.append(i)
        l.append(c + i)
    for i in range(len(l)):
        for j in range(i, len(l)):
            if len(l[j]) < len(l[i]):
                l[i], l[j] = l[j], l[i]
            if len(l[j]) == len(l[i]) and l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


def matrix_chain_rec(p, i, j):
    if i == j:
        return 0
    min_val = sys.maxsize
    for k in range(i, j):
        val = matrix_chain_rec(p, i, k) + \
            matrix_chain_rec(p, k+1, j) + p[i-1]*p[k]*p[j]
        if val < min_val:
            min_val = val
    return min_val


def matrix_chain_mem(p, i, j, cache_matrix):
    if i == j:
        return 0

    if cache_matrix[i][j] != -1:
        return cache_matrix[i][j]
    cache_matrix[i][j] = sys.maxsize

    for k in range(i, j):
        cache_matrix[i][j] = min(cache_matrix[i][j], matrix_chain_mem(p, i, k, cache_matrix) +
                                 matrix_chain_mem(p, k + 1, j, cache_matrix) + p[i - 1] * p[k] * p[j])

    return cache_matrix[i][j]


def matrix_chain_bottom_up(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                val = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if val < m[i][j]:
                    m[i][j] = val
    return m[1][n-1]


def mult_of_prev_elements(listt):
    if len(listt) == 1:
        return listt
    return mult_of_prev_elements(listt[0:-1]) + [math.prod(listt[0:-1])]


def get_substrings(s):
    if s == '':
        return []
    l = []
    c = s[0]
    l.append(c)
    for i in get_substrings(s[1:]):
        l.append(i)
        l.append(c + i)
    return sorted(l, key=len)


def get_bin(val, num_of_bits):
    bin = ''
    for i in range(num_of_bits):
        bin = str(val % 2) + bin
        val //= 2
    return bin


def get_substrings_using_bit_manipulations(s):
    for i in range(0, 2**(len(s))):
        b = get_bin(i, len(s))
        substr = ''
        for j in range(len(b)):
            if b[j] == '1':
                substr += s[j]
        print(substr)


counter = 0


def fib(chache, n):
    global counter
    counter += 1
    if chache[n] == -1:
        chache[n] = fib(chache, n-1) + fib(chache, n-2)
    return chache[n]


def knapsack(W, w, v, i, r):
    if W <= 0 or i < 0:
        return 0
    if w[i] > W:
        return knapsack(W, w, v, i-1, r)
    r1 = [0] * len(w)
    r2 = [0] * len(w)
    with_i = v[i] + knapsack(W - w[i], w, v, i-1, r1)
    without_i = knapsack(W, w, v, i-1, r2)
    if with_i > without_i:
        r = r1
        r[i] = 1
    else:
        r = r[2]
        r[i] = 0
    return max(with_i, without_i)


def knapsack_mem(W, w, v, i, r, chache):
    if W <= 0 or i < 0:
        return 0
    if w[i] > W:
        if chache[W][i - 1] == -1:
            chache[W][i - 1] = knapsack_mem(W, w, v, i - 1, r, chache)
        chache[W][i] = chache[W][i - 1]
        return chache[W][i]

    if chache[W - w[i]][i - 1] == -1:
        chache[W - w[i]][i -
                         1] = knapsack_mem(W - w[i], w, v, i - 1, r, chache)
    with_i = v[i] + chache[W - w[i]][i - 1]

    if chache[W][i - 1] == -1:
        chache[W][i - 1] = knapsack_mem(W, w, v, i - 1, r, chache)
    without_i = chache[W][i - 1]
    if with_i > without_i:
        r[i] = 1
        chache[W][i] = with_i
        return with_i
    chache[W][i] = without_i
    r[i] = 0
    return without_i


def longest_common_subseq(a, b, i, j):
    if i >= len(a) or j >= len(b):
        return 0
    if a[i] == b[j]:
        return 1 + longest_common_subseq(a, b, i+1, j+1)
    return max(longest_common_subseq(a, b, i, j+1), longest_common_subseq(a, b, i+1, j))


def longest_common_subseq_memo(a, b, i, j, cache):
    if i >= len(a) or j >= len(b):
        return 0
    if a[i] == b[j]:
        return 1 + longest_common_subseq(a, b, i + 1, j + 1)
    return max(longest_common_subseq(a, b, i, j+1), longest_common_subseq(a, b, i+1, j))


if __name__ == "__main__":
    main()
