import clsx from "clsx";

import { ProgressBar } from "@shared/ui/progressBar";
import "./duty.scss";

export function Duty(props) {
  const { current, amount, percentage, daysLeft, className } = props;
  //const percentage = Math.round((parseInt(current) / parseInt(amount)) * 100); -> Should be moved to logic part

  return (
    <div className={clsx("duty", className)}>
      <div className="duty__progress">
        <div className="duty__progress_current">
          <div className="duty__progress_current_description">Current</div>
          <div className="duty__progress_current_wrapper">
            <div className="duty__progress_current_wrapper_value">
              ₽{current}
            </div>
            <div className="duty__progress_current_wrapper_description">
              {percentage}%
            </div>
          </div>
        </div>
        <div className="duty__progress_target">
          <div className="duty__progress_target_description">Amount</div>
          <div className="duty__progress_target_value">₽{amount}</div>
        </div>
      </div>

      <ProgressBar percentage={percentage} />

      <div className="duty__daysleft">
        <svg
          className="duty__daysleft_icon"
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

        <div className="duty__daysleft_value">{daysLeft}</div>
        <div className="duty__daysleft_description">Days Left</div>
      </div>
    </div>
  );
}
