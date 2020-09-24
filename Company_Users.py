company_users = {}

command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id in company_users[company_name]:
        company_users[company_name].remove(employee_id)
        # continue
    company_users[company_name] += [employee_id]

    command = input()

for name, id in sorted(company_users.items(), key=lambda x: x[0]):
    print(name)
    for i in sorted(id):
        print(f"-- {''.join(i)}")

# print(company_users)

#Input text
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
