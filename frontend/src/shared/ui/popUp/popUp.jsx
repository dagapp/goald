import { useState, useEffect } from "react";

import clsx from "clsx";
import "./popUp.scss";

export function PopUp(props) {
  const { className, isOpenPopUp, closePopUp, children } = props;
  
  let isClosed = isOpenPopUp ? "pop-up__open" : "pop-up__closed";

  return (
    <div className={clsx("pop-up__wrapper", isClosed)}>
      <div className="pop-up__background" onClick={closePopUp}></div>

      <div className={clsx("pop-up", className)}>
        <div className="pop-up__header">
          <div className="pop-up__header_close-button" onClick={closePopUp}>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500">
              <path d="M456.851 0 245 212.564 33.149 0 .708 32.337l211.961 212.667L.708 457.678 33.149 490 245 277.443 456.851 490l32.441-32.322-211.961-212.674L489.292 32.337z" />
            </svg>
          </div>
        </div>

        <div className="pop-up__content">{children}</div>
      </div>
    </div>
  );
}
