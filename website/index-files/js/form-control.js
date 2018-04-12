var items = "climate culture demographics economy politics proximity".split(" ")
var sliders = items.map( item => {return document.getElementById(item + "-slider")} )
var outputs = items.map( item => {return document.getElementById(item + "-value")} )
var submit_button = document.getElementById("submit-button")
var city_input = document.getElementById("city-input")

init_slider = function (slider, output) {
    slider.oninput = function() {
        output.innerHTML = slider.value;
        console.log( slider.value )
        console.log( output.innerHTML)
    }
}

for (var i = 0; i < items.length; i++) {
    init_slider( sliders[i], outputs[i] );
}

submit_button.onclick = function() {
    submit_vals = [ city_input.value, sliders.map( slider => {return slider.value} ) ]
    console.log( submit_vals )
}
