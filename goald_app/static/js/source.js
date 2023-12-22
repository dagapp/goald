$(document).ready(function () {
    var manager = new Manager();

    function init() {
        manager.init();
    }

    init();

    $("#logo").on("click", () => {
        init();
    });

    $("body").fadeIn("slow");
});

class List {
    constructor(list_type) {
        var self = this;

        var get                 = list_type.get;
        var add                 = list_type.add;
        var add_btn             = list_type.add_btn;
        var del                 = list_type.del;
        var del_btn             = list_type.del_btn;
        var parent              = list_type.parent;
        var get_element_html    = list_type.get_element_html;
        var get_no_element_html = list_type.get_no_element_html;

        var elements = [];

        self.get_elements = function () {
            return elements;
        };

        self.get_chosen_element = function () {
            var id_str = parent.find(".list-element-chosen").attr("id");
            if (id_str)
            {
                var id_split = id_str.split("-");
                var id = Number(id_split[id_split.length - 1]);
                return elements[id];
            } else {
                return null;
            }
        };

        self.init = function () {
            if (add_btn && add) add_btn.on("click", () => add());
            if (del_btn && del) del_btn.on("click", () => del());
            self.update();
        };

        self.update = function (params) {
            clear();
            get(params).then(els => {
                if (els && els.length) {
                    els.forEach((el, index) => {
                        elements.push(el)
                        add_element(el, index);
                    });
                } else {
                    add_no_element();
                }
            });
        };

        function add_element(element, index) {
            parent.append(get_element_html(element).attr("id", `list-element-${index}`));
        }

        function add_no_element() {
            parent.append(get_no_element_html());
        }

        function clear() {
            elements = [];
            parent.empty();
        }
    }
}

class Group {
    constructor(group) {
        var self = this;

        self.id         = group.id;
        self.tag        = group.tag;
        self.name       = group.name;
        self.image      = group.image;
        self.is_private = group.is_private;

        self.users = [];
        if (group.users) {
            group.users.forEach(u => {
                self.users.push(new User(u));
            });
        }

        self.goals = [];
        if (group.goals) {
            group.goals.forEach(g => {
                self.goals.push(new Goal(g));
            });
        }
    }
}

class GroupListType {
    constructor(get, add, del, action) {
        var self = this;

        self.get     = get;
        self.add     = add;
        self.add_btn = $("#add-group-button");
        self.del     = del;
        self.del_btn = $("#del-group-button");
        self.parent  = $("#group-list .list-content");

        self.get_element_html = function (group) {
            return $("<div>")
                .addClass("list-element button shadow")
                .html(`
                    <div class="list-image">
                        <img src="${group.image}" alt="group-image">
                    </div>
                    <div class="list-info">
                        <h2>${group.name}</h2>
                        <p>${group.tag}</p>
                    </div>
                `)
                .bind("click", function () {
                    var do_turn_on = !$(this).hasClass("list-element-chosen");

                    self.parent.find(".list-element-chosen").removeClass("list-element-chosen");
                    if (do_turn_on) $(this).addClass("list-element-chosen");

                    action(group);
                });
        };

        self.get_no_element_html = function () {
            return $("<div>")
                .addClass("list-element no-element")
                .html(`
                    <h2 class="title">Нет групп</h2>
                `);
        };
    }
}

class Goal {
    constructor(goal) {
        var self = this;

        self.name         = goal.name;
        self.is_active    = goal.is_active;
        self.deadline     = goal.deadline;
        self.alert_period = goal.alert_period;

        self.current_value = goal.current_value;
        self.final_value   = goal.final_value;

        self.user_current_value = goal.user_current_value;
        self.user_final_value = goal.user_final_value;

        self.events = [];
        if (goal.events) {
            goal.events.forEach(e => {
                self.events.push(new Event(e));
            });
        }

        self.reports = [];
        if (goal.reports) {
            goal.reports.forEach(r => {
                self.reports.push(new Report(r));
            });
        }
    }
}

class GoalListType {
    constructor(get, add, del, action) {
        var self = this;

        self.get     = get;
        self.add     = add;
        self.add_btn = $("#add-goal-button");
        self.del     = del;
        self.del_btn = $("#del-goal-button");
        self.parent  = $("#goal-list .list-content");

        self.get_element_html = function (goal) {
            return $("<div>")
                .addClass("list-element button shadow")
                .html(`
                    <div class="goal-list-title">
                        <h2 class="title-text">${goal.name}</h2>
                        <h4 class="title-text" style="float: right; color: grey;">@group</h4>
                    </div>
                    <div class="goal-list-status">
                        <span class="${goal.is_active ? "active-status" : "notactive-status"}"></span>
                        <p>${goal.is_active ? "активна" : "не активна"}</p>
                    </div>
                `)
                .bind("click", function () {
                    var do_turn_on = !$(this).hasClass("list-element-chosen");

                    self.parent.find(".list-element-chosen").removeClass("list-element-chosen");
                    if (do_turn_on) $(this).addClass("list-element-chosen");

                    action(goal);
                });
        };

        self.get_no_element_html = function () {
            return $("<div>")
                .addClass("list-element no-element")
                .html(`
                    <h2 class="title-text">Нет целей</h2>
                `);
        };
    }
}

