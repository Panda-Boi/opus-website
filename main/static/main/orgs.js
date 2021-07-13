document.addEventListener('DOMContentLoaded', load);
   
function expandOrg(event) {

    if(event.target.nodeName != "DIV") {
        var name = event.target.parentNode.dataset.name;
    } else {
        var name = event.target.dataset.name;
    }

    window.location.href = `org?name=${name}`;

};

function showAll(event) {
    window.location.href = event.target.dataset.url + "?all=True";
};

function showRelated() {
    window.location.href = "organisations";
};