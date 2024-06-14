import clsx from "clsx";
import "./checkbox.scss";

export function Checkbox(props) {
  const { children, className, properties, disabled = false } = props;

  return (
    <div className={clsx("checkbox", className)}>
      <input
        type="checkbox"
        id="checkbox"
        className="checkbox__input"
        {...properties}
      />
      <div
        className={clsx("checkbox__pseudobox", disabled && "checkbox_disabled")}
      >
        <svg viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M3.66406 8.98528L7.1996 12.5208"
            //stroke="#ECE7F4"
            strokeWidth="2"
            strokeLinecap="round"
          />
          <path
            d="M7.25 12.5711L14.3211 5.49999"
            //stroke="#ECE7F4"
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
      </div>

      {children && (
        <label for="checkbox" className="checkbox__label">
          {children}
        </label>
      )}
    </div>
  );
}
