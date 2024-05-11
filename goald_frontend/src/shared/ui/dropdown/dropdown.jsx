import clsx from "clsx";
import "./dropdown.scss";

export function Dropdown(props) {
  const { labelElement, isOpen, content, className } = props;

  let isOpenDropdown = isOpen ? "dropdown_open" : "dropdown_close";

  if (isOpen === undefined) {
    isOpenDropdown = "dropdown_opening-state_hover";
  }

  return (
    <div className={clsx("dropdown", isOpenDropdown, className)}>
      <div className="dropdown__label">{labelElement}</div>
      <div className="dropdown__content">{content}</div>
    </div>
  );
}
