import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  fetchGoals,
  selectGroupGoals,
  selectGoalsError,
  selectGoalsLoading,
} from "@features/goals/goalsList";

import { GoalItem } from "@entities/group/goal/";

import "./goalsList.scss";

export const GoalsList = (props) => {
  const { id } = props;

  const goals = useSelector(selectGroupGoals);
  const loading = useSelector(selectGoalsLoading);
  const error = useSelector(selectGoalsError);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchGoals({ id }));
  }, [id]);

  const renderContent = () => {
    if (!goals && !loading) {
      return "Create your first goal!";
    }

    if (loading) {
      return <div className="goals-list__loading">Loading...</div>;
    }

    if (error) {
      return <span className="goals-list__error">{error.messageError}</span>;
    }

    // On the final stage
    if (goals != null && goals.length > 0) {
      return (
        <div className="goals-list">
          {goals?.map((goal, index) => (
            <GoalItem
              key={index}
              name={goal.name}
              current={goal.current_value}
              amount={goal.final_value}
            />
          ))}
        </div>
      );
    }
  };

  return renderContent();
};
