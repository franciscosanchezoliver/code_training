function roundToTwo(num) {
    return +(Math.round(num + "e+2")  + "e-2");
}

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

var percentageDone = count_problems_done/count_total_problems * 100
percentageDone = roundToTwo(percentageDone) + "%"

complete_message = "[" + count_problems_done + "/" + 
                         count_total_problems + "] " + percentageDone

document.getElementById("progress").innerHTML = complete_message 

// update the progress bar

var elem = document.getElementById("myBar");
elem.style.width = percentageDone + "%";