import {Link} from 'react-router-dom'


import Card from "@components/Utils/Card";
import Avatar from "@components/Utils/Avatar";
import "./groupList.scss";

//Test Array
const groups = [
  {
    Image: "image",
    Name: "Name 1",
    Description: "Description of the Name 1",
  },
  {
    Image: "image",
    Name: "Name 2",
    Description: "Description of the Name 2",
  },
  {
    Image: "image",
    Name: "Name 3",
    Description: "Description of the Name 3",
  },
];

export default function GroupList() {
  return (
    <div className="group-list">
      {groups.map((group, index) => {
        return (
          <Card key={index} 
            children={
              <div className="group-card">
                <Avatar image={group.Image} />
                <div className="group-card__about">
                  <Link to="/group"> 
                  {/* There should be react-router too, but idk API output
                  if can be link or just id (?). Now it's to template group*/}
                    <div className="group-card__about_title">{group.Name}</div>
                  </Link>
                  <div className="group-card__about_desc">
                    {group.Description}
                  </div>
                </div>
              </div>
            }
          />
        );
      })}
    </div>
  );
}
