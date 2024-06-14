import clsx from "clsx";

import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { Button } from "@shared/ui/button";

import {
  fetchGroupDescription,
  selectGroupDescription,
  selectGroupDescriptionError,
  selectGroupDescriptionLoading,
} from "@entities/group/groupDescription";

import { GoalsList } from "@features/goals/goalsList";
import { CreateGoal } from "@features/goals/createGoal";

import { EventsList } from "@features/eventsList";

import "./groupPage.scss";

function GroupPageCell(props) {
  const { title, className, children } = props;
  return (
    <div className={clsx("group-page__cell", className)}>
      <h1 className="group-page__cell_header">{title}</h1>
      { children  && (
        <div className="group-page__cell_content">{children}</div>
      )}
    </div>
  );
}

export function GroupPage(props) {
  const { id } = props;

  const [popUpActive, setPopUpActive] = useState(false);
  const tooglePopUp = () => setPopUpActive(!popUpActive);

  const groupDescription = useSelector(selectGroupDescription);
  const groupDescriptionLoading = useSelector(selectGroupDescriptionLoading);
  const groupDescriptionError = useSelector(selectGroupDescriptionError);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchGroupDescription({ id }));
  }, []);

  const name = groupDescription;

  return (
    <div className="group-page__wrapper">
      <CreateGoal id={id} popUpActive={popUpActive} tooglePopUp={tooglePopUp} />
      <div className="group-page">
        <GroupPageCell title={name} className={"group-page__description"} />
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
          <GoalsList id={id} />
        </GroupPageCell>
        <GroupPageCell title={"Events"} className={"group-page__events"}>
          <EventsList id={id} />
        </GroupPageCell>
        <GroupPageCell title={"Reports"} className={"group-page__reports"} />
      </div>
    </div>
  );
}
