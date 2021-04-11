const url = document.URL;

function resizing() {
    if (window.matchMedia("(max-width: 855px)").matches) {
        document.getElementById('navbar').innerHTML = `
            <div class="nav_item">
                <div id="logo"><img src="static/Images/logo.jpg" alt="logo" id="logo-img" onclick="homeFunction()"></div>
                <div id="hambarger" onclick="hambargerFunction()">
                    <div class="bars"></div>
                    <div class="bars"></div>
                    <div class="bars"></div>
                </div>
            </div>
            <!-- Links for mobile navbar -->
            <div class="nav_item">
                <div id="myLinks">
                    <button class="links" onclick="homeFunction()">Home</button>
                    <button class="links" onclick="servicesFunction()">Services</button>
                    <button class="links" onclick="playlistFunction()">Your Playlists</button>
                    <button class="links" onclick="aboutFunction()">About Us</button>
                    <button class="links" onclick="contactFunction()">Contact Us</button>
                </div>
            </div>`
    }
    else {
        document.getElementById('navbar').innerHTML = `
            <div id="logo">
                <div id="logo"><img src="static/Images/logo.jpg" alt="logo" id="logo-img" onclick="homeFunction()"></div>
            </div>
            
            <ul id="navigation">
                <li><button class="tabs" onclick="homeFunction()">Home</button></li>
                <li><button class="tabs" onclick="servicesFunction()">Services</button></li>
                <li><button class="tabs" onclick="playlistFunction()">Your Playlists</button></li>
                <li><button class="tabs" onclick="aboutFunction()">About Us</button></li>
                <li><button class="tabs" onclick="contactFunction()">Contact Us</button></li>
            </ul>

            <div id="search">
                <input type="text" name="query" id="searchBox">
                <img src="static/Images/search.png" alt="search-logo" id="search-logo">
            </div>`
    }
}

function hambargerFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "flex") {
        x.style.display = "none";
    }
    else {
        x.style.display = "flex";
    }
}

function homeFunction() {
    if (window.location.pathname == "/"){
        scrollTo(0, 0);
    }
    else{
        window.open("/","_self")
    }
}

function servicesFunction() {
    if (window.location.pathname == "/"){
        const services_height = window.scrollY + document.querySelector('#services').getBoundingClientRect().top - navbar.offsetHeight;
        scrollTo(0, services_height);
    }
    else{
        window.open("/","_self")
        const services_height = window.scrollY + document.querySelector('#services').getBoundingClientRect().top - navbar.offsetHeight;
        window.onload(scrollTo(0, services_height));
    }
}

function playlistFunction(){
    window.open("/playlist","_self")
}

function aboutFunction() {
    if (window.location.pathname == "/"){
        const about_height = window.scrollY + document.querySelector('#about-us').getBoundingClientRect().top - navbar.offsetHeight;
        window.onload(scrollTo(0, about_height));
    }
    else{
        window.open("/","_self")
        const about_height = window.scrollY + document.querySelector('#about-us').getBoundingClientRect().top - navbar.offsetHeight;
        window.onload(scrollTo(0, about_height));
    }
}

function contactFunction(){
    window.open("/contact","_self")
}

resizing()