import { useState } from "react";

import clsx from "clsx";
import "./input.scss";

export function Input(props) {
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
  const onChangeinputData = (e) => {
    setinputData(e.target.value);
  };

  return (
    <div className={clsx("input", className)}>
      <input
        id="input"
        className={"input__field"}
        type={type}
        value={inputData}
        onBlur={onBlur}
        onFocus={onFocus}
        onChange={onChange ?? onChangeinputData}
        onKeyDown={onKeyDown}
        required
      />
      <label for="input" className="input__label">
        {placeholder}
      </label>
    </div>
  );
}
