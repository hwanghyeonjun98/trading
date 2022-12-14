var rolling = document.getElementById("rolling");
 
window.setInterval( function () {
 
	rolling.style.transitionDuration = "400ms";
	rolling.style.marginTop = "-2em";
 
	window.setTimeout( function () {
                  
		rolling.removeAttribute("style");         
		rolling.appendChild(rolling.firstElementChild);
        
	}, 400);
}, 2000);

