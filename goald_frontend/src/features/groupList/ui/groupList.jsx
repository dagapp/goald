import { Link } from "react-router-dom";
import { getUserGroups } from "@shared/api";
import { Group } from "@entities/group";

import "./groupList.scss";

export function GroupList(props) {
  const { groups } = props;
  //   const groups = getUserGroups();
  //   console.log(groups)
  return (
    <ul class="group-list">
      {groups.map((group, index) => {
        return (
          <li key={index}>
            <Link to={group.url}>
              <Group
                avatar={group.avatar}
                groupName={group.name}
                groupTag={group.tag}
              />
            </Link>
          </li>
        );
      })}
    </ul>
  );
}
