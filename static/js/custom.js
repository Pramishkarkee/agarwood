// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

jQuery(document).ready(function ($) {
    
    function textLimit(elements,maxTextLength) {
        for (var i = 0; i < elements.length; i++){
            if (elements[i].innerHTML.length > maxTextLength)
            elements[i].innerHTML = elements[i].innerHTML.slice(0,maxTextLength) + '...';
        }
    }
    
    textLimit($('.content').find('p'),200);
    
});