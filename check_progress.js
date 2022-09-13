var count_problems_done = 0
var count_total_problems = 0 

for (i = 1; i < problems_table.rows.length; i++){
    count_total_problems += 1
    var row = problems_table.rows.item(i).cells;
    is_done = row[0].innerHTML
    console.log(is_done)
    if (is_done == "Yes"){
        count_problems_done += 1
    }
}
console.log(count_problems_done)
console.log(count_total_problems)

document.getElementById("progress").innerHTML = count_problems_done/count_total_problems + "%"