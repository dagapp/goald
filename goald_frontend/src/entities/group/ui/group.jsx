import clsx from "clsx";
import "./group.scss";

export function Group(props) {
  const { avatar, groupName, groupTag, className } = props;

  return (
    <div className={clsx("group", className)}>
      <img src={avatar} className="group__avatar" alt="avatar" />
      <div className="group__overview">
        <div className="group__overview_name">{groupName}</div>
        {groupTag && (
          <div className="group__overview_tag">{groupTag}</div>
        )}
      </div>
    </div>
  );
}
