var items = "climate culture demographics economy politics proximity".split(" ")
var sliders = items.map( item => {return document.getElementById(item + "-slider")} )
var outputs = items.map( item => {return document.getElementById(item + "-value")} )
var submit_button = document.getElementById("submit-button")
var city_input = document.getElementById("city-input")


var paramVals={}
paramVals[0] = document.getElementById("climate-value2");
paramVals[1] = document.getElementById("culture-value2");
paramVals[2] = document.getElementById("demographics-value2");
paramVals[3] = document.getElementById("economy-value2");
paramVals[4] = document.getElementById("politics-value2");
paramVals[5] = document.getElementById("proximity-value2");



// Autocomplete function for the input search bar
$( function() {
    city_names = ['Chicago', 'New York', 'Los Angeles', "San Francisco"]
    var limit = 5
    $( "#city-input" ).autocomplete({
        // source: city_names
        source: function(request, response) {
            var results = $.ui.autocomplete.filter(city_names, request.term)
            response(results.slice(0, limit))
        }
    })
})

// Function to initialize the sliders
init_slider = function (slider, output,output2) {
    slider.oninput = function() {
        output.innerHTML = slider.value
		output2.value=slider.value
        //console.log( slider.value )
        //console.log( output2)
    }
}

// Initialize the sliders
for (var i = 0; i < items.length; i++) {
    init_slider( sliders[i], outputs[i],paramVals[i] );
	//console.log(paramVals)
}

// Get and submit values on button click
submit_button.onclick = function() {
    submit_vals = [ city_input.value, sliders.map( slider => {return slider.value} ) ]
    //console.log( submit_vals )
}
