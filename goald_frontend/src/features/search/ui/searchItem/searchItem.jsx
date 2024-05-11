import { Link } from "react-router-dom";
import defaultGroupImage from "shared/assets/images/defaultGroupImage.png";

import "./dropdownSearchItem.scss";

export function SearchItem(props) {
  const { avatar = defaultGroupImage, groupName, groupTag } = props;

  return (
    <Link to={url} className="search-item">
      <img src={avatar} className="search-item__avatar" alt="Book cover." />
      <div className="search-item__overview">
        <div className="search-item__overview_name">{groupName}</div>
        {groupTag && (
          <div className="search-item__overview_tag">{groupTag}</div>
        )}
      </div>
    </Link>
  );
}
