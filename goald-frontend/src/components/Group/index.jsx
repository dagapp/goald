import Goals   from "@components/Group/Widgets/Goals";
import Info    from "@components/Group/Widgets/Info";
import Reports from "@components/Group/Widgets/Reports";
import Actions from "@components/Group/Widgets/Actions";

// Test Templeate of data
import { template } from "./groupCards";
import "./group.scss";

export default function Group() {
  const name = template["title"];
  const description = template["description"];
  
  const goals = template["goals"];
  const tags = template["tags"];

  return (
    <div className="group-content">
      <div className="group-content__goals group-content__column">
        <Goals 
          goals={goals}
        />
      </div>

      <div className="group-content__actions group-content__column">
        <Actions />
      </div>

      <div className="group-content__reports group-content__column">
        <Reports />
      </div>

      <div className="group-content__info group-content__column">
        <Info
          name={name}
          description={description}
          tags={tags}
        />
      </div>
    </div>
  );
}
