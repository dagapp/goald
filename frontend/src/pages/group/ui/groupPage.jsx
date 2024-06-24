import clsx from "clsx";

import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import { Button } from "@shared/ui/button";

import { GroupDescription } from "@features/groupDescription";
import { GoalsList } from "@features/goals/goalsList";
import { CreateGoal } from "@features/goals/createGoal";
import { EventsList } from "@features/eventsList";

import "./groupPage.scss";

function GroupPageCell(props) {
  const { title, className, children } = props;
  return (
    <div className={clsx("group-page__cell", className)}>
      <h1 className="group-page__cell_header">{title}</h1>
      {children && <div className="group-page__cell_content">{children}</div>}
    </div>
  );
}

export function GroupPage() {
  let { groupId } = useParams();

  const [popUpActive, setPopUpActive] = useState(false);
  const tooglePopUp = () => setPopUpActive(!popUpActive);

  return (
    <>
      <CreateGoal
        id={groupId}
        popUpActive={popUpActive}
        tooglePopUp={tooglePopUp}
      />
      <div className="group-page__wrapper">
        <div className="group-page">
          <GroupPageCell
            title={<GroupDescription id={groupId} />}
            className={"group-page__description"}
          />
          <GroupPageCell
            title={
              <>
                <span>Goals</span>

                <Button
                  className={"group-page__description_button"}
                  onClick={tooglePopUp}
                >
                  Create Goal
                </Button>
              </>
            }
            className={"group-page__goals"}
          >
            <GoalsList id={groupId} />
          </GroupPageCell>
          <GroupPageCell title={"Events"} className={"group-page__events"}>
            <EventsList id={groupId} />
          </GroupPageCell>
          <GroupPageCell title={"Reports"} className={"group-page__reports"} />
        </div>
      </div>
    </>
  );
}
