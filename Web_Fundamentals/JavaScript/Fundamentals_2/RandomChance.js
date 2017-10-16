function slotmachine (quarters, walkAwayAmount){
    while (quarters >0){
        quarters --;
        var winningnumber =1;
        if(Math.floor (Math.random()*100) === winningnumber){
            quarters += Math.floor (Math.random ()*51 + 50)
            console.log ("The User Just Wont, and Now Has" + quarters + "quarters") 
            if(quarters >= walkAwayAmount) {
                break;
            }
        }
    }
    return quarters;
}
var result = slotmachine (200, 250);
console.log (result);