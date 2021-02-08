function addBanner() {

    // let banner = document.createElement('div');
    // let bannernode = document.createTextNode("The sales is ending in 10 mins");
    // banner.appendChild(bannernode);
    // document.body.appendChild(banner);
    // banner.style.border = "solid 1 px black";
    

}

let banner = document.createElement('div');
// let bannernode = document.createTextNode("The sales is ending in 10 mins");
// banner.appendChild(bannernode);
document.body.appendChild(banner);
banner.style.border = "solid 1 px black";

let h1 = document.createElement('h1');
h1.innerHTML = "The sales end in 10 ";
h1.id = "countdown";
h1.style.color = "blue";
banner.appendChild(h1);

setTimeout(addBanner, 5000);

let timeleft = 10;
let downloadTimer = setInterval(function () {
    if (timeleft <= 0) {
        clearInterval(downloadTimer);
        document.getElementById("countdown").innerHTML = "Finished";
    } else {
        document.getElementById("countdown").innerHTML = "The sales end in " + timeleft + " seconds remaining";
    }
    timeleft -= 1;
}, 1000);
