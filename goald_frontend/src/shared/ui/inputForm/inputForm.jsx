import { useState } from "react";

import clsx from "clsx";
import "./inputForm.scss";

export function InputForm(props) {
  const {
    type,
    placeholder,
    onChange,
    onBlur,
    onFocus,
    onKeyDown,
    className,
  } = props;

  const [inputData, setinputData] = useState("");
  const onChangeinputData = (event) => {
    setinputData(event.target.value);
  };

  return (
    <div className={clsx("input-form", className)}>
      <input
        id="input-form"
        className={"input-form__field"}
        type={type}
        value={inputData}
        onBlur={onBlur}
        onFocus={onFocus}
        onChange={onChange ?? onChangeinputData}
        onKeyDown={onKeyDown}
        required
      />
      <label for="input-form" className="input-form__label">
        {placeholder}
      </label>
    </div>
  );
}
