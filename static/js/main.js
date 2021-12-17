function glove(name) {
    document.getElementById('glove_choice').innerHTML = name;
    if(name == "Glove 1"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove1.jpg"
    } else if(name == "Glove 2"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove2.jpg"
    } else if(name == "Glove 3"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove3.jpg"
    } else if(name == "Glove 4"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove4.jpg"
    }
}

function tempVal(val) {
    document.getElementById("temp").innerHTML = val + " Celcius";

    var tempColor = d3.scaleSequential().domain([-20,41])
        .interpolator(d3.interpolateTurbo);

    document.getElementById("temp").style.color = tempColor(val)
}

function tempHum(val) {
    document.getElementById("humid").innerHTML = val + " %";

    var tempColor = d3.scaleSequential().domain([15,76])
        .interpolator(d3.interpolateTurbo);

    document.getElementById("humid").style.color = tempColor(val)
}

function tempHour(val) {
    document.getElementById("hour").innerHTML = val + " hours";

    var tempColor = d3.scaleSequential().domain([0,21])
        .interpolator(d3.interpolateTurbo);

    document.getElementById("hour").style.color = tempColor(val)
}

function tempSpd(val) {
    document.getElementById("spd").innerHTML = val + " m/s";

    var tempColor = d3.scaleSequential().domain([1,7])
        .interpolator(d3.interpolateTurbo);

    document.getElementById("spd").style.color = tempColor(val)
}