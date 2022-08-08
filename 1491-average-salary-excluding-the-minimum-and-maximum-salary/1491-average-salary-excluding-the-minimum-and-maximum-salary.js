/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    //iterate over array
    var min = salary[0]
    var max = salary[0]
    for (var i = 0; i < salary.length; i++) {
        var currSalary = salary[i]
        if (currSalary < min) {
          min = currSalary
        }
        if (currSalary > max) {
          max = currSalary
        }
    }
    console.log(min, max)
    //find min salary
    //find max salary
    
    var total = 0
    //iterate over array
    for (var j = 0; j < salary.length; j++) {
        if (salary[j] !== min && salary[j] !== max) {
            total += salary[j]
        }
    }
    console.log(total)
    //if current salary !== min or max
      //add it to total
    //return total / array length - 2
    return total / (salary.length - 2)
};