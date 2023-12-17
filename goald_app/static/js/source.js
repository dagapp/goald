$(document).ready(function () {
    var manager = new Manager();

    function init() {
        manager.init();
    }

    init();

    $("#logo").on("click", () => {
        init();
    });

    $("#openModal").on("click", () => {

    });
});

var Manager = function () {
    var self = this;

    var groups = [];

    var group_list = new GroupList();
    var group_profile = new GroupProfile();

    var api = new API();

    var init = function () {
        group_list.update(api.get_group_list);
        group_profile.update(api.get_group_info);
    };
};

var GroupList = function () {
    var self = this;

    self.update = function (group_list) {
        group_list.forEach(group => {
            addGroup(group);
        });
    };

    function addGroup (group) {
        $("#group-container")
            .append(
                element(group.id, group.tag, group.name, group.image_url, )
            );
    }

    function element (id, tag, name, image_url, action) {
        return $("<button>")
            .attr({
                type: "button",
            })
            .addClass("groupListButton")
            .html("")
            .bind("click", action())
    };
};

var GroupProfile = function() {
    var self = this;
};

var Group = function () {
    var self = this;

    var id = 0;
    var tag = "";
    var type = 0;
    var name = "";
    var image_url = "";
    var leader_id = 0;
};

var API = function () {
    var self = this;
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
                    return d.result;
                } else {
                    throw new Error(`Empty result`);
                }
            });
    }

    function post(url) {
        return fetch(url, {
            method: "POST",
            headers: {...headers},
            body: data
        }).then(r => {
            if (r.ok) {
                return r.json();
            } else {
                return r.json().then(err => {
                    if ("error" in err) {
                        throw new Error(`Bad response: ${err.error}`);
                    }
                }).catch(err => {
                    console.log(err);
                    return err;
                }).then((err) => {
                    if (err == null) {
                        throw new Error(`Bad response: ${r.status} ${r.statusText}`);
                    }
                }).catch(err => {
                    console.log(err);
                    return err;
                })
            }
        });
    }

    self.get_group_list = async function () {
        return await get("group/list");
    };

    self.get_full_info = async function () {
        return await get("")
    };

    self.get_group_info = async function (group_id) {
        return await get(`group/${group_id}`);
    };
};