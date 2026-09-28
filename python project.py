print("======================================")
print(" TIME & SPACE COMPLEXITY TOOL")
print("======================================")
print()

print("Enter your Python code.")
print("Type END when you are finished.")
print()

code = []

while True:
    line = input()

    if line == "END":
        break

    code.append(line)

program = "\n".join(code)
lines = program.split("\n")

for_loops = program.count("for ")
while_loops = program.count("while ")
total_loops = for_loops + while_loops

nested_loops = False

for i in range(len(lines)):

    if "for " in lines[i] or "while " in lines[i]:

        current_indent = len(lines[i]) - len(lines[i].lstrip())

        for j in range(i + 1, len(lines)):

            if lines[j].strip() == "":
                continue

            next_indent = len(lines[j]) - len(lines[j].lstrip())

            if next_indent > current_indent:

                if "for " in lines[j] or "while " in lines[j]:
                    nested_loops = True
                    break

            else:
                break

        if nested_loops:
            break

max_depth = 0

for i in range(len(lines)):

    if "for " in lines[i] or "while " in lines[i]:

        indent = len(lines[i]) - len(lines[i].lstrip())
        depth = indent // 4 + 1

        if depth > max_depth:
            max_depth = depth

recursion = False
function_names = []

for line in lines:

    stripped = line.strip()

    if stripped.startswith("def "):

        name = stripped.split("def ")[1].split("(")[0]
        function_names.append(name)


for name in function_names:

    if name + "(" in program:

        if program.count(name + "(") > 1:
            recursion = True

list_of_n = False

if "[0] * n" in program:
    list_of_n = True

if "[1] * n" in program:
    list_of_n = True

if "[None] * n" in program:
    list_of_n = True

if "list(range(n))" in program:
    list_of_n = True

list_append = False

if ".append(" in program:
    list_append = True


string_reversal = False

if "[::-1]" in program:
    string_reversal = True

log_loop = False

if "// 2" in program:
    log_loop = True

if "/= 2" in program:
    log_loop = True

if recursion:

    time_complexity = "O(n)"

elif nested_loops:

    if "range(n)" in program and "range(m)" in program:
        time_complexity = "O(nm)"

    elif max_depth == 2:
        time_complexity = "O(n^2)"

    elif max_depth == 3:
        time_complexity = "O(n^3)"

    elif max_depth > 3:
        time_complexity = f"O(n^{max_depth})"

    else:
        time_complexity = "O(n^2)"

elif log_loop and total_loops == 1:

    time_complexity = "O(log n)"

elif string_reversal:

    time_complexity = "O(n)"

elif list_of_n:

    time_complexity = "O(n)"

elif list_append:

    time_complexity = "O(n)"

elif total_loops > 0:

    time_complexity = "O(n)"

else:

    time_complexity = "O(1)"

if recursion:

    space_complexity = "O(n)"

elif string_reversal:

    space_complexity = "O(n)"

elif list_of_n:

    space_complexity = "O(n)"

elif list_append:

    space_complexity = "O(n)"

else:

    space_complexity = "O(1)"


print()

print("======================================")
print(" RESULT")
print("======================================")
print()

print("Number of for loops :", for_loops)
print("Number of while loops :", while_loops)
print("Nested loops :", "Yes" if nested_loops else "No")
print("Recursion detected :", "Yes" if recursion else "No")

print()

print("Time Complexity :", time_complexity)
print("Space Complexity :", space_complexity)

print()

print("======================================")
