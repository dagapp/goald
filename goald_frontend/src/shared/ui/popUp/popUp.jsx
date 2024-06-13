import clsx from "clsx";
import "./popUp.scss";

export function PopUp(props) {
  const { className, onBlur, onFocus, onKeyDown, children } = props;

  return (
    <div
      onBlur={onBlur}
      onFocus={onFocus}
      onKeyDown={onKeyDown}
      className="pop-up__wrapper"
    >
      <div className="pop-up__background"></div>
      <div className={clsx("pop-up", className)}>{children}</div>
    </div>
  );
}
