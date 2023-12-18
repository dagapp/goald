$(document).ready(function () {
    var manager = new Manager();

    function init() {
        manager.init();
    }

    init();

    $(".logo").on("click", () => {
        init();
    });
});

var Group = function (group) {
    var self = this;

    self.id = group.id;
    self.tag = group.tag;
    self.name = group.name;
    self.image = group.image;
};

var Goal = function (goal) {
    var self = this;

    self.name = goal;
};

var Event = function (event) {
    var self = this;
}

var Manager = function () {
    var self = this;

    var group_list = new GroupList();
    var group_profile = new GroupProfile();

    var api = new API();

    self.init = function () {
        group_list.update(api.get_group_list, function (group_id) {
            group_profile.update(api.get_group_info, group_id);
        });
        //group_profile.update(api.get_full_info);
    };
};

var GroupList = function () {
    var self = this;

    self.update = async function (get, action) {
        clear();
        get().then(groups => 
            groups.forEach(group => {
                addGroup(group, action);
            })
        );
    };

    function addGroup (group, action) {
        $(".group-title")
            .after(
                element(group, action)
            );
    }

    function clear() {
        $(".group-list-element").remove();
    }

    function element (group, action) {
        return $("<div>")
            .addClass("shadow group-list-element")
            .html(`
                </li>
                    <a class="group-card">
                        <div class="avatar">
                            <img src="${group.image}" alt="avatar">
                        </div>
                        <div class="group-info">
                            <h2>${group.name}</h2>
                            <p>${group.tag}</p>
                        </div>
                    </a>
                </li>
            `)
            .bind("click", function () {
                return action(group.id)
            });
    };
};

var GroupProfile = function() {
    var self = this;

    var goals_list = new GoalsList();

    self.update = async function (get, group_id) {
        get(group_id).then(result => {
            showGroup(result["group"]);
            showGoals(result["goals"]);
        });
    };

    function showGroup (group) {
        if ($('#group-info-container').css('display') == 'none') {
            $('#group-info-container').slideDown();
        }
        $("#group-info-image").attr("src", group.image);
        $(".group-info-tag").text(group.tag);
        $(".group-info-name").text(group.name);
    }

    function showGoals (goals) {
        goals_list.update(goals);
    }
};

var GoalsList = function() {
    var self = this;

    self.update = function (goals) {
        clear();
        goals.forEach(goal => addGoal(goal));
    };

    function addGoal (goal) {
        $(".goals-container").append(element(goal));
    }

    function clear () {
        $(".goals-card").remove();
    }

    function element (goal) {
        return $("<div>")
            .addClass("goals-card")
            .html(`
                <h2>${goal.name}</h2>
                <span class="active-status"></span>
                <p>${goal.is_active ? "активна" : "не активна"} до ${goal.deadline}</p>
            `);
    };
}

var API = function () {
    var self = this;
    var headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    function get(url) {
        return fetch(url, {
            method: "GET",
            headers: {
                "Accept": "application/json",
            },
        }).then(r => {
                if (r.ok) {
                    return r.json();
                } else {
                    throw new Error(`Bad response: ${r.status} ${r.statusText}`);
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
        let groups = await get("group/list")
            .then(g => {
                group_list = [];
                g.forEach(group => {
                    group_list.push(new Group(group));
                })
                return group_list;
            });
        return groups;
    };

    self.get_full_info = async function () {
        return await get("")
    };

    self.get_group_info = async function (group_id) {
        let result = await get(`group/${group_id}`)
            .then(
                r => {
                    var goals = []
                    r.goals.forEach(g => {
                        goals.push(new Goal(g));
                    });
                    return {"group": new Group(r.group), "goals": goals};
                }
            );
        return result;
    };
};