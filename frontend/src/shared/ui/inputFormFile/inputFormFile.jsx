import clsx from "clsx";
import "./inputFormFile.scss";

export function InputFormFile(props) {
  const { placeHolder, className, onChange, error, errorMessage, properties } =
    props;

  return (
    <div
      className={clsx(
        "input-form-file__wrapper",
        error && "input-form-file__error-view",
        className
      )}
    >
      <label className="input-form-file__label">
        <input
          type={"file"}
          className={"input-form-file__field"}
          {...properties}
          onChange={onChange}
        />
        <span className="input-form-file__button">Choose Avatar</span>
        <span className="input-form-file__description">{placeHolder}</span>
      </label>

      {errorMessage && (
        <div className="input-form-file__error">{errorMessage}</div>
      )}
    </div>
  );
}

InputFormFile;
