$(document).ready(function () {
    $("#openModal").on("click", () => {

    });
});

function update_group_list() {

}

function update_group_info() {

}

var GroupList = function () {

};

var GroupProfile = function() {
    
};

var API = function () {
    var self = this;
    var path = "info/group";
    var headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    function get(url) {
        return fetch(url)
            .then(r => {
                if (r.ok) {
                    return r.json;
                } else {
                    throw new Error(`Bad response: ${r.status} ${r.statusText}`);
                }
            })
            .then(d => {
                if (d.ok) {

                } else {
                    throw new Error(`Empty result`);
                }
            });
    }

    function get_group_info() {

    }
};