class User {
    constructor (user) {
        var self = this;

        self.login       = user.login;
        self.name        = user.name;
        self.second_name = user.second_name;
    }
}

class UserListType {
    constructor(get, add, del, action) {
        var self = this;

        self.get     = get;
        self.add     = add;
        self.add_btn = $("#add-user-button");
        self.del     = del;
        self.del_btn = $("#del-user-button");
        self.parent  = $("#user-list .list-content");

        self.get_element_html = function (user) {
            return $("<div>")
                .addClass("list-element button shadow")
                .html(`
                    <div class="list-image">
                        <img src="/media/group/default.jpg" alt="user-image">
                    </div>
                    <div class="list-info">
                        <h2>${user.login}</h2>
                        <p>${user.name} ${user.second_name}</p>
                    </div>
                    <!--
                    <div style="display: inline-block">
                        <h3 style="display: inline-block">0</h3>
                        <h3 style="display: inline-block">/</h3>
                        <h3 style="display: inline-block">0</h3>
                    </div>
                    -->
                    <div class="buttons">
                        <h2 class="alter-button grey-button">+</h2>
                        <h2 class="alter-button grey-button">-</h2>
                    </div>
                `);
        };

        self.get_no_element_html = function () {
            return $("<div>")
                .addClass("list-element no-element")
                .html(`
                    <h2 class="title-text">Нет целей</h2>
                `);
        };
    }
}

class Event {
    constructor(event) {
        var self = this;

        self.type = event.type;
        self.text = event.text;
        self.timestamp = event.timestamp;
    }
}

class EventListType {
    constructor(get) {
        var self = this;

        self.get     = get;
        self.add     = null;
        self.add_btn = null;
        self.del     = null;
        self.del_btn = null;
        self.parent  = $("#event-list .list-content");

        self.get_element_html = function (event) {
            return $("<div>")
                .addClass("list-element button shadow")
                .html(`
                    <div class="goal-list-title">
                        <h2 class="title-text">${event.text}</h2>
                        <h4 class="title-text" style="float: right; color: grey;">${event.timestamp}</h4>
                    </div>
                `);
        };

        self.get_no_element_html = function () {
            return $("<div>")
                .addClass("list-element no-element")
                .html(`
                    <h2 class="title-text">Нет событий</h2>
                `);
        };
    }
}

class Profile {
    constructor(get) {
        var self = this;

        self.group = null;
        self.goal = null;

        self.update = async function () {
            get().then(params => {
                self.group = params.group;
                self.goal = params.goal;

                hideGroup();
                hideGoal();

                console.log(self.group, self.goal);

                $("#entity").slideDown("fast");
                if (self.goal != null) {
                    showGoal(self.goal);
                } else if (self.group != null) {
                    showGroup(self.group);
                } else {
                    $("#entity").slideUp("fast");
                }
            });
        };

        function showGroup (group) {
            $("#group-info-image").attr("src", group.image);
            $("#group-info-name").text(group.name);
            $("#group-info-tag").text(group.tag);
            $("#group-info-container").fadeIn("fast");
        }

        function hideGroup () {
            $("#group-info-container").fadeOut("fast");
        }

        function showGoal (goal) {
            $("#goal-info-name").text(goal.name);
            $("#goal-list-deadline").text(goal.deadline);
            $("#goal-list-user-current-value").text(goal.user_current_value);
            $("#goal-list-user-final-value").text(goal.user_final_value);
            $("#goal-list-current-value").text(goal.current_value);
            $("#goal-list-final-value").text(goal.final_value);

            $("#goal-info-container").fadeIn("fast");
        }

        function hideGoal () {
            $("#goal-info-container").fadeOut("fast");
        }
    }
}

