import Card from "@components/Utils/Card";
import Avatar from "@components/Utils/Avatar";

import "./Info.scss";

export default function Info(props) {
  const { name, image, description, tags } = props;
  return (
    <Card
      children={
        <div className="group-info">
          <div className="group-info_banner"></div>
          <div className="group-info_avatar">
            <Avatar image={image} />
          </div>

          {/* Should this be with .toString()??? */}
          <div className="group-info_title card-title">{name}</div>
          <div className="group-info_description">
            <div className="group-info_description_icon">
              <svg
                fill="#ECE7F4"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M21,2H3A1,1,0,0,0,2,3V21a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V3A1,1,0,0,0,21,2ZM4,4H20V6H4ZM20,20H4V8H20ZM6,12a1,1,0,0,1,1-1H17a1,1,0,0,1,0,2H7A1,1,0,0,1,6,12Zm0,4a1,1,0,0,1,1-1h5a1,1,0,0,1,0,2H7A1,1,0,0,1,6,16Z" />
              </svg>
            </div>
            <div className="group-info_description_content">{description}</div>
          </div>

          <div className="group-info_tags">
            <div className="group-info_tags_icon">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M7.0498 7.0498H7.0598M10.5118 3H7.8C6.11984 3 5.27976 3 4.63803 3.32698C4.07354 3.6146 3.6146 4.07354 3.32698 4.63803C3 5.27976 3 6.11984 3 7.8V10.5118C3 11.2455 3 11.6124 3.08289 11.9577C3.15638 12.2638 3.27759 12.5564 3.44208 12.8249C3.6276 13.1276 3.88703 13.387 4.40589 13.9059L9.10589 18.6059C10.2939 19.7939 10.888 20.388 11.5729 20.6105C12.1755 20.8063 12.8245 20.8063 13.4271 20.6105C14.112 20.388 14.7061 19.7939 15.8941 18.6059L18.6059 15.8941C19.7939 14.7061 20.388 14.112 20.6105 13.4271C20.8063 12.8245 20.8063 12.1755 20.6105 11.5729C20.388 10.888 19.7939 10.2939 18.6059 9.10589L13.9059 4.40589C13.387 3.88703 13.1276 3.6276 12.8249 3.44208C12.5564 3.27759 12.2638 3.15638 11.9577 3.08289C11.6124 3 11.2455 3 10.5118 3ZM7.5498 7.0498C7.5498 7.32595 7.32595 7.5498 7.0498 7.5498C6.77366 7.5498 6.5498 7.32595 6.5498 7.0498C6.5498 6.77366 6.77366 6.5498 7.0498 6.5498C7.32595 6.5498 7.5498 6.77366 7.5498 7.0498Z"
                  stroke="#ECE7F4"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </div>

            <div className="group-info_tags_content">
              {tags.map((tag, index) => {
                return (
                  <div key={index} className="group-info_tag">
                    {tag.value}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      }
    />
  );
}
