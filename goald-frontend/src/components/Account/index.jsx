import { useState } from "react";
import Card from "@components/Utils/Card";
import Placeholder from "@components/Utils/Placeholder";

import "./account.scss";

export default function Account() {
  const [accountName, setAccountName] = useState(false);
  return (
    <div className="account">
      <Card
        title={"Account"}
        children={
          <div className="account__settings">
            <div className="account__field">
              <Placeholder description={"Name"} placeholder="Ivan" />
              <Placeholder description={"Surname"} placeholder="Ivanov" />
            </div>
            <button className="button_gradient button_rect">Change</button>
          </div>
        }
      />
    </div>
  );
}
