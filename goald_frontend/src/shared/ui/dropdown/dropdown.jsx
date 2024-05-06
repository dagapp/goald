import clsx from "clsx";
import "./dropdown.scss";

export function Dropdown(props) {
  const {
    labelElement,
    isOpen,
    contentElements,
    openLeft = false,
    className,
  } = props;

  let isOpenDropdown = isOpen ? "dropdown_open" : "dropdown_close";

  if (isOpen === undefined) {
    isOpenDropdown = "dropdown_opening-state_hover";
  }

  return (
    <div
      className={clsx(
        "dropdown",
        isOpenDropdown,
        openLeft && "dropdown_extending_left",
        className
      )}
    >
      <div className="dropdown__label">{labelElement}</div>
      <ul class="dropdown__content">
        {contentElements.map((contentElement, index) => {
          return <li key={index}>{contentElement}</li>;
        })}
      </ul>
    </div>
  );
}
