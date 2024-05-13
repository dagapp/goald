import { Link } from "react-router-dom";
import defaultGroupImage from "@shared/assets/images/defaultGroupImage.png";

import "./searchItem.scss";

export function SearchItem(props) {
  const { avatar = defaultGroupImage, title, tag, url } = props;

  return (
    <Link to={url} className="search-item">
      <img src={avatar} className="search-item__avatar" alt="Group Avatar" />
      <div className="search-item__overview">
        <div className="search-item__overview_name">{title}</div>
        {tag && <div className="search-item__overview_tag">{tag}</div>}
      </div>
    </Link>
  );
}
