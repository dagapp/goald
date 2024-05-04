import clsx from "clsx";
import "./button.scss";

export function Button(props) {
  const {
    children,
    Icon,
    disabled = false,
    className,
    onClick,
  } = props;

  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "button",
        disabled && "button_disabled",
        className
      )}
    >
      {Icon && <Icon />}
      {children}
    </button>
  );
}
