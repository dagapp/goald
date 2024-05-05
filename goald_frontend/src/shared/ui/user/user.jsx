import "./user.scss";

export function User(props) {
  const { avatar, userName, userDescription, className } = props;

  return (
    <div className={clsx("user", className)}>
      <img src={avatar} className="user__avatar" alt="avatar" />
      <div className="user__overview">
        <div className="user__overview_username">{userName}</div>
        <div className="user__overview_description">{userDescription}</div>
      </div>
    </div>
  );
}
