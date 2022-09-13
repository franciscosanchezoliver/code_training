if __name__ == "__main__":
    content =""
    with open("./list_of_questions.md", "r") as f:
        content = f.readlines()

result = ""
type_of_problem = ""
for line in content:
    line = line.replace("\t", "")
    line = line.replace("\n", "")
    problem = ""
    if line.startswith("##"):
        type_of_problem = line[3:]

    elif line.startswith("-"):
        problem = line[2:]
    
    if problem != '':
        result += \
            """
        <tr>
            <td>No</td>
            <td>{}</td>
            <td>{}</td>
            <td></td>
        </tr>

            """.format(type_of_problem, problem)

    with open("./result_table.txt" , 'w') as f:
        f.write(result)


    
