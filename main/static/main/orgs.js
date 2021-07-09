
let metadata = "{{ metadata }}";
let loggedin = true;
let counter = 0;

const quantity = 20;

//check if user is logged in
if (metadata == "") {
    loggedin = false;
};
    
document.addEventListener('DOMContentLoaded', load);

function load() {

    const start = counter;
    const end = start + quantity - 1;
    
    fetch(`orgs?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.orgs.forEach(add_org);
    })

};

function add_org(contents) {

    // Create new org
    const org = document.createElement('div');
    org.className = 'org';
    org.innerHTML = `<div class="heading"> ${contents.name} </div>` + `<img src="${contents.logo}}">`;
    org.addEventListener("click", function() { expandOrg(contents.name) })

    // Add org to DOM
    document.querySelector('#orgs').append(org);

    //const test = document.createElement('img');
    //test.src = contents.i

};
   
function expandOrg(name) {

    window.location.href = `org?name=${name}`;

};