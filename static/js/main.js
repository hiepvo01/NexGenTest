var glove_choice = 0;

function getData() {
    const loading = document.createElement("div");
    loading.setAttribute("id", "loading");
    loading.setAttribute("class", "spinner-border text-primary");
    loading.setAttribute("role", "status");
    block = document.getElementById("result_button")
    block.appendChild(loading)

    var url = "http://127.0.0.1:5000/predict";
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        result = JSON.parse(xhr.responseText)
        document.getElementById("dexterity_result").innerHTML = result.dexterity.toFixed(3) + " hours";
        document.getElementById("frostbite_result").innerHTML = result.frostbite.toFixed(3) + " hours";
        console.log(xhr.responseText)
        loading.remove();
    }};

    let temp = document.getElementById('temp').innerHTML.split(" ")[0]
    let humid = document.getElementById('temp').innerHTML.split(" ")[0]
    let spd = document.getElementById('temp').innerHTML.split(" ")[0]
    let hour = document.getElementById('hour').innerHTML.split(" ")[0]

    let active = 0;

    if(document.getElementById('flexRadioDefault1').checked) {
        active = 1;
    }

    var data = {
        "air_temp": temp,
        "humidity": humid,
        "wind_speed": spd,
        "active": active,
        "hours": hour,
        "glove": glove_choice
    
    };
    xhr.send(JSON.stringify(data));
}

function glove(name) {
    document.getElementById('glove_choice').innerHTML = name;
    if(name == "Glove 1"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove1.jpg"
        glove_choice = 0;
    } else if(name == "Glove 2"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove2.jpg"
        glove_choice = 1;
    } else if(name == "Glove 3"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove3.jpg"
        glove_choice = 2;
    } else if(name == "Glove 4"){
        var Image_Id = document.getElementById('glove_image');
        Image_Id.src = "pictures/gloves/glove4.jpg"
        glove_choice = 3;
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