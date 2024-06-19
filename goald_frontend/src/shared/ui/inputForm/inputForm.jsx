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
    <div
      className={clsx(
        "input-form",
        error && "input-form__error-view",
        className
      )}
    >
      <div className="div input-form__input-wrapper">
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
      </div>

      {errorMessage && <div className="input-form__error">{errorMessage}</div>}
    </div>
  );
}
