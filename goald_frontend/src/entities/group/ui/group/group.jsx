import { Link } from "react-router-dom";
import defaultGroupImage from "@shared/assets/images/defaultGroupImage.png";

import "./group.scss";

export function Group(props) {
  const { avatar = defaultGroupImage, name, tag, url } = props;

  return (
    <Link to={url} className="group">
      <img src={avatar} className="group__avatar" alt="Group Avatar" />
      <div className="group__overview">
        <div className="group__overview_name">{name}</div>
        {tag && <div className="group__overview_tag">{tag}</div>}
      </div>
    </Link>
  );
}
