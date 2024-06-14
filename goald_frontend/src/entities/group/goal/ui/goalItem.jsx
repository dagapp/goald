import clsx from "clsx";

import { ProgressBar } from "@shared/ui/progressBar";
import "./goalItem.scss";

export function GoalItem(props) {
  //after `amount` insert `percentage`
  const { current, amount, daysLeft, className } = props;

  //-> Should be moved to logic part
  const percentage = Math.round((parseInt(current) / parseInt(amount)) * 100);

  return (
    <div className={clsx("goal-item", className)}>
      <div className="goal-item__progress">
        <div className="goal-item__progress_current">
          <div className="goal-item__progress_current_description">Current</div>
          <div className="goal-item__progress_current_wrapper">
            <div className="goal-item__progress_current_wrapper_value">
              ₽{current}
            </div>
            <div className="goal-item__progress_current_wrapper_description">
              {percentage}%
            </div>
          </div>
        </div>
        <div className="goal-item__progress_target">
          <div className="goal-item__progress_target_description">Amount</div>
          <div className="goal-item__progress_target_value">₽{amount}</div>
        </div>
      </div>

      <ProgressBar percentage={percentage} />

      <div className="goal-item__daysleft">
        <svg
          className="goal-item__daysleft_icon"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 7V12L14.5 13.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z"
            stroke="#000000"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>

        <div className="goal-item__daysleft_value">{daysLeft}</div>
        <div className="goal-item__daysleft_description">Days Left</div>
      </div>
    </div>
  );
}
