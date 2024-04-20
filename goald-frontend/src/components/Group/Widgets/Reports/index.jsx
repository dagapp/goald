import Menu from "@components/Utils/Menu"
import Card from "@components/Utils/Card";

import docIcon from "@assets/icons/utils/document.svg";
import "./Reports.scss";

export default function Reports() {
  return (
    <Card
      title={"Reports"}
      children={
        <Menu
          elements={[
            {
              icon: docIcon,
              title: "Report 1",
            },
            {
              icon: docIcon,
              title: "Report 2",
            },
            {
              icon: docIcon,
              title: "Report 3",
            },
          ]}
        />
      }
    />
  );
}