class Manager {
    constructor() {
        var self = this;

        var api = new API();

        self.group_list = new List(new GroupListType(
            api.get_group_list,
            api.add_group,
            api.del_group, 
            function action (group) { 
                self.goal_list.update(group);
                self.user_list.update(group);
                self.event_list.update(group);
                self.profile.update();
            }
        ));

        self.goal_list = new List(new GoalListType( 
            function get () {
                return new Promise(resolve => {
                    var chosen_group = self.group_list.get_chosen_element();
                    if (chosen_group) {
                        var goals = chosen_group.goals;
                        if (goals) {
                            resolve(goals);
                        } else {
                            resolve();
                        }
                    } else {
                        var goals = [];
                        self.group_list.get_elements().forEach(el => {
                            el.goals.forEach(el_g => {
                                goals.push(el_g);
                            });
                        });
                        resolve(goals);
                    }
                })
            }, 
            function add () { }, 
            function del () { }, 
            function action (goal) {
                self.event_list.update(goal);
                self.profile.update();
            }
        ));

        self.user_list = new List(new UserListType(
            function get () {
                return new Promise(resolve => {
                    var chosen_group = self.group_list.get_chosen_element();
                    if (chosen_group) {
                        resolve(chosen_group.users);
                    } else {
                        resolve(null);
                    }
                });
            },
            function add () {

            },
            function del () {

            },
            function action (user) {

            }
        ));

        self.event_list = new List(new EventListType(
            function get() {
                return new Promise(resolve => {
                    var chosen_group = self.group_list.get_chosen_element();
                    if (chosen_group) {
                        resolve(chosen_group.events);
                    } else {
                        var events = [];
                        self.group_list.get_elements().forEach(el => {
                            el.events.forEach(el_g => {
                                events.push(el_g);
                            });
                        });
                        resolve(events);
                    }
                });
            }
        ));

        self.profile = new Profile(function () {
            return new Promise(resolve => resolve({group: self.group_list.get_chosen_element(), goal: self.goal_list.get_chosen_element()}));
        });

        self.init = function () {
            self.group_list.init();
            self.goal_list.init();
            self.user_list.init();
            self.event_list.init();
        };

        self.update = function () {
            self.group_list.update();
            self.goal_list.update();
            self.user_list.update();
            self.event_list.update();
            self.profile.update();
        };
    }
}

class Modal {
    constructor() {
        var self = this;

        self.open = function () {
            $("#blackout").fadeIn("fast");
        };

        self.close = function () {
            $("#blackout").fadeOut("fast");
        };
    }
}

class API {
    constructor() {
        var self = this;
        var headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
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

        function post(url, data) {
            var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
            return fetch(url, {
                method: "POST",
                headers: { ...headers },
                body: `csrfmiddlewaretoken=${csrfmiddlewaretoken}&data=${JSON.stringify(data)}`
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
                    });
                }
            });
        }

        self.get_group_list = async function () {
            let groups = await get("group/list")
                .then(g => {
                    var result = [];
                    g.forEach(group => {
                        result.push(new Group(group));
                    });
                    return result;
                });
            return groups;
        };

        self.create_group = async function (group) {
            return await post("group/create", {
                "tag": group.tag,
                "name": group.name,
                "image": group.image,
                "is_private": group.is_private
            });
        };

        self.join_group = async function (group_tag) {
            return await post("group/users/add", {
                "tag": group_tag
            });
        };

        self.create_goal = async function (group_id, goal) {
            return await post("goal/create", {
                "group_id": group_id,
                "name": goal.name,
                "deadline": goal.deadline,
                "alert_period": goal.alert_period,
                "final_value": goal.final_value
            });
        };

        self.pay = async function (goal_id, value) {
            return await post("goal/pay", {
                "goal_id": goal_id,
                "value": value
            });
        };
    }
}

function setBlackout() {
    $("#blackout").fadeIn("fast");
}

function removeBlackout() {
    $("#blackout").fadeOut("fast");
}

function openModal(modalId) {
    $("#" + modalId).fadeIn("fast");
    setBlackout();
}

function closeModal(modalId) {
    $("#groupActionWindow").fadeOut("fast");
    $("#" + modalId).fadeOut();
    removeBlackout();
}

function createGroupButtonPressed() {
    var api = new API();
    api.create_group(new Group({
        tag: $("#creategroup-tag").val(),
        name: $("#creategroup-name").val(),
        is_private: false
    }));
    closeModal("createGroupWindow");
}

function joinGroupButtonPressed() {
    var api = new API();
    api.join_group($("#joingroup-tag").val());
    closeModal('joinGroupWindow');
}

function createGoalButtonPressed() {
    var api = new API();
    api.create_goal(0, new Goal({
        name: $("#creategoal-name").val(),
        deadline: $("#creategoal-deadline").val(),
        final_value: $("#creategoal-sum").val(),
        alert_period: $("#creategoal-period").val()
    }));
    closeModal("createGoalWindow");
}

function acceptDeleteGroup() {
    closeModal('deleteGroupWindow');
}

function acceptDeleteGoal() {
    closeModal('deleteGoalWindow');
}

function pay() {
    var api = new API();
    api.pay(0, $("#pay-sum").val());
    closeModal('payWindow');
}
