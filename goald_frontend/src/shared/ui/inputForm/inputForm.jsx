import clsx from "clsx";
import "./inputForm.scss";

export function InputForm(props) {
  const {
    id = "id",
    type = "text",
    placeholder,
    className,
    error,
    errorMessage,
    properties,
  } = props;

  return (
    <div className={clsx("input-form", error && "input-form__error-view", className)}>
      <input
        id={`input-form-${id}`}
        className={"input-form__field"}
        type={type}
        {...properties}
        required
      />

      <label htmlFor={`input-form-${id}`} className="input-form__label">
        {placeholder}
      </label>

      {errorMessage && <div className="input-form__error">{errorMessage}</div>}
    </div>
  );
}
